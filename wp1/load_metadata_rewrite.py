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
    metadata_df = pd.read_csv(metadata_path, sep = seperator, header = 0)
    metadata_df.set_index('cellID', inplace=True)
    if columns_to_keep is not None:
        metadata_df = metadata_df[columns_to_keep]
    adata.obs = adata.obs.merge(metadata_df, left_index=True, right_index=True)
