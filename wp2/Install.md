# Files (private)
- Repository for Annotate by marker and features
  - `/mnt/workspace_stud/allstud/wp2/annotate_by_marker_and_features-sort`
- Necessary documents Metadata whitelists for running notebook
  - `metadata_whitelists`
  - `homologene.data` for homology
- Testdaten path: 
  - `/mnt/workspace_stud/allstud/wp1/data/2024_01_28`
  - `/mnt/workspace_stud/allstud/wp1/data/2024_02_17`

---
# Upload or download files/folder to/from VM

```scp [-r] path1 path2```

---
# Install the Conda environment and MarkerRepo Package
1. Open your terminal
2. Navigate to the  `environment.yaml` file in the repository

    (should be at folder `.../annotate_by_marker_and_features-sort/`)
3. Run one of the following commands, it creates a new Conda enviroment named `marker-repo`:
   - `conda env create -f environment.yaml` or 
   - `mamba env create -f environment.yaml` 
4. activate the Conda environment `conda activate marker-repo`
5. add the environment to Jupyter as a Kernel
   - `python -m ipykernel install --user --name=marker-repo --display-name 'marker_env'`
   - `marker_env` should appear as an available option when choosing a Kernel in Jupyter (If `marker_env` not appear, use `sudo reboot`)
6. install MarkerRepo Package `pip install .`
7. deactivate the Conda environment `conda deactivate marker-repo`

---
# Library
1. openpyxl: if you want run `submit_new_marker_list_notebook.ipynb`, you will need install this library first.