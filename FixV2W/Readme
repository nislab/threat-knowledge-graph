## Table of Contents

- [File Structure](#file-structure)
- [How to run tutorials on the NERC](#how-to-run-tutorials-on-the-nerc)
- [How to run tutorials in SCC using GPU](#how-to-run-tutorials-in-scc-using-gpu)
- [How to run the pipeline on the NERC](#how-to-run-the-pipeline-on-the-nerc)
- [Web App code repo information](#fixv2w-webapp)
- [TODO](#todo)

# File structure
This is the same structure as the original repository with some slight changes as indicated below.
```
```text
.
├── threat_kg/ # ID conversions required for training and then evaluating the model
│   ├── id_conversions/
│   ├── id_conversions_complex/
│   ├── id_conversions_distmult/
│   ├── id_conversions_exp/
│   ├── id_conversions_other/
│   ├── id_conversions_other1/
│   ├── id_conversions_other2/
│   ├── id_conversions_other3/
│   ├── id_conversions_retrain_0/
│   ├── id_conversions_retrain_0_cwa/
│   ├── id_conversions_retrain_1/
│   ├── id_conversions_retrain_2/
│   ├── id_conversions_retrain_3/
│   ├── id_conversions_rotate/
│   │
│   ├── models/
│   │   ├── transe_model_nll.pt
│   │   ├── transe_model_nll_other.pt
│   │   ├── transe_model_nll_exp_with_keywords.pt
│   │   ├── transe_model_nll_other1.pt
│   │   ├── transe_model_nll_other2.pt
│   │   └── transe_model_nll_other3.pt
│   │
│   ├── models_trained_scc/ # trained models corresponding to the same suffixes as the scripts
│   │   ├── transe_model_nll.pt
│   │   ├── transe_model_nll_complex.pt
│   │   ├── transe_model_nll_distmult.pt
│   │   ├── transe_model_nll_rotate.pt
│   │   ├── transe_model_nll_retrain_0.pt
│   │   ├── transe_model_nll_retrain_0_cwa.pt
│   │   ├── transe_model_nll_retrain_2.pt
│   │   └── transe_model_nll_retrain_3.pt
│   │
│   ├── saved/
│   ├── saved_retrain_0/
│   ├── saved_retrain_1/
│   ├── saved_retrain_2/
│   ├── saved_retrain_3/
│   │
│   ├── pytorch_threat_knowledge_graph.ipynb # Original model TransE
│   ├── pytorch_threat_knowledge_graph-complex.ipynb # ComplEx implementation
│   ├── pytorch_threat_knowledge_graph-distmult.ipynb # DistMult implementation
│   ├── pytorch_threat_knowledge_graph-exploits.ipynb # TransE model with exploits in the KG
│   ├── pytorch_threat_knowledge_graph_kw_other.ipynb # TransE model with keywords added to the KG
│   ├── pytorch_threat_knowledge_graph_retrain_top_0.ipynb # Retraining TransE model without CVE mapped to Discouraged/Prohibited CWE
│   ├── pytorch_threat_knowledge_graph_retrain_topk.ipynb # Script for retraining model with top k predictions (we try 1, 2 and 3)
│   └── pytorch_threat_knowledge_graph-rotate.ipynb # RotatE implementation
│
├── FixV2W/
│   ├── csv/
│   ├── files/
│   ├── kev_files/
│   │   # This folder contains preprocessed output from Exploit DB and KEVs
│   │   # used by the KEV analysis notebook.
│   ├── kev.ipynb
│   │   # This notebook produces the analysis of exploits and which exploits
│   │   # were remapped after they were exploited.
│   ├── pytorch_fixv2w_tutorial.ipynb
│   │   # This is the FixV2W tutorial using the PyTorch model. Here you can
│   │   # specify which model to use and its corresponding id_conversions folder.
│   └── pytorch_fixv2w_tutorial_with_other.ipynb
│       # This is the same tutorial as above, but also evaluates remapping
│       # for CWE-NoInfo and CWE-Other.
│
├── long_analysis_data/
│   ├── cve_modified/
│   ├── init_analysis/
│   ├── cwe_remap/
│   ├── combined_remaps.csv
│   ├── current_mappings.csv
│   ├── cve_mod.csv
│   └── cwe_remaps.csv
│
├── longitudinal_analysis/
│   └── long_analysis.ipynb
│       # This notebook retrieves the state of the NVD from past years by
│       # scraping the CVE Change History API and undoing those changes
│       # year by year. Preprocessing results are saved in long_analysis_data.
│
├── preprocess/
│   └── csv_file/
│       # Preprocessed NVD/CPE/CVE/CWE data used by the experiments.
│
├── pipelining/
│   ├── 0_get_data.ipynb
│   ├── 0.5_process_data.ipynb
│   ├── 1_experiment_train.ipynb
│   ├── 2_save_model.ipynb
│   ├── 5_rest_requests_single_model.ipynb
│   └── 6_database_injection.ipynb
│       # These notebooks form the pipeline that collects, updates, and
│       # retrains the TransE model. In NERC, this process is automated
│       # to run every week. The prefix indicates the pipeline step.
│
├── README.md
└──  requirements.txt

```


```

# How to run tutorials on the NERC

1. Make an account following the [onboarding instructions](https://nerc-project.github.io/nerc-docs/get-started/user-onboarding-on-NERC/).

2. Once added to the project by the PI, you can access the NERC OpenShift web console here:  
   [https://console.apps.shift.nerc.mghpcc.org/](https://console.apps.shift.nerc.mghpcc.org)

3. Log in with **mss-keycloak**.

4. To access RedHat OpenShift AI, which is useful for training and serving ML models, select the grid button shown below:  
   ![Grid Button Screenshot](https://github.com/user-attachments/assets/ce605c0f-3fc7-43bf-9e5f-81185e42a7ac)

5. The project you were added to should show up here under **Data Science Projects**. Click the appropriate project.

6. To run Jupyter Notebooks and train models, you can use a **Workbench**:  
   ![Workbench Screenshot](https://github.com/user-attachments/assets/8e02e734-2447-4ade-b913-af23fbb12dcb)

7. Select the blue **Create Workbench** button. Configure your workbench as you prefer, but you can use the instructions in this [example](https://nerc-project.github.io/nerc-docs/openshift-ai/other-projects/configure-jupyter-notebook-use-gpus-aiml-modeling/) to start learning how to configure the workbench to access GPUs for training.

8. To start the workbench, select **Start**. Then, to open the Jupyter Notebook, select the name of the workbench.
  <img width="1357" height="178" alt="image" src="https://github.com/user-attachments/assets/9e43ff43-d8bf-4347-b330-8dd29e4028ad" />

9. Log in with **mss-keycloak** again if necessary.

10. You can now run Python Notebooks. To clone or initialize a git repository, click **Git** in the navigation bar at the top of the page.

11. Once you are done working in the workbench, make sure to **Stop** the workbench. You can restart it when you work on it again.
   <img width="1357" height="203" alt="image" src="https://github.com/user-attachments/assets/e72a1ea4-2a4b-403e-b5e4-e1af5f66d0bd" />

# How to run tutorials in SCC using GPU
NERC does not support older versions of Python, so to run the original versions of the tutorials on the GPU, I used SCC. There are different ways to configure this, but I recommend using the Miniconda module. The following instructions are compatabile with Python 3.7.10, AmpliGraph 1.4.0, and Tensorflow 1.15.0. However, for other compatability information, reference [here for cuDNN](https://developer.nvidia.com/rdp/cudnn-archive) and [here for CUDA](https://www.tensorflow.org/install/source#gpu).
1. I recommend doing the following steps on an Interactive Desktop using 8 cores and 1 GPU.
   <img width="1046" height="610" alt="image" src="https://github.com/user-attachments/assets/ca193755-2dbe-47b6-ae98-2d0d42a7a6d4" />

3. Use these [instructions](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-software/miniconda-modules/) to load the Miniconda module. If you get an error saying: ```Cannot load module "miniconda/24.5.0" because these module(s) are loaded: python3 ```, unload the python3 module. It is not neccesary to create a conda environment.
4. Then, create an environment using: ```mamba create -y -n my_conda_env python=3.7.10 jupyterlab```.
5. Once created, activate the environment using ```mamba activate my_conda_env```. The name of your environment (in this case ```my_conda_env```, should be displayed).
6. Now, we need to install AmpliGraph 1.4.0, CUDA 10.0.0, cuDNN 7.6.5, Tensorflow 1.15.0, and Ipykernel. Run the following commands to do this.
```bash
mamba install -c conda-forge cudnn=7.6.5
mamba install -c conda-forge cudatoolkit=10.0.130
pip install ampligraph==1.4.0
pip install tensorflow-gpu==1.15
pip install ipykernel
python -m ipykernel install --user --name=my_conda_env
```
6. Then, run ```jupyter lab``` in your terminal, and it should open your directory in Jupyter Lab. Make sure the appropriate Kernel is selected in the top right corner (whatever you named your environment) so that you do not see any errors when importing the Python packages.

# How to run the pipeline on the NERC
1. Follow the steps until Step 5 from the first section about running tutorials in the ReadME. Then choose the appropriate research project. It should be the second one, the project without dashes in its name. This project has been allocated the appropriate resources to run a pipeline.
<img width="944" height="440" alt="image" src="https://github.com/user-attachments/assets/c328d686-bb70-463f-8665-3dc526143d25" />
2. Select "Workbenches," and then start the "trans-pipe" workbench to start.
3. The "pipelining" folder contains the model pipeline with data collection and retraining.

# FixV2W Webapp
A preliminary MVP webapp has been developed and can be found at [this repository](https://github.com/varsha487/fixv2w_webapp.git). It is an example of how the S3 Object Storage and Model Inference API endpoint can be used. It also depends on Supabase database.

# TODO
- Add a temporal analysis of FixV2W
- To the pipeline, add ability to pull from the database directly rather than files to reduce internal dependencies
- Integrate keywords into the pipeline, keywords are already saved when new data is retrieved from the NVD CVE Change History API, but it is not trained on currently
- For the UI, add styling to components for better formatting
- After running FixV2W, integrate an API call to an LLM to determine which out of the top 10 is most apt to remap. If there are no candidate CWES for remap, maybe use the LLM to narrow down the CWE-1003 list.
- Add CWE-Other and noinfo to the pipeline.
- See if for CWE-Other and noinfo, a candidate set can be generated based on common CPE mappings.
