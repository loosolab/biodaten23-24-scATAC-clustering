# Preprocessing
- Die Daten sind schon vorverarbeitet, aber müssen noch:
    - gefiltert
        - highly variable genes only
        - Zellen mit sehr wenig / sehr vielen counts
        - Regionen mit sehr wenig / sehr vielen counts
        - jeweils der cut-off
    - normalisiert
        - exclude_highly_expressed
        - auf Anzahl Gene normalisieren, so dass Zellen mit vielen aktiven Genen nicht überräpresentiert sind
    - binärisiert
    - dimensionsreduziert
        - Wie viele PCA Dimensionen übernehmen wir?
        - Erste PCA Dim übernehmen?
        - SVD / TruncateSVD
        - andere DimRed techniken? LDA (latent Dirichlet allocation), multidimensional scaling (MDS), DiffusionMaps
- Muss gebatcht arbeiten können
- Ergebnis: PCA-reduzierte Matrix <cells>x50 Dimensionen pro Zelle (oder weniger)

# Clustering
- Algorithmen
    - kMeans: als Vergleich
    - hierarchical clustering: als Vergleich
    - Louvain: Erste Methode
    - Leiden
    - Self-organising maps?
    - UNPAST?
- Speichern des Clusterings in eine Spalte von obs
- jeweils eindeutige Namen aus preprocessing und clustering vergeben
    - evtl sogar im Namen das Datum, lfd. Nummer dazu einen Eintrag hier im git
    - Wir müssen clusterings reproduzieren können!
- bestes Clustering in adata.uns["best_clustering"] speichern
    -> für WP3

# Evaluation der Clusterings
- Finden von sehr variablen Regionen
    - am besten eindeutiger Peak für das Cluster oder eindeutiges Fehlen eines Peaks, also ein Ausreißer gegenüber den anderen Clustern
- Die Clusterings mit Markern mit RAGI bewerten. siehe ragi.py bzw chen-2019
- auch mit anderen Cluster evaluationen Vergleichen, zB aus dem episcan Tutorial

# Visualisierung
- UMAP oder tSNE, generell ist UMAP besser
- Reads/counts über das gesamte Genom visualisieren, wie in den Folien von Mario