# Best current cluster [Last updated: 13.12.2023]

## Preprocessing steps and order
- Tissue: Esophagus muscularis
- Metrics (calculate_qc_metrics)
- Normalize (normalize_total)
- log1p
- pca (PCA of n compontents, or subsetting a higher PCA from 0-n achive virually the same ARI)
    - n components
    - use_highly_variable=False 
- Neighbors (sc.pp.neighbors)
    - n_neighbors = 15
    - method = 'umap'
    - metric = 'euclidean'
- umap
    - spread = 2.5
    - min_dist = 0.1


## Louvain
- res : 0.3
- pca components : 10   
- ari : 0.8064244437875907

## Leiden
- res : 0.2
- pca components : 16
- ari : 0.800098609593834

## kmeans
- k clusters : 7
- pca components : 47
- ari : 0.5665200638988788