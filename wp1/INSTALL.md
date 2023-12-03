# Vorbereitung für das Projekt
## Verbindung zur VM
Vorraussetzung: VPN-Zugriff auf 172.16.31.*
```
ssh -i <key> studX@172.16.31.Y
```

## Einrichtung der conda Umgebung
Vorrausetzung: conda und jupyter (sind auf der VM schon installiert)

_Von der Projektgruppe vorgegeben_
```
conda create -n datenanalyse episcanpy
conda activate datenanalyse
conda install ipykernel
python -m ipykernel install --user --name datenanalyse
```

## Weitere Dependencies
### Clustering Louvain und Leiden
```
conda install -c conda-forge python-igraph leidenalg louvain
```
- `louvain`: Der eigentliche Louvain-Algorithmus
- `leidenalg`: Der eigentliche Leiden-Algorithmus
- `python-igraph`: wird von scanpy für `flavor=vtraag` von lovain benötigt

### GeneScore
Ich habe das noch nicht zum Laufen bekommen, daher ist GeneScore nur vorläufig - snitz
```
conda install -c r r-irkernel
conda install bioconductor-genomicranges bioconductor-summarizedexperiment -y

# im Notenbook (in R)
devtools::install_github("caleblareau/BuenColors")
```
- `r-irkernel`: Um R Code in Jupyter auszuführen
- `bioconductor-genomicranges`: Effizientes ablegen von Gensequenzen und Metadaten zu Abschnitten
- `bioconductor-summarizedexperiment`: ähnlich wie AnnData oder Seurat's object
- `caleblareau/BuenColors`: Enthält Farbcodes, wie sie das Buenrostro Lab verwendet