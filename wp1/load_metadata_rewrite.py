# Code from epiScanpy/episcanpy/preprocessing/_metadata.py

import anndata as ad
import pandas as pd

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
    #columns_to_keep = ['logUMI', 'tsse', 'cell type', 'Life stage']
    #columns_to_keep = ['cell type']

    metadata_f = pd.read_csv(metadata_path, sep = seperator, header = 0)

    # column names cause issues later on if they contain a SPACE
    # search for tags with space and replace it with a _
    # Example: ['cellID', 'logUMI', 'tsse', 'tissue', 'cell type', 'Life stage']
    metadata_f.columns = [column.replace(' ', '_') for column in metadata_f.columns]

    adata_index = adata.obs.index

    # check if columns_to_keep is not empty
    if columns_to_keep:
        # if not empty: Only select the specified metadata columns for the new dataframe
        
        # Get the cell_ids / barcodes from the first column, needed for assiging the right data to the right cells
        cell_ids = [metadata_f.columns[0]]
        columns_to_keep = cell_ids + columns_to_keep

        columns_to_keep = [column.replace(' ', '_') for column in columns_to_keep] # Ajust column names to not include spaces
        metadata_list = [tuple(getattr(row, column) for column in columns_to_keep) for row in metadata_f.itertuples(index=False)]
        df = pd.DataFrame('NA', index=adata_index, columns=columns_to_keep[1:])
    else:
        # if empty: add all possible metadata columns to the dataframe
        metadata_list = [tuple(row) for row in metadata_f.itertuples(index=False)]
        df = pd.DataFrame('NA', index=adata_index, columns=metadata_f.columns)

    # write the metadata values into the freshly created dataframe
    for metadata_content_row in metadata_list:
        df.loc[metadata_content_row[0], :] =  metadata_content_row[1:]
    
    #print(f"new df:\t{df}")

    for col in df.columns:
        adata.obs[col] = df[col]