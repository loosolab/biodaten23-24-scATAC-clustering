
TODO
Index auf Gene wechseln erst nach Clustering
  -> Trotzdem vorher probieren

Tuning mit einem Metaoptimizer ausprobieren
Tuning auf mehrere Geweben testen

cell type Metadaten nach Ontologie zusammenfassen
  -> wie weit, etwa 8 Cluster

Gene als Index
  - unique intergenic -> intergenic_id
  - Regionen mit mehreren Genannotationen aufteilen
    -> alle Peaks auf ein Gen, oder auf alle?
  - Gene mit mehreren Regionen
    -> 1. alle Peaks aus den Regionen übernehmen
    -> 2. Peaks bewerten und nur Peaks mit hohem Informationsgehalt übernehmen
  Ziel Genannotationen im Index

my_first_cluster
cluster_gene_annotation
- clusterings
  - louvain mit resolution 0.6
  - leiden mit resolution 0.5
  - kmeans 
- metadaten mit in adata.uns schreiben
- verbesserte gene_annotation
  - region bekommt nur nähestes Gen
  - Gen bekommt erstmal alle Regionen, später nach Informationsgehalt
- pfad auf /data/release ändern

prio Ragi / cell ontology

sqlite statt uropa
pca quer um dimensionen manuell zu reduzieren
warum laufen die verschiedenen Zelltypen in der UMap in der Mitte alle zusammen? welche Gene sind in diesen mittigen Zellen stärker ausgeprägt? Kann man das als Faktor nehmen um die Varianz vor der PCA zu reduzieren? Quasi Anti Marker?

uropa gegen my_find_genes abgleichen
den region-merge verbessern

