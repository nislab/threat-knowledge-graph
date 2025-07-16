# Threat Knowledge Graph

This repository contains accompanying materials to the following works (available at https://people.bu.edu/staro/publications.html):

 * Zhenpeng Shi, Nikolay Matyunin, Kalman Graffi, and David Starobinski, "Uncovering CWE-CVE-CPE Relations with Threat Knowledge Graphs," *ACM Transactions on Privacy and Security*, Vol. 27, No. 1, Article 13: pp. 1-26, February 2024.
 * Sevval Simsek, Howell Xia, Jonah Gluck, David Sastre Medina, and David Starobinski, "Fixing Invalid CVE-CWE Mappings in Threat Databases," *IEEE COMPSAC 2025*, Toronto, Canada, July 2025.

In our knowledge graph research, we generate a **threat knowledge graph** from public threat databases, including Common Platform Enumeration (CPE), Common Vulnerabilities and Exposures (CVE), and Common Weakness Enumeration (CWE). Through knowledge graph embedding, we are able to uncover the CVE-CPE and CVE-CWE associations that might exist but are not known yet. Moreover, using the embedding querying, we predict top N CWE mappings for CVE, and categorize erroneous mappings based on knowledge graph evaluation metrics such as mean rank, mean reciprocal rank, and hits@N.

## Overview

This repository has five main folders: `/FixV2W/`, `/preprocess/`, `/threat_kg/`, `/kg_querying` and `/neo4j_import/`.

The `/FixV2W/`, folder contains the documents on applying knowledge graph querying to correct invalid CVE-CWE mappings in the National Vulnerability Database. The accompanying materials include preprocessed CVE-CWE mappings, CWE-1003 list, and others. We provide several versions of the FixV2W tutorial which is explained in the folder.

The `/preprocess/` folder contains the document on pre-processing the CPE, CVE, and CWE databases from their original formats to CSV files. This pre-processing step is documented in `database_preprocessing.md`. The processed databases are saved in `/csv_file/`. Moreover, the code for pre-processing is provided under `/py_code/`.


The `/threat_kg/` folder contains materials relevant to the threat knowledge graph, including generation, embedding, evaluation, and prediction. The details are documented in the Jupyter Notebook called `threat_knowledge_graph.ipynb`. Under the `/saved/` folder, we also save a few important files during this process for reuse, such as the knowledge graph as a list of triples.

The `/kg_querying` folder contains materials on the tutorial that elaborate on the knowledge graph embeddings, including categorization of erroneous (removed) mappings, querying the KG for CVE-CWE mapping queries, and method evaluations. 

The `/neo4j_import/` folder contains the document on importing the knowledge graph to [Neo4j Graph Database](https://neo4j.com/) for visualization and query. This process is detailed in `threat_kg_with_neo4j.md`. The knowledge graph is stored as a set of CSV files under `/files/`, such that it can be easily imported into Neo4j.

## Workflow

Our workflow is illustrated in the following figure:

![Workflow illustration](figures/workflow1.png "Workflow")

First, we download the CPE, CVE, and CWE data feed from the MITRE and NVD websites. The downloaded databases are in their original formats, such as JSON and XML. Next, we run our Python code to pre-process those databases into CSV files. We then import the CSV files into a Jupyter Notebook as Pandas DataFrames, and extract the knowledge graph triples from them. The knowledge graph is represented as a long list of triples, and the embedding process is completed with the help of a Python package named AmpliGraph.

With the embedded knowledge graph, we can evaluate its quality and prediction capability using standard metrics. We conduct both closed-world evaluation, where the test set is a subset of the knowledge graph, and open-world evaluation, where the test set consists of newly added triples that were not in the knowledge graph. This evaluation process is illustrated in the figure below.

![Usage of embedded knowledge graph](figures/workflow2.png "Prediction")


## License

These materials may be freely used and distributed, provided that attribution to this original source is acknowledged. If you use the resources in this repository, we kindly ask that you refer to the following work:

- Zhenpeng Shi, Nikolay Matyunin, Kalman Graffi, and David Starobinski, "Uncovering CWE-CVE-CPE Relations with Threat Knowledge Graphs," *ACM Transactions on Privacy and Security*, Vol. 27, No. 1, Article 13: pp. 1-26, February 2024.
    ```
    @article{shi2024uncovering,
    author = {Shi, Zhenpeng and Matyunin, Nikolay and Graffi, Kalman and Starobinski, David},
    title = {Uncovering CWE-CVE-CPE Relations with Threat Knowledge Graphs},
    year = {2024},
    issue_date = {February 2024},
    publisher = {Association for Computing Machinery},
    volume = {27},
    number = {1},
    issn = {2471-2566},
    url = {https://doi.org/10.1145/3641819},
    journal = {ACM Transactions on Privacy and Security},
    month = feb,
    articleno = {13},
    numpages = {26},
    }

    ```
  

- Sevval Simsek, Howell Xia, Jonah Gluck, David Sastre Medina, and David Starobinski, "Fixing Invalid CVE-CWE Mappings in Threat Databases," *IEEE COMPSAC 2025*, Toronto, Canada, July 2025.
    ```
    @inproceedings{simsek2025fixing,
    title={Fixing Invalid CVE-CWE Mappings in Threat Databases},
    author={\c{S}im\c{s}ek, \c{S}evval and Xia, Howell and Gluck, Jonah, and Medina, David Sastre and Starobinski, David},
    booktitle={2025 IEEE COMPSAC},
    year={2025},
    organization={IEEE}
    }
    ```

    
## Acknowledgments

This project was supported in part by
- The Red Hat Collaboratory at Boston University 
- The US National Science Foundation
- Honda Research Institute Europe GmbH and BU Hariri Institute Research Incubation Award 
  
