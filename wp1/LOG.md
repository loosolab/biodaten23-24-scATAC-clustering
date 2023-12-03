# Sa 02.12.2023
Meeting zwischen wp1 und wp2
TODOs:
- Git umziehen
- Test clustering rübergeben
  -> nächste Woche
- Notebook / Daten von wp2 anschauen
- data ordner in allstud/wp1 -> was kommt da rein?
  -> gene metadaten dort hinlegen
- ein main adata hd5a mit reproduktionsskript/notebook im git
  -> Wie nennen wir das?
  -> Wie bauen wir das Skript/Notebook auf?
  %run von der cli?
- einfachen RAGI implementieren
- funktion zur Annotation von Zellen an wp2 geben
- Features auf Gene umschlüsseln vor der PCA?
  -> Wie viel up/downstream? -> Möglichst alle Regionen mitnehmen, möglichst wenig überlappungen
  -> Genes, Transcript oder CDS aus gtf?

# Mi 29.11.2023 Abend
- Stefan: Ich habe einen Bug in episcanpy find_genes gefunden

# Mi 29.11.2023
Meeting
- git Zugriff? Oder sollen wir immer PRs nutzen?
  - Wurde angelegt
- Können wir davon ausgehen, dass wir Zelltypannotationen in den Daten vorliegen haben für ARI, HS, AMI
  - Sind da, aber ist nicht Goldstandard
- Wo können wir Datenablegen für die Übergabe von WP1 an WP3 /mnt/workspace_stud/???
  - Wo sollen wir unsere eigenen Gen- oder Zell-Annotationen ablegen? 
  - /mnt/workspace_stud/allstud/wp1
- Wie sollen wir Markergene bestimmen?
  -> Erstmal alle
- Ist die Gen-Annotation wie wir sie haben ok?
  - hg19 alignment, gencode.v19.annotation.gtf
  - nur HAVANA
  - upstream 2000
  - no downstream -> auch 2000
  - gerne mehr nehmen
  - Evtl noch eigener Annotationsalgo von Jan
  - TODO Auf hg38 wechseln
  - nur eine Annotation aus dem gtf nehmen, aktuell HAVANA, aber auch ENSEMBL probieren. Nicht mischen
- Aus dem Termin mitgenommen:
  - TODO Namenskonvention für Cluster festlegen
  - Datenqualitätsanalyse auf versch. Geweben ausprobieren
  - UROPA für die Annotation ausprobieren


# So 26.11.2023
- snitz: Ich wollte GeneScore (R code aus dem chen2019 Anhang) ausprobieren, habe aber weder alle Dependencies installiert bekommen, noch verstanden, auf welchen Daten dieser arbeitet.
- snitz: Ich habe die Gen Annotationen wie im episcan Tutorial ausprobiert und dann einige Plots erstellt um zu schauen, ob die Annotationen gut aussehen

# Sa. 25.11.2023
- Treffen mit WP3 über Zoom
- Notizen
    - Was ist für Mittwoch wichtig?
        - Eigene Aufgabenstellung, Arbeitspakete, Vorgehen
        - bisherige Ergebnisse, aus den Notebooks
    - Wie präsentieren wir das?
        - Als Markdown, bzw die Notebooks per Screenshare
    - Hat jemand Zugriff auf git?
        - Haben die anderen auch nicht
    - Wo habt ihr noch Probleme?
        - Schwierigkeiten mit ssh/scp und conda

# Do. 23.11.2023
- Wir haben dieses Repo angelegt
- Leonard versucht das Louvain Clustering auf den Esophagus Daten zum laufen zu bekommen
- Stefan hat die data_quality.ipynb erstellt und an Jan geschickt
- Wir haben die Aufgabenstellung in TASK.md beschrieben

# Mi. 22.11.2023 - Wochentermin mit Mario und Jan
- Fragen für den Termin:

    Wie preprocessing?
    Woher kommen die Daten, woher kommen die Genabschnitte? Immer 400 Groß
    Wie Peak Calling? Können wir den Code dafür bekommen

    Peak verhalten / Quality Control
    Viele Peaks > 1, ~50% >= 2, bis zu 77

    Tote Gene, ohne Peaks, können wir diese rausfiltern?

    Zelle mit sehr vielen Peaks, können wir diese rausfiltern?

- Wir haben im Vorfeld die Gruppen eingeteilt
- Wir bearbeiten WP1, das Clustering der ATAC-Seq Daten und die Bewertung der Cluster mit einer eigenen Metrik
- Mario hat uns den RAGI vorgestellt, dieser nutzt Gini intern
- Wir haben Aufgabe bekommen:
    - unser Arbeitspaket in eigenen Worten zu formulieren
    - eine Schnittstelle zwischen unseren Clusterings und dem nachfolgenden Marker Team (WP3) festzulegen
        - Wir sollen die Clusterings als Layer in obs ablegen, jedes Clustering unter einem eigenen Namen
        - Wie legen wir in dem AnnData Objekt fest, was das beste Clustering ist?


# Davor
- Wir haben festegestellt, dass die Daten noch nicht komplett sauber sind
    - In dem Beispieldatensatz Esophagus gibt es eine Zelle mit sehr vielen counts
      und viele Gene ganz ohne counts -> Damit wenden wir uns nochmal an Jan