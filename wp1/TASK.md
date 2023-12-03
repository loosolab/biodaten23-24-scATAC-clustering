# Aufgabe WP1 - Aufgabenstellung: Auswertung von ATAC-Seq Daten mittels Clustering-Algorithmen und Entwicklung der RAGI-Metrik

- [Aufgabe WP1 - Aufgabenstellung: Auswertung von ATAC-Seq Daten mittels Clustering-Algorithmen und Entwicklung der RAGI-Metrik](#aufgabe-wp1---aufgabenstellung-auswertung-von-atac-seq-daten-mittels-clustering-algorithmen-und-entwicklung-der-ragi-metrik)
  - [Vorgaben](#vorgaben)
    - [Arbeitsauftrag Gesamtprojekt](#arbeitsauftrag-gesamtprojekt)
    - [Arbeitspakete](#arbeitspakete)
      - [WP1](#wp1)
      - [WP2](#wp2)
      - [WP3](#wp3)
  - [Selbstgeschriebene Aufgabenstellung - WP1](#selbstgeschriebene-aufgabenstellung---wp1)
    - [Ziel](#ziel)
    - [Aufgaben](#aufgaben)
      - [1. Datenbeschaffung und -vorbereitung](#1-datenbeschaffung-und--vorbereitung)
      - [2. Dimensionalitätsreduktion und Einbettung](#2-dimensionalitätsreduktion-und-einbettung)
      - [3. Datenanalyse und Clustering](#3-datenanalyse-und-clustering)
      - [4. Entwicklung der RAGI-Metrik](#4-entwicklung-der-ragi-metrik)
      - [5. Beurteilung der Clusterqualität](#5-beurteilung-der-clusterqualität)
      - [6. Interaktion mit einer anderen Arbeitsgruppe](#6-interaktion-mit-einer-anderen-arbeitsgruppe)
    - [Anforderungen](#anforderungen)
    - [Ergebnis](#ergebnis)


## Vorgaben
### Arbeitsauftrag Gesamtprojekt
  <p align="center" style="font-size: 20px;">Investigate and evaluate <br>the effect of pattern finding and clustering <br>in the context of chromatin accessibility <br>at single cell resolution, <br>and <br>the annotation of clusters</p>

### Arbeitspakete
#### WP1
  - Dimred + Embedding
  - 2 Clustering methods
  - Gini Gene Index
  - Cluster Quality assessment
#### WP2
  - Export and UNPAST
  - Import
  - Scanpro
  - Bi-Cluster Quality assessment
#### WP3
  - Marker Repository
  - Annotate
  - Evaluate

## Selbstgeschriebene Aufgabenstellung - WP1
### Ziel
  Diese Aufgabe zielt darauf ab, ATAC-Seq Daten aus dem cAtlas zu analysieren. Dabei sollen verschiedene Clustering-Algorithmen angewendet und eine Metrik, genannt RAGI, zur Bewertung dieser Algorithmen verwendet werden.

### Aufgaben

#### 1. Datenbeschaffung und -vorbereitung
  - Importieren und vorbereiten der ATAC-Seq Daten aus dem cAtlas bzw. aus /mnt/workspace_stud/

#### 2. Dimensionalitätsreduktion und Einbettung
  - Einsatz von Dimensionalitätsreduktion und Einbettungstechniken, um die sehr dünnbesetzte (über 99% 0-Werte) Matix effektiv zu handhaben und für anschließende Analysen zugänglicher zu machen.

#### 3. Datenanalyse und Clustering
  - Anwendung verschiedener Clustering-Algorithmen, um die Daten in sinnvolle Gruppen zu teilen.
  - Am Beispiel von Louvain- und Leiden-Algorithmus.

#### 4. Entwicklung der RAGI-Metrik
  - Entwickeln Sie die RAGI-Metrik, die den Gini-Index über die reads von ausgewählten Markern berechnet.
  - Implementieren und testen Sie die Metrik, um die Effektivität der verschiedenen Clustering-Algorithmen zu bewerten.

#### 5. Beurteilung der Clusterqualität
  - Einsatz von Cluster-Qualitätsmetriken zur Bewertung der Effektivität der angewendeten Clustering-Methoden und -Parameter.

#### 6. Interaktion mit einer anderen Arbeitsgruppe
  - Eine andere Gruppe wird die für RAGI identifizierten Marker verwenden, um den Zelltyp zu bestimmen. Ihre Aufgabe ist es, eine Schnittstelle zu dieser Gruppe zu erstellen.
  - Die Schnittstelle sollte die Integration der von beiden Gruppen verwendeten Daten und Methoden ermöglichen.

### Anforderungen
  - Kommunikation: Eine klare und effektive Kommunikation mit der anderen Arbeitsgruppe ist entscheidend, um eine funktionierende Schnittstelle zu entwickeln.
  - Dokumentation: Alle Methoden und Ergebnisse sollten gründlich dokumentiert werden, um die Nachvollziehbarkeit und Reproduzierbarkeit der Arbeit zu gewährleisten.

### Ergebnis
  - Methodik und Ergebnisse der Datenclustering.
  - Entwicklung und Anwendung der RAGI-Metrik.
  - Details zur Schnittstelle mit der anderen Arbeitsgruppe und wie sie die Gesamtziele unterstützt.