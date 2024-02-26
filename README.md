# biodaten23-24-scATAC-clustering

## Allgemeine Aufgabenstellung
  <p align="center" style="font-size: 20px;">
    Investigate and evaluate <br>
    the effect of pattern finding and clustering <br>
    in the context of chromatin accessibility <br>
    at single cell resolution, <br>
    and <br>
    the annotation of clusters
  </p>

  Good cooperation within the groups, but also between the groups, is important.

<p align="center">
  <img src="images/wp_distribution.png" alt="drawing" width="1000"/>
  Since only a limited number of students applied for this course, WP2 is cancelled and WP3 is now WP2
</p>

## Arbeitsgruppen
This project focuses on analysing scATAC-Seq data using clustering algorithms and developing the Residual Average Gini Index (RAGI) metric. The aim is to explore patterns in chromatin accessibility at the single-cell level and to determine clusters of different cell types, that can then be annotated. The cell annotation is made possible by using marker gene lists, which are stored in the Marker Repository. This project also aimed to automate the annotation process as much as possible and to evaluate the quality of the annotations using an ontology label as a reference.

### [WP1](wp1/)
- preprocessing
- dimension reduction
- clustering
- export for WP2

### [WP2](wp2/)
- create a marker list
- transfer markers from a source organism using the homology function
- annotate the cluster based on the marker list used as input
- automate the annotation process
- evaluate the quality of the annotation
