# WP1 - Preprocessing and Clustering

Quick recap of whole project

- What part does wp1 play in the whole project
wp1 takes data from catlas and preprocesses it, reduces dimensions and creates and evaluates clusters on the cells. The data is then provided to wp2 with a known layout.

What did we do?

- What can be found here?
In the clustering.ipynb is our pipeline that reads catlas data, processes it and stores it for wp2 to access

In detail:
1. Read
2. Filter
3. Load cell metadata (ontology label)
4. Annotate regions with uropa
5. Dimension reduction
6. Clustering
7. Export


- How can I run this notebook?
- Install and execute

What did we find?


catlas
http://catlas.org/catlas_downloads/humantissues/Cell_by_cCRE/matrix.h5ad
The data we use is stored at /mnt/workspace_stud/mbentse/catlas_objects
And the whole matrix is split into tissue specific subsets.9+++9