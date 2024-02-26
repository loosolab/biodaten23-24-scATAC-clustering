# WP 2

## Introduction 

The main task of WP2 is to annotate the clusters obtained from WP1 using the central repository for the management and application of marker gene lists. The goal is to perform an appropriate computational analysis to extract meaningful biological insights from the single-cell data.

## Task

### Annotation of clusters using the central repository for management and application of marker gene lists (Jupyter Notebooks)

The segment below has information about the functionality of the main components of the repository and the ultimate goal 
  of using the repository. This file contains a brief description of each component and its main operations. The idea is to represent the workflow
  in a step-by-step manner from the selection of the appropriate makers to the final step of evaluating the resulting annotation.

1. Marker Repository
2. Annotate
3. Evaluate

#### 1. Marker Repository
- The Marker Repository was created to assign a biological meaning to these clusters by comparing features, such as chromatin accessibility, to known markers for specific cell types. 
- The markers lists used in the annotation process were taken
  from PanglaoDB, CellMarker 2.0, or hand-curated.
- Challenges:
- 1. Selecting an appropriate source of marker lists
- 2. Transferring genetic information to less annotated organisms using HomoloGene and Ensembl

#### 1.1 Marker Lists:
- Marker lists represented as Pandas DataFrames, stored in YAML files as "key.yaml"
- YAML format as Two Column Style --> The First column is the "Marker" (gene) and the second column is the  "Info" (cell type)
- "key.yaml" consists of two main sections: metadata and marker_list
- whitelist attribute needs to be run first to avoid data inconsistencies
- Marker identifiers: Ensembl ID or GeneSymbol

#### 1.1.1 Adding marker lists: step-by-step
- This section is explained in detail in the mySubmit.ipnyb notebook

#### 1.1.2 Querying the repository: 
- Lists can be searched for keywords --> guided_search: when we click "continue searching" it keeps searching on the search performed before
- Filter lists by specific genes, regions, or other criteria
- User interacts with the search function and applies the appropriate filters, allowing further customization

#### 1.1.3 Transfer markers 
- The user can transfer markers from a source organism to a target organism using two different homology-based approaches
- This section is explained in more detail in the homology.ipynb notebook

### 2. Annotate using Scanpy
- t1.rank_gene_groups: this function calculates a score for the potential cell types based on the marker lists it uses as input --> the scores are used to annotate the AnnData object
- - Creating marker lists: compiles existing marker lists based on user-defined criteria that can be integrated
  into subsequent analyses

### 2.1 Annotating AnnData: annotating clustered h5ad files via the Annotation Jupyter Notebook (4 steps)
1. Information entry: define the repository path, the h5ad file to annotate, the organism of interest, and other variables
2. Preparing AnnData object: data loaded from the specified h5ad file, validate preliminary settings
3. Creating marker: The create_marker_lists function curates subsets of existing markers
4. Cluster annotation: The function annotates clusters using the defined marker lists and the internal annotation tool

- After annotation, UMAP plots are visualized to provide a graphical representation of the newly annotated clusters
- A table is created ranking the cell types for each cluster, identifying the top-ranked cell for each cluster and 
  a range of potential alternative cell types


### 3. Evaluate
- Ontology labels were used as reference data to evaluate the accuracy of the annotation produced by the MarkerRepo
- Homology-based annotation: evaluate the effects on the annotation when using translated human markers vs. using human markers
- Automate the annotation process as much as possible (the functions are described in detail in codes section) 



## Contents
- [Backgrounds.md](archive/Backgrounds.md): The knowledge required to understand and use this project. 
- [Install.md](./Install.md): 
- [codes](./codes/):
  - [auto_annotation.py](./codes/auto_annotation.py):
  - [auto_annotation_notebook.ipynb](./codes/auto_annotation_notebook.ipynb):
  - [homology_notebook.ipynb](./codes/homology_notebook.ipynb):
  - [submit_new_marker_list_notebook.ipynb](./codes/submit_new_marker_list_notebook.ipynb):
- [data](./data/):
  - [DataSheet1.XLSX](./data/DataSheet1.XLSX)
  - [DataSheet2.XLSX](./data/DataSheet2.XLSX)
  - [2024_02_17](./data/2024_02_17/):

## Installation
To start the project, follow the instructions in [Install.md](./Install.md) to set up your development environment.

## References and Materials

The following is a list of scientific publications, technical notes, and a university thesis that were used as main sources of literature to research the most important concepts related to the project. The list also includes the paper from which the material with the zebrafish marker Excel files was taken.
We recommend reading the publications in case the person is not familiar with the subject.


1. Cell Type Annotation Strategies for Single Cell ATAC-Seq Data
   - Last modified March 30, 2022
   - https://www.10xgenomics.com/support/single-cell-atac/documentation/steps/sequencing/cell-type-annotation-strategies-for-single-cell-atac-seq-data
   - Explores three different strategies for annotating cell types in single-cell ATAC-seq data 

2. From reads to insight: a hitchhiker´s guide to ATAC-seq data analysis
   - Authors: Feng Yan, David R. Powell, David J. Curtis & Nicholas C. Wong
   - Published: 03 February 2020
   - https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-1929-3
   - Explains the concept of ATAC-seq and discusses the major steps in ATAC-seq analysis, such as quality check and alignment, peak calling, nucleosome position analysis, etc.

3. Supervised classification enables rapid annotation of cell atlases
   - Authors: Hannah A. Pliner, Jay Shendure & Cole Trapnell
   - Published: 09 September 2019
   - https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-1929-3
   - Rapid annotation of cell types in single-cell chromatin accessibility datasets using the tool "Garnett"

4. Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin, DNA-binding proteins and nucleosome position
   - Authors: Jason D. Buenrostro, Paul G. Giresi, Lisa C. Zaba, Howard Y. Chang, William J Greenleaf
   - Published: 06 October 2023
   - https://www.nature.com/articles/nmeth.2688
   - ATAC-seq as a method to identify regions of open chromatin, identify nucleosome-bound and nucleosome-free positions in regulatory regions

5. Characterization of the Zebrafish Cell Landscape at Single-Cell Resolution
   - Authors: Mengmeng Jiang, Yanyu Xiao, Weigao E, Lifeng Ma, Jingjing Wang, Haide Chen, Ce Gao, Yuan Liao, Qile Guo, Jinrong Peng, Xiaoping Han, Guoji Guo
   - Published: 01 October 2021
   - https://www.frontiersin.org/articles/10.3389/fcell.2021.743421/full
   - Zebrafish as an important organism to investigate gene regulation and cell lineage specification

6. Central Repository for Management and Application of Marker Gene Lists
   - Author: Micha Frederick Keßler
   - Presented: Dezember 2023
   - Management of the marker lists as a key step in the annotation of the cellular clusters

## Contacts 
For any queries or further discussion, feel free to contact:
- Huijie Li: huijie.li@bioinfsys.uni-giessen.de
- Marta Quintanilla: maria.marta.quintanilla.aguilar@bioinfsys-uni-giessen.de
