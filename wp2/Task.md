## Annotation of clusters using the central repository for management and application of marker gene lists (Jupyter Notebooks)

- The segment below has information about the functionality of the main components of the repository and the ultimate goal 
  in using the repository. This file contains a brief description of each component and its main operations. The idea is to represent the workflow
  in a step-by-step manner from the selection of the appropiate makers to the final step of evaluating the resulting annotation.

1. Marker Repository
2. Annotate
3. Evaluate

**Sidenote: Ubiquitousness index = gene expression markers for identification of biological cell types**

## 1. Marker Repository
- Repository was created to assing a biological meaning to these clusters by comparing features, such as gene 
  expression patterns, to known markers for specific cell types. Features guide the annotation process to identify
  the cluster as a cell type.
- Marker lists are used as references in the annotation process (+ UI to indicate abundance in each cell type), taken
  from PanglaoDB, CellMarker 2.0, or hand-curated.
- Challenge: selecting an appropiate source of marker lists
- Transfering genetic information to less annotated organisms using HomoloGene and Ensembl

- The single cell data is stored in a h5ad file format containing an AnnData object, implemented as Pantas DataFrame

### 1.1 Marker Lists:
- Marker lists represented as Pandas DataFrames, stored in YAML files as "key.yaml"
- YAML format as: Two Column Style, Score Style, UI Style
- "key.yaml" consists of two main sections: metadata and marker_list
- whitelist attribute needs to be ran first to avoid data inconsistencies
- Marker identifiers: Ensembl ID or GeneSymbol
- Management: structures organization, storage, and retrieval of biological markers for efficient use in research studies

### 1.1.1 Adding marker lists: step-by-step
- Submit marker list into the notebook 
- Validate input using whitelists
- Select an appropiate organism and marker type
- Marker genes that are on present in the organism´s whitelist are removed
- Additional IDs (Ensembl or Gene Symbol) are appended to the marker genes
- Integrate data with the existing metadata to avoid duplicates
- After validation, the marker list becomes part of the repository

### 1.1.2 Querying the repository: 
- Lists can be searched for keywords --> guided_search: when we click "continue searching" it keeps searching on the search performed before
- Filter lists by specific genes, regions, or other criteria

- User interacts with the search function and applies the appropiate filters
- It returns markers lists that are used for further customization
- User can modify the combined marker lists using specific functions 
- User can add a score to the lists

## 2. Annotate using Scanpy
- t1.rank_gene_groups: differential analysis to identify marker features, enriching biological interpretability

### 2.1 Application of the marker lists
2.1.1 Transfer markers
2.1.2 Cell type annotation
2.1.3 Identification of marker genes

### 2.1.1 Transfer markers: identify homologous genetic markers in a target organism based on the markers from the 
source organisms 
- homology function: transfer marker genes from source organisms to a specific target organism
1. Select target organism
2. Select source markers
3. Transfer markers: using BioMart and HomoloGene
4. Filter source markers
5. Transfer filtered markers
6. Results = Transfered marker list

### 2.2 Cell type annotation
- Marker weighing: weighs significance of each marker depending on its prevalence in different lists and 
  assigns them a score (UI) --> compare_marker_list + update_scores
- Creating marker lists: compiles existing marker lists based on user-defined criteria that can be integrated
  into subsequent analyses

### 2.3 Annotation tool: t1.ranked_genes_groups function (Scanpy function)
- The tool accepts marker lists 
- Identifies cell types in each cluster by calculating a ranking score for each potential cell type
--> marker genes, ranked scores, total number of available marker genes for each cell type, and UI

### 2.3.1 Annotating AnnData: annotating clustered h5ad files via the Annotation Jupyter Notebook (4 steps)
1. Information entry: define repository path, the h5ad file to annotate, organism of interest, and other variables
2. Preparing AnnData object: data loaded from the specified h5ad file, validate preliminary settings
3. Creating marker: create_marker_lists function curates subsets of existing markers
4. Cluster annotation: function annotates clusters using the defined marker lists and the internal annotation tool

- After annotation, UMAP plots are visualized to provide graphical representation of the newly annotated clusters
- A table is created ranking the cell types for each cluster, identifying the top-ranked cell for each cluster and 
  a range of potential alternative cell types

### 2.3.2 Identification of marker genes: export_markers_from_anndata function
- Function is designed to identify and export top marker genes from data stored in the AnnData objects
- It uses the Scanpy function to accerss the ranked genes and sort them by their associated scores
- Function isolates a set of highly informative genes that effectively characterize the identity of each cluster

## 3. Evaluate
- Compare results with the clusters available in the ATLAS --> test data clustering from ATLAS
- Compare results from different databases: are they subtypes? are they completely different?
- Self-consistency check: re-annotate an already annotated h5ad file using a marker list extracted from the rank genes scores
  in the same file
- Cross-reference validation using the Annotation Notebook
- Homology-based annotation








  




