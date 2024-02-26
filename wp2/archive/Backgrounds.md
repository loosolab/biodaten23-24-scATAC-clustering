# Single Cell Analysis Annotation
-	Computational methods such as PCA and UMAP are required to reduce dimensionality and clustering algorithms to identify groups of similar cells
-	Annotation through marker gene lists
-	Standardization is hard due to inconsistent formats to the limited availability of marker lists for organisms beyond mouse and human
-	Marker Repo: centralized repository for the management and application of marker lists  data uniformity + wide range of query functionalities (thanks to YAML and whitelists)
-	Features for adding, combining and customizing marker lists
-	YAML: human-readable data serialization language for writing config files
-	Homology-based approaches: BioMart and HomoloGene to facilitate the transfer of markers across species
-	Performance evaluation of Marker Repo: cross-reference validation and homology-based annotation to demonstrate robustness and reliability
-	Annotates cell clusters with high biological accuracy and integrates seamlessly into existing bioinformatics pipelines

# Introduction

## Single cell sequencing
-	Bulk RNA: produces an average gene expression profile from a pool of cells (signifies quantity not specificity)  method provides a general overview of gene activity, but is less informative for capturing the variation in gene expression across individual cells in a heterogeneous sample (not appropriate for cancer cells)
-	We need techniques capable of dissecting cellular complexity at higher resolution
-	Single cell RNA sequencing allows researchers to profiles transcriptomes of individual cells, providing unique insights into cell differentiation, function and disease states
-	example in tumors: single cell RNA-sequencing to identify rare but critical cell types and states responsible for treatment resistance
-	scRNA-seq + scATAC seq as a complementary technique
-	scRNA: provides information on mRNA expression levels within individual cells and scATAC-seq allows investigation of chromatin accessibility, providing insights into the regulation of gene expression –> to identify regulatory elements associated with malignant, stromal and immune cells
-	this combination enables the dissection of both genetic and epigenetic mechanisms at high resolution  however, sophisticated computational analysis is still necessary
-	single cell data has a dimensionality, so methods to extract the meaning biological insights are necessary  need for dimensionality reduction and clustering techniques

## Dimensionality reduction and clustering
-	high dimensionality can obscure underlying biological insights
-	starting point of the analysis represented as a count table (each row corresponds to a unique feature, such as a gene, and each column represents a single cell)
-	entries in the matrix quantify the level of accessibility for each feature in each cell
-	count table as an input for methods such as PCA to reduce the dimensionality of the data  by finding its principal components (linear combination of the original features that capture most of the variance)
-	pca identifies the eigenvalues and eigenvectors of the covariance matrix of the data and projects the original data onto the subspace spanned by these eigenvectors (linear dimensionality reduction, but not suitable for reducing data to two or three dimensions for visualization purposes)
-	limitation requires additional dimensionality reduction techniques such as UMAP 
-	UMAP: non-linear method that preserves both local and global structures within the data set  algorithm constructs a weighted graph for each data point and unifies the local graphs into a single cell topological representation 
-	Key parameters in UMAP: number of nearest neighbours and the minimum distance between points (preservation of local and global structure
-	Clustering is performed using algorithms such as Louvain or DBSCAN  annotation is based on these newly identified cell subgroups
-	Choice of clustering depends on the specific research question and data set at hand  quality should be assessed by different metrics and biologically validated
-	Annotation to give the clusters a biological context or meaning

## Cell type annotation
-	Features such as gene expression patterns are compared to known markers for specific cell types
-	High expression of a particular gene known to be a marker for a specific cell type would guide the annotation process to identify the cluster as that cell type
-	panglaoDB oder CellMarker provide comprehensive sets of known markers  contains data of mouse and human only (gap for significant model organisms)
-	single cell analysis in other species is challenging
-	HomoloGene and Enseml offer a potential solution for the problem
-	PanglaoDB includes a ubiquitousness index to indicate the abundance of each marker in different cell types
-	Researchers also include their knowledge and hand-curated lists
-	CHALLENGE: select an appropriate source for marker lists, as each database may be different sets of markers
-	HomoloGene and Enseml offer a potential solution for the problem of missing marker genes for less annotated organisms  facilitates the identification of homologous genes, useful for transferring genetic information from well-studied organisms to less-studied ones (but there is a risk of including irrelevant markers)
Objectives
-	Navigate complexities of marker list management and application, including the selection of appropriate marker sources, the inclusion of less-studies species, and issues of data standardization and integration
Methods 
-	Jupyter notebooks to serve as web-based interactive computational environments that eases the development and documentation of code

##Methods
-	Jupyter Notebooks as a interactive computational environment for the development and documentation of code
-	Single cell data in a h5ad file format
-	 h5ad: used to store large amounts of data in the form of multidimensional arrays
-	 h5ad are composed of a cell by feature matrix, metadata such as cluster labels for barcodes, and the embeddings (UMAP, PCA)
-	 metadata in csv format with barcode & metadata such as celltype, compartment, sample, condition, age, sex, etc.
-	H5ad contain AnnData with a .var table implemented as a Pandas DataFrame
-	Scanpy: tl.rank_gene_groups function  to identify marker features that are significantly up-or downregulated in individual cell clusters, enriching the biological interpretability of the dataset
-	Marker lists are represented as Pandas DataFrames and stored in YAML files
Marker list management
-	Structed organization, storage, and retrieval of biological marker for efficient use in research studies
Data organization and format
-	Keys.yaml: standardizes the structure and elements of all marker lists stored in the central repository  has two main sections: metadata and marker_list
-	1. Metadata contains fields: id, list_name, organism, etc. (basic details about the marker list + flexibility to include optional tags for annotating lists) and each field has a description and input requirements + Whitelist: to ensure that data values match a set of acceptable terms
-	2. Marker_list: structure and requirements for the actual marker data (name and markers)
-	 each marker list is stored in a separate YAML file, which contains the two primary sections: metadata and marker_list, focuses on the actual content (gene names or genomic regions)
Output and export options
-	YAML format enables one to export marker lists in specialized output formats that can be integrated into various bioinformatics pipelines
-	 Two Column Style: first column = marker, second column = info
-	 Score Style: Adds a score for each marker using a third column
-	 UI Style: adds or updates the score column with the ubiquitousness index provided by PanglaoDB
-	 identifiers of the markers: Ensembl ID or Gene Symbol
-	Marker lists are exported as Tab-Separated Values (TSV) files
Adding marker lists  step-by-step manner
-	1. Enter marker list into the submit lists notebook
-	2. Whitelists to validate the input and assist in selecting the appropriate organism and marker type  maintained in the metadata_whitelists_repository
-	3. Marker list is compared to the organism´s whitelist genes  marker genes not present in the organisms are removed and additional IDs are appended to the remaining marker genes
-	4. Integrate this data with existing metadata and transform it into a yaml file
-	5. List undergoes a unique ID check to ensure no duplicates exists
-	6. Once validated, the marker list becomes part of the repository
Querying the repository
-	Using the metadata, lists can be searched for keywords  query results are used for further customization
-	One can filter lists by specific genes, regions, or other criteria
-	After combining marker lists that meet the filter criteria, users can modify and customize the combined marker list using specific functions
-	End result: customized marker list that can be exported in a variety of formats + one can attach a quantitative score to each marker
Marker list application
-	1. Transfer markers: cross-species marker identification
-	2. Cell type annotation: focuses on the annotation of single cell data
-	3. Identification of marker genes: algorithms for  isolating relevant marker genes in AnnData objects
Transfer markers 
-	  identify genetic markers in a target organism base on marker from source organisms (extrapolating known markers) bioMart and HomoloGene
-	Steps performed by the homology function:
-	1. Select target organism: must be selected from a list of supported organisms
-	2. Select source markers: either provided or selected
-	3. Transfer markers: target organism and source markers (Biomart and HomoloGene)
-	4. Filter source markers: based on the number of target genes for each source gene
-	5. Transfer filtered markers: only source markers resulting in a target gene are re-transferred
-	6. Result: list of transferred marker genes in generated and returned
Cell type annotation: combination of algorithms and genetic markers to identify different cell types within complex data sets
-	Annotation AnnData: 1. Marker weighting (to assign importance to individual genetic markers based on frequency in different lists + UI), 2. Creating marker lists (compiles marker lists from existing repository based on user-defined criteria, user can only select existing lists from organisms) and 3. Annotation tool: tool design to apply the markers to clustered data sets (annotate AnnData using Scanpy, marker lists can be accepted in two formats  identifies cell types in each cluster by calculating a ranking score for each potential cell type (marker genes, their ranked scores, total number of available marker genes for each cell type, and the ubiquitousness index)
Annotating AnnData  Four primary steps: information entry, preparing the AnnData object, creating marker list, and cluster annotation
-	1. Information entry: set up basic settings for the annotation process  define repository path, the h5ad to annotate, the organism of interest, clustering column, gene column and search terms
-	2. Preparing the AnnData object: AnnData loaded from the specified h5ad file + gene ranking (optional)
-	3. Creating marker Lists from repository: assemble tailored lists of markers based on user-defined settings, curates subsets of existing markers
-	4. Cluster annotation: using the defined marker list and the internal annotation tool, annotations are added to the obs table, UMAP plots are visualized to provide graphical representation of each cluster + additional table to rank cell types for each cluster
Identification of marker genes
-	To identify and export the top marker genes from single cell data stored in an AnnData object using the Scanpy function to access ranked genes and sort their associated scores
-	Once sorted, the function isolates the ranked genes for each identified cell cluster
-	 re-annotation + cross-reference validation to validate the performance of the annotation tool using an external set of markers (tested for internal consistency)
Limitations:
-	Fields such as biology don´t use YAML format –> they would have to adapt
-	Whitelists require ongoing updates to include newly accepted terms to ensure its comprehensiveness
-	Contextual interpretation is also important for high specificity can produce annotations that are out of the expected biological context of the tissue being studied (doesn´t always match the tissue)
-	Database also lacks entries for some specialized cell types  performance vary depending on the complexity of the tissue under study
-	BioMart has a higher transferability  more homologous copies result in fewer unique genes


