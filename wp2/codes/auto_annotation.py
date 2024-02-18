import markerrepo.marker_repo as mr
import markerrepo.wrappers as wrap
import markerrepo.annotation as annot
import markerrepo.parsing as pars
import markerrepo.utils as utl
import scanpy as sc
import matplotlib.pyplot as plt
import pandas as pd
import os
import inspect
import re
import math

repo_path = "/mnt/workspace_stud/stud4/annotate_by_marker_and_features-sort"
h5ad_path = "/mnt/workspace_stud/allstud/wp1/data/2024_01_28/heart_lv_SM-IOBHO.h5ad"

adata = sc.read_h5ad(h5ad_path)
annot.list_possible_settings(repo_path, adata=adata)

# Taxonomy ID or Organism Name
# e.g., "human" or 9606
organism = "human"

# Column in .obs table where ranked genes groups are stored
# e.g., "rank_genes_groups"
# Enter None if no ranking has been performed yet
rank_genes_column = None

# Column in .var table where gene symbols or Ensembl IDs are stored
# Enter None if the index column of the .var table already has gene symbols or Ensembl IDs
# that you want to use for your annotation
genes_column = None

# The .obs table column of the clustering you want to annotate (e.g., "leiden" or "louvain")
# If None, you can pick one interactively 
clustering_column_lists = list(adata.uns["clusters"].keys())
#clustering_column_lists = ["lovain_0.1", "lovain_0.25", "lovain_0.5", "lovain_1", "leiden_0.1", "leiden_0.25", "leiden_0.5", "leiden_1", "kmeans_13", "kmeans_16"]

# Specify whether your index of the .var tables are Ensembl IDs (True) or gene symbols (False)
ensembl = mr.check_ensembl(adata)

# Name of the column to add with the final cell type annotation
# If None, all annotation columns will be kept
celltype_column_name = None

# Whether to delete the created marker lists after annotation or not
delete_lists = True

# 
column_specific_terms={"Source":"panglao", "Organism name":"human"}

# 
mr_parameters = [{"style":"two_column", "file_name":"two_column"}]

def validate_settings(settings=None, repo_path=None, adata=None, organism=None, rank_genes_column=None, genes_column=None, 
                      clustering_column=None, ensembl=None, col_to_search=None, search_terms=None, column_specific_terms=None):
    """
    Validates user settings including file paths, anndata object columns, and specified organism.

    Parameters
    ----------
    settings : list of dict, default None
        A list of dictionaries, each containing parameters for 'create_marker_lists' function.
    repo_path : str, default None
        Path to the marker repository.
    adata : anndata.AnnData, default None
        The loaded AnnData object.
    organism : str or int, default None
        Organism name, taxon ID, or both. E.g., "mouse", 10090, or "mouse 10090".
    rank_genes_column : str, default None
        Column in .obs table where ranked genes are stored.
    genes_column : str, default None
        Column in .var table where gene symbols or IDs are stored.
    clustering_column : str, default None
        The column in .obs table of the clustering you want to annotate.
    ensembl : bool, default None
        Whether the genes in the genes_column are Ensembl IDs.
    col_to_search : str, default None
        Column to search in for marker list selection.
    search_terms : list of str, default None
        List of search terms to use for marker list selection.
    column_specific_terms : list of dicts, default None
        List of dictionaries with specific 'col_to_search' and 'search_terms' for each.

    Returns
    -------
    bool :
        Returns True if all settings are valid, otherwise prints the errors and returns False.
    """ 

    errors = []
    combined_df_columns = list(mr.combine_dfs(repo_path=repo_path).columns)
    utl.get_whitelists(repo_path=repo_path, silent_skip=True, update=False)

    # Validate settings dictionaries
    if settings:
        # Validate keys of dictionaries
        valid_params = set(param.name for param in inspect.signature(wrap.create_marker_lists).parameters.values())
        for setting in settings:
            invalid_params = set(setting) - valid_params
            if invalid_params:
                errors.append(f"Invalid parameters in settings: {', '.join(invalid_params)}")
        # Validate values of dictionaries
        if not invalid_params:
            for i, setting in enumerate(settings, 1):
                if "repo_path" in setting:
                    if not setting["repo_path"]:
                        errors.append(f"Settings for marker list {i}: No repo_path provided.")
                    else:
                        if not os.path.exists(setting["repo_path"]):
                            errors.append(f"Settings for marker list {i}: Repo path {setting['repo_path']} does not exist.")
                if "organism" in setting:
                    if not setting["organism"]:
                        errors.append(f"Settings for marker list {i}: No organism provided.")
                    else:
                        organism_str = str(setting["organism"]).strip()
                        is_valid_organism = any(organism_str == valid_entry.split(" ")[0] or organism_str == valid_entry.split(" ")[1] or organism_str == valid_entry for valid_entry in valid_organisms)
                        if not is_valid_organism:
                            formatted_valid_organisms = "\n  - " + "\n  - ".join(valid_organisms)
                            errors.append(f"Settings for marker list {i}: Invalid organism or taxon ID {setting['organism']}.\nAvailable options:{formatted_valid_organisms}\n")
                if "column_specific_terms" in setting:
                    if not setting["column_specific_terms"]:
                        errors.append(f"Settings for marker list {i}: No column specific terms provided.")
                    else:
                        for specific_column in setting["column_specific_terms"]:
                            if specific_column not in combined_df_columns:
                                formatted_combined_df_columns = "\n  - " + "\n  - ".join(combined_df_columns)
                                errors.append(f"Settings for marker list {i}: Invalid col_to_search {specific_column}.\nAvailable columns:{formatted_combined_df_columns}\n") 
                else:
                    if "col_to_search" in setting:
                        if not setting["col_to_search"]:
                            errors.append(f"Settings for marker list {i}: No col_to_search provided.")
                        else:
                            if setting["col_to_search"] not in combined_df_columns:
                                formatted_combined_df_columns = "\n  - " + "\n  - ".join(combined_df_columns)
                                errors.append(f"Settings for marker list {i}: Invalid col_to_search {setting['col_to_search']}.\nAvailable columns:{formatted_combined_df_columns}\n")
                    if "search_terms" in setting:
                        if not setting["search_terms"]:
                            errors.append(f"Settings for marker list {i}: No search_terms provided.")
                if "style" in setting:
                    if not setting["style"]:
                        errors.append(f"Settings for marker list {i}: No style provided.")
                    else:
                        if setting["style"] not in ["two_column", "score", "ui", "panglao"]:
                            errors.append(f"Settings for marker list {i}: Invalid style {setting['style']}. Available styles: two_column, score, ui, panglao")
                    
    # Validate individual parameters
    if repo_path and not os.path.exists(repo_path):
        errors.append(f"Repo path {repo_path} does not exist.")

    if adata is None:
        errors.append("No AnnData object provided.")
        
    # List of valid organisms and their tax IDs
    valid_organisms = utl.read_whitelist("organism", repo_path=repo_path)['whitelist']

    # Validate the organism
    if organism:
        organism_str = str(organism).strip()
        is_valid_organism = any(organism_str == valid_entry.split(" ")[0] or organism_str == valid_entry.split(" ")[1] or organism_str == valid_entry for valid_entry in valid_organisms)
        if not is_valid_organism:
            formatted_valid_organisms = "\n  - " + "\n  - ".join(valid_organisms)
            errors.append(f"Invalid organism or taxon ID {organism}.\nAvailable options:{formatted_valid_organisms}\n")

    # Validate obs and var columns
    if rank_genes_column and rank_genes_column not in adata.obs.columns:
        formatted_obs_columns = "\n  - " + "\n  - ".join(adata.obs.columns)
        errors.append(f"Invalid rank_genes_column {rank_genes_column}.\nAvailable columns in adata.obs:{formatted_obs_columns}\n")

    if genes_column and genes_column not in adata.var.columns:
        formatted_var_columns = "\n  - " + "\n  - ".join(adata.var.columns)
        errors.append(f"Invalid genes_column {genes_column}.\nAvailable columns in adata.var:{formatted_var_columns}\n")

#    if clustering_column and clustering_column not in adata.obs.columns:
#        formatted_obs_columns = "\n  - " + "\n  - ".join(adata.obs.columns)
#        errors.append(f"Invalid column {clustering_column}.\nAvailable columns in adata.obs:{formatted_obs_columns}\n")

    if isinstance(clustering_column, list):
        for column in clustering_column:
            if column and column not in adata.obs.columns:
                formatted_obs_columns = "\n  - " + "\n  - ".join(adata.obs.columns)
                errors.append(f"Invalid column {column}.\nAvailable columns in adata.obs:{formatted_obs_columns}\n")
    else:
        if clustering_column and clustering_column not in adata.obs.columns:
            formatted_obs_columns = "\n  - " + "\n  - ".join(adata.obs.columns)
            errors.append(f"Invalid column {clustering_column}.\nAvailable columns in adata.obs:{formatted_obs_columns}\n")    


    # Validate col_to_search and search_terms based on column_specific_terms if provided
    if column_specific_terms:
        for specific_column in column_specific_terms:
            if specific_column not in combined_df_columns:
                formatted_combined_df_columns = "\n  - " + "\n  - ".join(combined_df_columns)
                errors.append(f"Invalid col_to_search {specific_column}.\nAvailable columns:{formatted_combined_df_columns}\n")
    else:
        # Validate col_to_search using the columns from the combined DataFrames in the repo
        if col_to_search:
            if col_to_search not in combined_df_columns:
                formatted_combined_df_columns = "\n  - " + "\n  - ".join(combined_df_columns)
                errors.append(f"Invalid col_to_search {col_to_search}.\nAvailable columns:{formatted_combined_df_columns}\n")

    # Print errors or confirm validation
    if errors:
        print("Validation failed due to the following errors:")
        print("-" * 40)
        for error in errors:
            print(error)
        print("-" * 40)

        return False
    else:
        print("All settings are valid.")
        print(f"Summary of settings:")
        print("-" * 40)
        print("General parameters:")
        print(f"  Repo path: {repo_path}")
        print(f"  Organism: {organism}")
        print(f"  Rank genes column: {rank_genes_column}")
        print(f"  Genes column: {genes_column}")
        print(f"  Clustering column: {clustering_column}")
        print(f"  Ensembl IDs: {ensembl}")

        if column_specific_terms:
            print(f"  Column specific terms:")
            for i, specific_column in enumerate(column_specific_terms.keys()):
                print(f"    {i+1}. Column to search: {specific_column}, Search terms: {column_specific_terms[specific_column]}")
        else:
            print(f"  Column to search: {col_to_search}")
            print(f"  Search terms: {search_terms}")

        if settings:
            print("\nParameters from dictionary:")
            for i, setting in enumerate(settings, 1):
                print(f"  {i}. Marker list:")
                for key, value in setting.items():
                    print(f"    {key}: {value}")

        print("-" * 40)

    return True

validate_settings(settings=mr_parameters, repo_path=repo_path, adata=adata, organism=organism, 
                        rank_genes_column=rank_genes_column, genes_column=genes_column, clustering_column=clustering_column_lists, ensembl=ensembl,
                        column_specific_terms=column_specific_terms)

marker_lists = wrap.create_multiple_marker_lists(settings=mr_parameters, repo_path=repo_path, organism=organism, 
                                                 ensembl=ensembl, column_specific_terms=column_specific_terms,
                                                 show_lists=True, adata=adata)

def show_tables(annotation_dir=None, n=5, clustering_column="leiden_0.1", show_diff=True):
    """
    Display dataframes for each cluster showing scores, hits, number of genes, mean of UI. Optionally, 
    it can also show both normal and scaled normalized differences of every potential cell type.

    For each cluster, this function reads the corresponding file, sorts the cell types based on their scores.
    If show_diff is True, it calculates both normal and scaled normalized differences between each cell type 
    and its immediate successor, and then displays the dataframe with these additional columns.

    Parameters
    ----------
    annotation_dir : string, default None
        The directory path where the annotation files are stored.
    n : int, default 5
        The maximum number of rows to display for each cluster.
    clustering_column : string, default "leiden_0.1"
        The clustering column used for cell type annotation.
    show_diff : bool, default False
        Whether to show the normalized differences in the output.
    """
    cluster_dict = {}

    path = f'{annotation_dir}/ranked/output/{clustering_column}/ranks'

    files = os.listdir(path)
    for file in files:
        cluster = file.split("_")[1]
        ct_column = f"Cluster {cluster}"
        df = pd.read_csv(f'{path}/{file}', sep='\t', names=[ct_column, "Score", "Hits", "Number of marker genes", "Mean of UI"])

        #df = df.sort_values(by='Score', ascending=False).reset_index(drop=True)

        if show_diff:
            # Calculate and add both normal and scaled diffs to the DataFrame if show_diff is True
            normal_diffs, scaled_diffs = annot.calculate_normalized_diffs(df.rename(columns={ct_column: "Cell type"}))
            df['Normalized Diff'] = df[ct_column].apply(lambda x: normal_diffs.get(x, 0))
            df['Scaled Diff'] = df[ct_column].apply(lambda x: scaled_diffs.get(x, 0))

        cluster_dict[ct_column] = df.head(n)
        display(df.head(n))

    return cluster_dict

def run_annotation(adata, marker_repo=True, SCSA=True, marker_lists=None, mr_obs="mr", scsa_obs="scsa", 
                   rank_genes_column=None, clustering_column=None, reference_obs=None, keep_all=False, 
                   verbose=False, show_ct_tables=False, show_plots=False, show_comparison=False, ignore_overwrite=True,
                   celltype_column_name=None):
    """
    Performs annotations on single cell data and allows the user to choose between different annotation methods. 

    Parameters
    ----------
    adata : AnnData
        The anndata object to annotate.
    marker_repo : bool, default True
        Whether to use Marker Repo annotation.
    SCSA : bool, default True
        Whether to use SCSA annotation.
    marker_lists : list of str, default []
        Paths to marker list files.
    mr_obs : str, default "mr"
        .obs key for Marker Repo annotation.
    scsa_obs : str, default "scsa"
        .obs key for SCSA annotation.
    rank_genes_column : str, default None
        The column of the .uns table which contains the rank genes scores. E.g. "rank_genes_groups". 
        If None, the ranking will be performed on the clustering_column.
    clustering_column : str, default None
        The column of the .obs table which contains the clustering information. E.g. "louvain" or "leiden".
    reference_obs : str, default None
        A reference annotation already present in the .obs table that can be compared with the other annotations.
    keep_all : bool, default False
        If True, all annotation columns will be kept. If False, only the selected annotation column and the reference_obs will be kept.
    verbose : bool, default False
        If True, the function will print additional information.
    show_ct_tables : bool, default False
        If True, the function will show the tables of the annotation.
    show_plots : bool, default False
        If True, the function will show the plots of the annotation.
    show_comparison : bool, default False
        If True, the function will show the comparison of the annotations.
    ignore_overwrite : bool, default False
        If True, the function will not ask for confirmation before overwriting existing files.
    celltype_column_name : str, default None
        The name of the selected cell type annotation column. If None, all annotation columns will be kept.
    """

    if not marker_repo and not SCSA:
        raise ValueError("At least one of 'marker_repo' or 'SCSA' must be True.")

    if marker_lists is None or not marker_lists:
        raise ValueError("No marker lists provided. Please provide a list of marker list paths.")
    
    for marker_list in marker_lists:
        if not os.path.exists(marker_list):
            raise FileNotFoundError(f"Marker list file not found: {marker_list}")
        
    if not clustering_column:
        clustering_column = mr.select(whitelist=list(adata.obs.columns), heading="clustering column")

    if clustering_column not in adata.obs:
        raise ValueError(f"Clustering column '{clustering_column}' not found in adata.obs.")

    if rank_genes_column is not None and rank_genes_column not in adata.uns:
        raise ValueError(f"Rank genes column '{rank_genes_column}' not found in adata.uns.")

    if reference_obs is not None and reference_obs not in adata.obs:
        raise ValueError(f"Reference annotation column '{reference_obs}' not found in adata.obs.")
    
    if not rank_genes_column:
        rank_genes_column = wrap.rank_genes(adata, clustering_column, show_plots=show_plots, verbose=verbose)

    annotation_columns = [] if reference_obs is None else [reference_obs]        

    for marker_list in marker_lists:
        name = marker_list.split('/')[-1]
        annotation_dir = f"./annotation/{name}"
        plot_columns = [] if reference_obs is None else [reference_obs]

        if marker_repo:
            ct_column = f"{mr_obs}_{name}"
            annotation_columns.append(ct_column)
            plot_columns.append(ct_column)
            
            # Execute Marker Repo annotation
            annot.annot_ct(adata, output_path=annotation_dir, db_path=marker_list,
                           cluster_column=clustering_column, rank_genes_column=rank_genes_column, 
                           ct_column=ct_column, verbose=verbose, ignore_overwrite=ignore_overwrite)

            # Show tables and alternative cell types of each cluster
            if show_ct_tables:
                print(f"Tables of cell type annotation with clustering {clustering_column} and marker list {name}:")
                #annot.show_tables(annotation_dir=annotation_dir, n=5, clustering_column=clustering_column, show_diff=True)
                show_tables(annotation_dir=annotation_dir, n=5, clustering_column=clustering_column, show_diff=True)

        if SCSA:
            column_added = f"{scsa_obs}_{name}"
            annotation_columns.append(column_added)
            plot_columns.append(column_added)

            # Execute SCSA annotation
            if verbose:
                celltype_annotation.run_scsa(adata, 
                    gene_column=None, 
                    key=rank_genes_column, 
                    column_added=column_added,
                    inplace=True, 
                    species=None, 
                    fc=1.5, 
                    pvalue=0.05, 
                    user_db=annot.reformat_marker_list(marker_list), 
                    celltype_column="cell_name")
            else:
                with wrap.suppress_logging(logger_name='sctoolbox'):
                    celltype_annotation.run_scsa(adata, 
                        gene_column=None, 
                        key=rank_genes_column, 
                        column_added=column_added,
                        inplace=True, 
                        species=None, 
                        fc=1.5, 
                        pvalue=0.05, 
                        user_db=annot.reformat_marker_list(marker_list), 
                        celltype_column="cell_name")

        umap_plot_file = f"{clustering_column}.png"

        # Show plots
        if show_plots:
            sc.pl.umap(adata, color=column, wspace=0.5, cmap=None, save=umap_plot_file)

    # Compare annotations
    if show_comparison:
        print("Comparison of cell type annotations:")

        
        display(annot.compare_cell_types(adata, clustering_column, annotation_columns))
    
    # Select cell type annotation
    if celltype_column_name:
        annotation_column = mr.select(whitelist=annotation_columns, heading="Select cell type annotation column:")
        adata.obs.rename(columns={annotation_column: celltype_column_name}, inplace=True)
    else:
        keep_all = True

    if not keep_all:
        # Keep only the selected annotation column and reference_obs if provided
        columns_to_keep = [annotation_column]
        if reference_obs is not None and reference_obs in adata.obs.columns:
            columns_to_keep.append(reference_obs)

        columns_to_remove = [col for col in annotation_columns if col not in columns_to_keep]
        adata.obs.drop(columns=columns_to_remove, inplace=True)

    return clustering_column, annot.compare_cell_types(adata, clustering_column, annotation_columns), umap_plot_file, show_tables(annotation_dir=annotation_dir, n=5, clustering_column=clustering_column, show_diff=True)

annotation_df_list = []

for column in clustering_column_lists:
    annotation_df_list.append(run_annotation(adata, SCSA=False, marker_lists=marker_lists, reference_obs=None, show_comparison=True,
                    clustering_column=column, rank_genes_column=rank_genes_column, 
                    ignore_overwrite=True, verbose=False, show_plots=True, show_ct_tables=True, 
                    celltype_column_name=celltype_column_name))
    
def show_umap_collection(annotation_df_list, clustering_column_lists):
    pattern = r'^([a-zA-Z]+)'
    methodes_dict = {}

    for column in clustering_column_lists:
        isMatch = re.match(pattern, column)
        if isMatch:
            methode = isMatch.group(1)
            if methode in methodes_dict:
                methodes_dict[methode] += 1
            else:
                methodes_dict[methode] = 1 
    
    for methode, num in methodes_dict.items():

        if num == 1:
            plt.imread(f"./figures/umap{methode}")
            plt.show()

        elif num == 2:
            fig, axes = plt.subplots(1, 2, figsize=(15,10))
            count = 0 
            for index, df in enumerate(annotation_df_list):
                if methode in str(df[1]):
                    axes[count].imshow(plt.imread(f"./figures/umap{df[2]}"))
                    axes[count].axis("off")
                    count += 1
            plt.tight_layout()
            plt.show()
        
        elif num > 2:
            row_ = math.ceil(num / 2)
            fig, axes = plt.subplots(row_, 2, figsize=(15,10))
            row = 0
            col = 0
            count = 0
            for index, df in enumerate(annotation_df_list):
                if methode in str(df[1]):
                    axes[row, col].imshow(plt.imread(f"./figures/umap{df[2]}"))
                    axes[row, col].axis("off")
                    count += 1
                    row = count // 2
                    col = count % 2
            plt.tight_layout()
            plt.show()

show_umap_collection(annotation_df_list, clustering_column_lists)

def create_compare_df(annotation_df_list):
    cell_types = list(set(value for df in annotation_df_list for value in df[1].iloc[:,0]))
    cell_types.append("ari_score")

    merge_df = pd.DataFrame(columns=clustering_column_lists, index=cell_types)
    merge_df = merge_df.fillna("")

    for data in annotation_df_list:
        col_name = data[0]
        df = data[1]
        for index, value in df.iloc[:,0].iteritems():
            if value in cell_types:
                if not merge_df.at[value, col_name]:
                    merge_df.at[value, col_name] = f"{index}"
                else:
                    merge_df.at[value, col_name] += f", {index}"

    for column in clustering_column_lists:
        merge_df.at["ari_score", column] = round(adata.uns["clusters"][column]["score"]["ari"], 5)

    return merge_df

merge_df = create_compare_df(annotation_df_list)
merge_df

def find_cluster(methode, cluster_num):
    for df in annotation_df_list:
        if methode == str(df[0]):
            clusters = df[3]
            display(clusters[f"Cluster {cluster_num}"])

find_cluster("lovain_1", 2)

best_cluter = str(adata.uns["best_cluster"])
best_cluter

reference_best = wrap.run_annotation(adata, SCSA=False, marker_lists=marker_lists, reference_obs="ontology label", show_comparison=False,
                    clustering_column=best_cluter, rank_genes_column=rank_genes_column, 
                    ignore_overwrite=True, verbose=False, show_plots=True, show_ct_tables=True, 
                    celltype_column_name=celltype_column_name)

if delete_lists:
    mr.delete_files(marker_lists)

