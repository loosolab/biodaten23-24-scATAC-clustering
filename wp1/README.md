# WP1 - Preprocessing and Clustering

## Introduction
This project focuses on analysing scATAC-Seq data using clustering algorithms and developing the Residual Average Gini Index (RAGI) metric. The aim is to explore patterns in chromatin accessibility at the single cell level and to determine clusters of different cell types, that can then be annotated by the second work package.  
For the evaluation of the created clusters, we make use of the aforementioned RAGI-Score, alongside the popular ARI-score if reference data is available.  

The pipeline introduced in this repository can be summed up over the following steps:  
1. Setup & Reading in files
2. Filtering
3. Load cell metadata (ontology label)
4. Annotate regions with uropa
5. Dimension reduction
6. Clustering
7. Export

## Content of the Repository
  - `clustering.ipynb`  : Jupyter Notebook containing the pipeline.
  - `utils.py`          : Utility functions that are used in the pipeline.
  - `experimental`      : Uncommented documents and code history of the project. 

## Requirments & Installation

### Setup of the conda environment

```
conda create -n datenanalyse episcanpy
conda activate datenanalyse
conda install ipykernel
python -m ipykernel install --user --name datenanalyse
```

### Other dependencies

Clustering Louvain and Leiden:
```
conda install -c conda-forge python-igraph leidenalg louvain
```
- `louvain`: The louvain algorithm
- `leidenalg`: The leiden algorithm
- `python-igraph`: is used by scanpy for `flavor=vtraag` of louvain
<br/> <br/> 

Uropa:
```
conda install uropa
```

## Running the Notebook

To run the pipeline in `clustering.ipynb` it's important to set the "Project setup variables", which are as followed:  

- data_folder, project folder where all files and folders will be created.

- Input paths: 
    - input_folder, where the target h5ad scATAC-Seq files are located.
    - input_filename, the name of the h5ad file to be read and analysed.

- Output paths:
    - out_filename, the name of the export h5ad file to be created.
    - out_file, the full path of the file that will be written to.

- uropa path, the path pointing to the uropa binary.

### Important variables

The section dedicated for important variables that were tweaked most during the development of the pipeline.

## File organization
Only files and folders in the data_folder will be read and written to, except for the input h5ad file.
In the data_folder are the following files:

- catlas_metadata/Cell_metadata.tsv : one line per cell, only the cell_type column is relevant for this notebook.
- catlas_metadata/Cell_ontology.tsv : one line per cell_type, has ontology id and label
- gencode.v38.annotation.gtf : genomic annotation for the human reference genome hg38
- YYYY_MM_DD/output.h5ad : extra folder to group different runs of the notebook by date of execution.