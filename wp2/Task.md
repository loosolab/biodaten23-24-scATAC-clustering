## Annotation of clusters using the central repository for management and application of marker gene lists (Jupyter Notebooks)

- The segment below has information about the functionality of the main components of the repository and the ultimate goal 
  of using the repository. This file contains a brief description of each component and its main operations. The idea is to represent the workflow
  in a step-by-step manner from the selection of the appropriate makers to the final step of evaluating the resulting annotation.

1. Marker Repository
2. Annotate
3. Evaluate

## 1. Marker Repository
- Repository was created to assign a biological meaning to these clusters by comparing features, such as chromatin accessibility, to known markers for specific cell types. The annotation of the cluster was made possible by using marker genes.
- The markers lists used in the annotation process were taken
  from PanglaoDB, CellMarker 2.0, or hand-curated.
- Challenges:
- 1. Selecting an appropriate source of marker lists
- 2. Transferring genetic information to less annotated organisms using HomoloGene and Ensembl

- The single-cell data is stored in a h5ad file format containing an AnnData object, implemented as a pandas DataFrame

### 1.1 Marker Lists:
- Marker lists represented as Pandas DataFrames, stored in YAML files as "key.yaml"
- YAML format as Two Column Style --> The First column is the "Marker" (gene) and the second column is the  "Info" (cell type)
- "key.yaml" consists of two main sections: metadata and marker_list
- whitelist attribute needs to be run first to avoid data inconsistencies
- Marker identifiers: Ensembl ID or GeneSymbol

### 1.1.1 Adding marker lists: step-by-step
- This section is explained in detail in the mySubmit.ipnyb notebook

### 1.1.2 Querying the repository: 
- Lists can be searched for keywords --> guided_search: when we click "continue searching" it keeps searching on the search performed before
- Filter lists by specific genes, regions, or other criteria
- User interacts with the search function and applies the appropriate filters, allowing further customization

### 1.1.3 Transfer markers 
- The user can transfer markers from a source organism to a target organism using two different homology-based approaches
- This section is explained in more detail in the homology.ipynb notebook

## 2. Annotate using Scanpy
- t1.rank_gene_groups: this function calculates a score for the potential cell types based on the marker lists it uses as input --> the scores are used to annotate the AnnData object
- - Creating marker lists: compiles existing marker lists based on user-defined criteria that can be integrated
  into subsequent analyses

### 2.1 Annotating AnnData: annotating clustered h5ad files via the Annotation Jupyter Notebook (4 steps)
1. Information entry: define repository path, the h5ad file to annotate, the organism of interest, and other variables
2. Preparing AnnData object: data loaded from the specified h5ad file, validate preliminary settings
3. Creating marker: The create_marker_lists function curates subsets of existing markers
4. Cluster annotation: The function annotates clusters using the defined marker lists and the internal annotation tool

- After annotation, UMAP plots are visualized to provide a graphical representation of the newly annotated clusters
- A table is created ranking the cell types for each cluster, identifying the top-ranked cell for each cluster and 
  a range of potential alternative cell types


## 3. Evaluate
- Ontology labels were used as reference data to evaluate the accuracy of the annotation produced by the MarkerRepo
- Homology-based annotation: Evaluate the effects on the annotation when using translated human markers vs. using human markers








  




