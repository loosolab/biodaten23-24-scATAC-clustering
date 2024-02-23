import anndata as ad
import pandas as pd
import subprocess
import os.path
from collections import defaultdict
from scipy.sparse import issparse, csr_matrix, csc_matrix, hstack
import numpy as np

def gini_coefficient(x):
    """Compute Gini coefficient of array of values"""
    diffsum = 0
    for i, xi in enumerate(x[:-1], 1):
        diffsum += np.sum(np.abs(xi - x[i:]))
    return diffsum / (len(x)**2 * np.mean(x))


def ragi(adata, cluster_tag):
    """ Compute ragi and save _gini_scores per region to adata.var"""
    if cluster_tag not in adata.obs:
        raise ValueError(f"Cluster column '{cluster_tag}' not found in adata.obs.")

    gini_tag = cluster_tag + "_gini_scores"
        
    if gini_tag in adata.var:
        return adata.var[gini_tag].mean()
        
    # Convert to CSC format for efficient column-wise operations
    data = adata.X.copy()
    data[adata.X != 0] = 1 # binarize
    data_csc = csc_matrix(data)

    # Get cluster labels
    clusters = adata.obs[cluster_tag].values
    unique_clusters = np.unique(clusters)

    # Initialize a DataFrame to hold the results
    sum_per_cluster = pd.DataFrame(index=adata.var_names, columns=unique_clusters)

    # Compute sums for each cluster
    for cluster in unique_clusters:
        # Get indices of cells in the cluster
        cell_indices = np.flatnonzero(clusters == cluster)

        # Extract the submatrix for the cluster and compute the sum
        cluster_submatrix = data_csc[cell_indices, :]
        cluster_sum = cluster_submatrix.sum(axis=0).A.squeeze()
        sum_per_cluster[cluster] = cluster_sum
    
    # calculate number of cells in each region
    region_sum = sum_per_cluster.sum(axis=1)
    
    # remove 0 values to handle div/0 (NaN)
    sum_per_cluster = sum_per_cluster[region_sum != 0]
    region_sum = region_sum[region_sum != 0]

    proportion_per_cluster = sum_per_cluster.div(region_sum, axis=0)

    # step that takes the longest
    gini_scores = proportion_per_cluster.apply(gini_coefficient, axis=1, raw=True)
    
    # save back to adata
    adata.var[gini_tag] = gini_scores
    
    return gini_scores.mean()


def load_metadata(adata, metadata_path, seperator='\t', columns_to_keep=None):
    '''
    Loads in cell metadata in adata.obs of a given adata object.

    Metadata file is expected to contain the cell identifiers "cellID"
    These identifiers won't be written to the adata object, but are needed for matching the right metadata to the cells.
    Example data: CATlas metadata
    http://catlas.org/catlas_downloads/humantissues/Cell_metadata.tsv.gz

    Args:
        adata (adata object)   : adata object to be annotated
        metadata_path (string) : path to the metadata file
        seperator (string)     : [optional] seperator in the metadata file, default: tab
        columns_to_keep (list) : [optional] list of strings, containing the column names to be written in the adata object. If not given      writes all columns to file.

        ---
    '''
    metadata_df = pd.read_csv(metadata_path, sep = seperator, header = 0)
    metadata_df.set_index('cellID', inplace=True)
    if columns_to_keep is not None:
        metadata_df = metadata_df[columns_to_keep]
    adata.obs = adata.obs.merge(metadata_df, left_index=True, right_index=True)


def download(path, url, zipped=True):
    """" lazily downloads and optionally extracts file if it does not exist"""
    if os.path.exists(path):
        print(f"{path} already exists.")
    else:
        print(f"Downloading {os.path.basename(path)}...")
        
        if zipped:
            subprocess.Popen(f"wget -qO- {url} | gunzip > {path}", shell=True)
        else:
            subprocess.Popen(f"wget -qO- {url} > {path}", shell=True)
            
        print(f"Download and extraction of {os.path.basename(path)} complete.")
