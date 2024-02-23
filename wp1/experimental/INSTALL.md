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
conda install -c conda-forge python-igraph leidenalg louvain requests
```
- `louvain`: Der eigentliche Louvain-Algorithmus
- `leidenalg`: Der eigentliche Leiden-Algorithmus
- `python-igraph`: wird von scanpy für `flavor=vtraag` von lovain benötigt
- `requests`: For downloading data from the OLS Ontology Service