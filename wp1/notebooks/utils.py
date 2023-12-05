import anndata as ad
import pandas as pd
import subprocess
import os.path
from collections import defaultdict

def load_metadata(adata, metadata_path, seperator='\t', columns_to_keep=None):
    '''
    Loads in cell metadata in adata.obs of a given adata object.

    Metadata file is expected to contain the cell identifiers in the first column.
    These identifiers won't be written to the adata object, but are needed for matching the right metadata to the cells.
    Example data: CATlas metadata

    Args:
        adata (adata object)   : adata object to be annotated
        metadata_path (string) : path to the metadata file
        seperator (string)     : [optional] seperator in the metadata file, default: tab
        columns_to_keep (list) : [optional] list of strings, containing the column names to be written in the adata object. If not given writes all columns to file.

    Returns:
        ---
    '''
    metadata_df = pd.read_csv(metadata_path, sep = seperator, header = 0)
    metadata_df.set_index('cellID', inplace=True)
    if columns_to_keep is not None:
        metadata_df = metadata_df[columns_to_keep]
    adata.obs = adata.obs.merge(metadata_df, left_index=True, right_index=True)


# keep the same parameters and default values as epi.tl.find_genes,
# but dropping the raw parameter since it is not even used in episcanpy's find_genes
def find_genes(adata,
        gtf_file,
        feature_type='gene',
        annotation='HAVANA',
        upstream=5000,
        downstream=0,
        key_added="gene_annotation"):

    def extract_gene_name(attributes):
        attributes_list = attributes.split(';')
        for attribute in attributes_list:
            if 'gene_name' in attribute:
                return attribute.split('"')[1].strip()
        raise KeyError("'gene_name' not found in gtf attributes")

    def parse_region(region):
        if ':' in region and '-' in region:
            chrom, positions = region.split(':')
            begin, end = map(int, positions.split('-'))
        elif '_' in region:
            chrom, begin, end = region.split('_')
            begin, end = int(begin), int(end)
        else:
            raise ValueError(f"Invalid region format: {region}")
        return chrom, begin, end

    genes = defaultdict(list)
    with open(gtf_file) as f:
        for line in f:
            # skip comment lines
            if line.startswith('#'):
                continue

            # gtf data is tab separated
            fields = line.strip().split('\t')

            # only read lines with the correct source and feature_type
            if fields[1] != annotation or fields[2] != feature_type:
                continue

            chrom = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            strand = fields[6]
            attributes = fields[8]
            gene_name = extract_gene_name(attributes)

            if strand == '+':
                adjusted_start = start - upstream
                adjusted_end = end + downstream
            else:
                adjusted_start = start - downstream
                adjusted_end = end + upstream

            genes[chrom].append((adjusted_start, adjusted_end, gene_name))
    genes = dict(genes) # defaultdict -> dict

    # Since we add upstream and downstream offsets, the list might be unsorted
    for chrom in genes:
        # sort by start
        genes[chrom].sort(key=lambda x: x[0])


    # Group and sort regions by chromosome
    regions = defaultdict(list)
    for region in adata.var_names.tolist():
        chrom, start, end = parse_region(region)
        regions[chrom].append((start, end, region))

    for chrom in regions:
        # sort by start
        regions[chrom].sort(key=lambda x: x[0])

    # Perform a merge-like operation for each chromosome
    gene_annotations = defaultdict(set)
    for chrom in regions:
        rs = regions[chrom]
        try:
            gs = genes[chrom]
        except KeyError:
            # chromosome not found in gtf
            for region in rs:
                gene_annotations[region[2]] = ['unassigned']
            continue

        gene_pointer, region_pointer = 0, 0
        while gene_pointer < len(gs) and region_pointer < len(rs):
            gene_start, gene_end, gene_name = gs[gene_pointer]
            region_start, region_end, region_name = rs[region_pointer]

            if gene_end < region_start:
                # Move to the next gene
                gene_pointer += 1
            elif gene_start > region_end:
                # Move to the next region
                region_pointer += 1
            else:
                # Overlap detected
                gene_annotations[region_name].add(gene_name)

                # look through all regions after region_pointer, then go to next gene
                region_pointer2 = region_pointer + 1
                while region_pointer2 < len(rs):
                    region_start2, region_end2, region_name2 = rs[region_pointer2]
                    if gene_end < region_start2:
                        break
                    gene_annotations[region_name2].add(gene_name)
                    region_pointer2 += 1
                gene_pointer += 1

    # label unannotated regions as intergenic
    all_gene_annotations = dict()
    for chrom in regions:
        for _region_start, _region_end, region_name in regions[chrom]:
            annotation = gene_annotations[region_name]
            annotation = ";".join(sorted(annotation)) if len(annotation) > 0 else 'intergenic'
            all_gene_annotations[region_name] = annotation

    # Update adata
    update_df = pd.DataFrame.from_dict(all_gene_annotations, orient='index')
    adata.var[key_added] = update_df


def download(path, url):
    if os.path.exists(path):
        print(f"{path} already exists.")
    else:
        print(f"Downloading {os.path.basename(path)}...")
        subprocess.Popen(f"wget -qO- {url} | gunzip > {path}", shell=True)
        print(f"Download and extraction of {os.path.basename(path)} complete.")
