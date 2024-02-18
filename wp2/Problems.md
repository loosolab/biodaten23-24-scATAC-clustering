## week 1: 22.11 - 29.11 
- install env and run examples
- reading Thesis 
- examples from `notebook` 

### Problems
- Befehl-`scp` funktioniert nicht bei Marta, es gibt immer `lost connection`.
- VM-Berechtigungen: Wir können nicht auf Dateien in fremden Ordnern zugreifen.
- Einige Dateien von Ordnern `notebook` laufen immer noch mit Fehlern.
  - `homology`, `submit_lists`, `guided_annotation`
  - alle Dateien von Ordnern `examples`

## week 2: 29.11 - 06.12
- finish examples learnning --> Infrastructure is currently working on Marta´s laptop
- ´homology´, ´submit_lists´ and ´guided_annotation´ are working correctly (all functions are working correctly)
- testing clusters from wp1
- ´homology´: BioMart works better than HomoloGene (higher percentage of transferable genes)

### Problems
- Key error while creating the gene_ranking: error while trying to set the gene index
- Program keeps reading the old index: program might be reading the a.vars(?) 
- Decide which annotation is better? --> Semicolon loswerden (es sind viele Gene auf einmal bei dem GeneID)
- Redundante Gene loswerden?
- Format der Annotation der Gene verbessern
- Es gibt viele Gene mit der gleichen Annotation und die gleiche Region mit vielen Annotationen
- Semikolons loswerden?
- GeneRanking nicht so wichtig für die Annotation, man soll mehr auf die endliche Annotation achten!
- rüberkegel, raussetzten und zusammenfassen! wie löst man das mit den Genen?
- Problem: Mapping auf Gene, die nicht die Topgenen sind
- Stefan: Score berechnen --> welches Gen passt am Ende besser in der Region(?)
- Peaks, die unique sind, haben ein besseren Informationsgehalt --> nur die besondere Peaks nehmen?
- maxplot funktion bei der GeneRanking verbessern 
