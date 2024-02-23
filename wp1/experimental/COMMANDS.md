# conda
## Uninstall package
```
conda remove <package>
```

## Reset conda env
```
conda remove -n datenanalyse --all
```
Then redo the steps from INSTALL.md

## List conda envs
```
conda env list
```
oder
```
conda info --envs
```

## List installed conda packages
```
conda list
```

# scp
## Einen Ordner zur VM kopieren
Kopiert den in dein Home-Verzeichnis auf der VM
```
scp -r <folder on local machine> <user>@<host>:~/
```