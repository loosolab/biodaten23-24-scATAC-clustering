# Files (private)
- Repository for Annotate by marker and features
- Necessary documents Metadata whitelists for running notebook 
  
  (This folder need to be stored in the repository folder: under `annotate_by_marker_and_features/`)

- Testdaten path: `/mnt/workspace_stud/mkessle/test_data/hs_thymus.h5ad`
  
  (more informations about daten can be find at `/mnt/workspace_stud/mkessle/test_data/hs_thymus.pdf`)

---
# upload folder to VM

```scp -r local/path vm/path```

---
# Install the Conda environment and MarkerRepo Package
1. Open your terminal
2. Navigate to the  `environment.yaml` file in the repository
    (should be at folder `.../annotate_by_marker_and_features-main/`)
3. Run one of the following commands, it creates a new Conda enviroment named `marker-repo`:
  - ```conda env create -f environment.yaml``` or 
  - ```mamba env create -f environment.yaml``` *not working for Huijie Li*
4. activate the Conda environment ```conda activate marker-repo```
5. add the environment to Jupyter as a Kernel, ```python -m ipykernel install --user --name=marker-repo --display-name 'marker_env'```, `marker_env` should appear as an available option when choosing a Kernel in Jupyter (If `marker_env` not appear, use `sudo reboot`)
6. install MarkerRepo Package ```pip install .```
7. deactivate the Conda environment ```conda deactivate marker-repo```
---
