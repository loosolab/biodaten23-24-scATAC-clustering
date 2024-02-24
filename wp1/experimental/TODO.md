# Waiting

# Doing
- Testweise Clustering ausprobieren (Leonard)
  - Testweise das gefundenene Cluster evaluieren
    - Zelltypen annotieren
    - ARI auprobieren
- RAGI über alle Gene (Features) ausführen
  - Den Code von chen-2019 ausprobieren, erstmal ohne Housekeeping Gene


# TODO
## Projektdoku und Allgemeines
    - evtl eine USAGE.md, wie man die Notebooks aufruft
    - METHODS.md aufbereiten
    - Übersichtsgrafik über unsere Methode erstellen

## RAGI (Stefan)
    - RAGI verstehen und implementieren

## Clusterevaluation (Leonard)
    - andere ClusterMetriken berechnen (siehe episcanpy Tutorial) AMI, ARI, HS 
    - Annotationen von cAtlas anschauen, dort sollte es schon Zelltypannotationen geben, als Abgleich zu unseren Clustern
      - catlas metadaten laden (epi.pp.load_metadata) Cell_metadata.tsv.gz von http://catlas.org/catlas_downloads/humantissues/
    - Clustermetadaten in adata.uns["clusters"] speichern
      - Metadatenformat festlegen

# ATAC-Seq Daten besser verstehen
    - die anderen Dateien unter /mnt auf der VM anschauen
      - /mnt/workspace_stud/catlas_ref/cellXgene und cellXcCRE und evtl auch frag

## Für die Schnittstelle, marker-repo anschauen und verstehen
    - annotate_by_marker_and_feature.zip anschauen

# Optional
- Andere Paper von chen et al. anschauen
  - Und Buenrostro

# Done
- TASK / Aufgabenstellung formulieren
- Ordner im Projekt-git anlegen für wp1
    - 23.11.2023, Stefan: erstmal nur PR angelegt, wir haben noch kein commit Recht, ich habe Mario geschrieben, Mario hat den PR gemerged
- TASK.md nochmal überarbeiten
- Vorgehen/Projektmanagement festlegen: Welche Arbeitspakete haben wir? In welcher Reihenfolge gehen wir vor?, In welche Datei schreibe ich das? -> TASK.md
- Kurze Präsentation für nächste Woche
  - odt oder pdf? -> Markdown
  - was stellen wir vor? -> Aufgabenstellung/Aufgabengliederung vorstellen
  - unser aktuellen Notebooks vorstellen -> Filtern und Clustern
- Die abnormale Zelle von Esophagus in Slack posten (Stefan)
  - Habe Jan gefragt, was er davon hält, warte noch auf Antwort
  - können wir rausfiltern
- Die bisherigen Analysen in einem Notebook aufbereiten (Stefan)
  - Habe das auch mit an Jan geschickt
- git Zugang verproben
  - wir warten noch auf Mario
- Wie/wo können wir Zwischenergebnisse sichern? zB die PCA
  - in /mnt/workspace_stud/allstud
- Zu den Regionen die naheliegenden Gene o.ä. annotieren
    - episcanpy find_genes (siehe Tutorial von episcanpy) ausprobieren

# Didn't do
- Screenshots vom 22.11. in images/ und LOG.md einfügen
    - Die Screenshots kommen alle aus der Präsentation vom Anfang, die im Slack hinterlegt ist