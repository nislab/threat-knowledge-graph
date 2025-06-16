```python
!pip install ampligraph==1.4.0
!pip install tensorflow==1.13.1
# Do not run if these are already installed
```

    **** Missing build for a loaded module for Python version "3.7.10". 
    Directory does not exist: /share/pkg.7/tensorflow/1.13.1/install/lib/site-packages/../python3.7/site-packages
    
    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: ampligraph==1.4.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (1.4.0)
    Requirement already satisfied: numpy>=1.14.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages/numpy-1.19.5-py3.7-linux-x86_64.egg (from ampligraph==1.4.0) (1.19.5)
    Requirement already satisfied: pytest>=3.5.1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (6.2.3)
    Requirement already satisfied: scikit-learn>=0.19.1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (0.24.2)
    Requirement already satisfied: tqdm>=4.23.4 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (4.60.0)
    Requirement already satisfied: pandas>=0.23.1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (1.2.4)
    Requirement already satisfied: sphinx<3,>=2.2 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from ampligraph==1.4.0) (2.4.5)
    Requirement already satisfied: recommonmark==0.4.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from ampligraph==1.4.0) (0.4.0)
    Requirement already satisfied: sphinx-rtd-theme==0.4.3 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from ampligraph==1.4.0) (0.4.3)
    Requirement already satisfied: sphinxcontrib-bibtex==0.4.2 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from ampligraph==1.4.0) (0.4.2)
    Requirement already satisfied: beautifultable>=0.7.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from ampligraph==1.4.0) (1.1.0)
    Requirement already satisfied: pyyaml>=3.13 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (5.4.1)
    Requirement already satisfied: rdflib>=4.2.2 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (5.0.0)
    Requirement already satisfied: scipy>=1.3.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages/scipy-1.6.2-py3.7-linux-x86_64.egg (from ampligraph==1.4.0) (1.6.2)
    Requirement already satisfied: networkx>=2.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (2.5.1)
    Requirement already satisfied: flake8>=3.7.7 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (3.8.4)
    Requirement already satisfied: setuptools>=36 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from ampligraph==1.4.0) (47.1.0)
    Requirement already satisfied: commonmark<=0.5.4 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from recommonmark==0.4.0->ampligraph==1.4.0) (0.5.4)
    Requirement already satisfied: docutils>=0.11 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from recommonmark==0.4.0->ampligraph==1.4.0) (0.16)
    Requirement already satisfied: pybtex>=0.20 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from sphinxcontrib-bibtex==0.4.2->ampligraph==1.4.0) (0.24.0)
    Requirement already satisfied: pybtex-docutils>=0.2.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from sphinxcontrib-bibtex==0.4.2->ampligraph==1.4.0) (1.0.2)
    Requirement already satisfied: six>=1.4.1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinxcontrib-bibtex==0.4.2->ampligraph==1.4.0) (1.15.0)
    Requirement already satisfied: oset>=0.1.3 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from sphinxcontrib-bibtex==0.4.2->ampligraph==1.4.0) (0.1.3)
    Requirement already satisfied: wcwidth in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from beautifultable>=0.7.0->ampligraph==1.4.0) (0.2.5)
    Requirement already satisfied: pyflakes<2.3.0,>=2.2.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from flake8>=3.7.7->ampligraph==1.4.0) (2.2.0)
    Requirement already satisfied: pycodestyle<2.7.0,>=2.6.0a1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from flake8>=3.7.7->ampligraph==1.4.0) (2.6.0)
    Requirement already satisfied: mccabe<0.7.0,>=0.6.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from flake8>=3.7.7->ampligraph==1.4.0) (0.6.1)
    Requirement already satisfied: importlib-metadata in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from flake8>=3.7.7->ampligraph==1.4.0) (1.7.0)
    Requirement already satisfied: decorator<5,>=4.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from networkx>=2.3->ampligraph==1.4.0) (4.4.2)
    Requirement already satisfied: python-dateutil>=2.7.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pandas>=0.23.1->ampligraph==1.4.0) (2.8.1)
    Requirement already satisfied: pytz>=2017.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pandas>=0.23.1->ampligraph==1.4.0) (2021.1)
    Requirement already satisfied: attrs>=19.2.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pytest>=3.5.1->ampligraph==1.4.0) (20.3.0)
    Requirement already satisfied: iniconfig in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pytest>=3.5.1->ampligraph==1.4.0) (1.1.1)
    Requirement already satisfied: packaging in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pytest>=3.5.1->ampligraph==1.4.0) (20.9)
    Requirement already satisfied: pluggy<1.0.0a1,>=0.12 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pytest>=3.5.1->ampligraph==1.4.0) (0.13.1)
    Requirement already satisfied: py>=1.8.2 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pytest>=3.5.1->ampligraph==1.4.0) (1.10.0)
    Requirement already satisfied: toml in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from pytest>=3.5.1->ampligraph==1.4.0) (0.10.2)
    Requirement already satisfied: isodate in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from rdflib>=4.2.2->ampligraph==1.4.0) (0.6.0)
    Requirement already satisfied: pyparsing in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from rdflib>=4.2.2->ampligraph==1.4.0) (2.4.7)
    Requirement already satisfied: joblib>=0.11 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from scikit-learn>=0.19.1->ampligraph==1.4.0) (1.0.1)
    Requirement already satisfied: threadpoolctl>=2.0.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from scikit-learn>=0.19.1->ampligraph==1.4.0) (2.1.0)
    Requirement already satisfied: sphinxcontrib-applehelp in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (1.0.2)
    Requirement already satisfied: sphinxcontrib-devhelp in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (1.0.2)
    Requirement already satisfied: sphinxcontrib-jsmath in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (1.0.1)
    Requirement already satisfied: sphinxcontrib-htmlhelp in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (1.0.3)
    Requirement already satisfied: sphinxcontrib-serializinghtml in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (1.1.4)
    Requirement already satisfied: sphinxcontrib-qthelp in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (1.0.3)
    Requirement already satisfied: Jinja2>=2.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (2.11.3)
    Requirement already satisfied: Pygments>=2.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (2.9.0)
    Requirement already satisfied: snowballstemmer>=1.1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (2.1.0)
    Requirement already satisfied: babel!=2.0,>=1.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (2.9.1)
    Requirement already satisfied: alabaster<0.8,>=0.7 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (0.7.12)
    Requirement already satisfied: imagesize in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (1.2.0)
    Requirement already satisfied: requests>=2.5.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from sphinx<3,>=2.2->ampligraph==1.4.0) (2.25.1)
    Requirement already satisfied: zipp>=0.5 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from importlib-metadata->flake8>=3.7.7->ampligraph==1.4.0) (3.4.1)
    Requirement already satisfied: MarkupSafe>=0.23 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from Jinja2>=2.3->sphinx<3,>=2.2->ampligraph==1.4.0) (1.1.1)
    Requirement already satisfied: latexcodec>=1.0.4 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from pybtex>=0.20->sphinxcontrib-bibtex==0.4.2->ampligraph==1.4.0) (2.0.1)
    Requirement already satisfied: chardet<5,>=3.0.2 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from requests>=2.5.0->sphinx<3,>=2.2->ampligraph==1.4.0) (4.0.0)
    Requirement already satisfied: idna<3,>=2.5 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from requests>=2.5.0->sphinx<3,>=2.2->ampligraph==1.4.0) (2.10)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from requests>=2.5.0->sphinx<3,>=2.2->ampligraph==1.4.0) (1.26.4)
    Requirement already satisfied: certifi>=2017.4.17 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from requests>=2.5.0->sphinx<3,>=2.2->ampligraph==1.4.0) (2020.12.5)
    [33mDEPRECATION: celery 5.0.5 has a non-standard dependency specifier pytz>dev. pip 24.1 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of celery or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063[0m[33m
    [0m[33mDEPRECATION: nb-black 1.0.7 has a non-standard dependency specifier black>='19.3'; python_version >= "3.6". pip 24.1 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of nb-black or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063[0m[33m
    [0m**** Missing build for a loaded module for Python version "3.7.10". 
    Directory does not exist: /share/pkg.7/tensorflow/1.13.1/install/lib/site-packages/../python3.7/site-packages
    
    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: tensorflow==1.13.1 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (1.13.1)
    Requirement already satisfied: absl-py>=0.1.6 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from tensorflow==1.13.1) (0.12.0)
    Requirement already satisfied: astor>=0.6.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (0.8.1)
    Requirement already satisfied: gast>=0.2.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (0.6.0)
    Requirement already satisfied: keras-applications>=1.0.6 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (1.0.8)
    Requirement already satisfied: keras-preprocessing>=1.0.5 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (1.1.2)
    Requirement already satisfied: numpy>=1.13.3 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages/numpy-1.19.5-py3.7-linux-x86_64.egg (from tensorflow==1.13.1) (1.19.5)
    Requirement already satisfied: six>=1.10.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from tensorflow==1.13.1) (1.15.0)
    Requirement already satisfied: protobuf>=3.6.1 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from tensorflow==1.13.1) (3.15.8)
    Requirement already satisfied: tensorboard<1.14.0,>=1.13.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (1.13.1)
    Requirement already satisfied: tensorflow-estimator<1.14.0rc0,>=1.13.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (1.13.0)
    Requirement already satisfied: termcolor>=1.1.0 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (2.3.0)
    Requirement already satisfied: grpcio>=1.8.6 in /usr3/graduate/sevvals/.local/lib/python3.7/site-packages (from tensorflow==1.13.1) (1.62.3)
    Requirement already satisfied: wheel>=0.26 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from tensorflow==1.13.1) (0.36.2)
    Requirement already satisfied: h5py in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from keras-applications>=1.0.6->tensorflow==1.13.1) (3.2.1)
    Requirement already satisfied: markdown>=2.6.8 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from tensorboard<1.14.0,>=1.13.0->tensorflow==1.13.1) (3.3.4)
    Requirement already satisfied: werkzeug>=0.11.15 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from tensorboard<1.14.0,>=1.13.0->tensorflow==1.13.1) (1.0.1)
    Requirement already satisfied: mock>=2.0.0 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from tensorflow-estimator<1.14.0rc0,>=1.13.0->tensorflow==1.13.1) (4.0.3)
    Requirement already satisfied: importlib-metadata in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from markdown>=2.6.8->tensorboard<1.14.0,>=1.13.0->tensorflow==1.13.1) (1.7.0)
    Requirement already satisfied: cached-property in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from h5py->keras-applications>=1.0.6->tensorflow==1.13.1) (1.5.2)
    Requirement already satisfied: zipp>=0.5 in /share/pkg.7/python3/3.7.10/install/lib/python3.7/site-packages (from importlib-metadata->markdown>=2.6.8->tensorboard<1.14.0,>=1.13.0->tensorflow==1.13.1) (3.4.1)
    [33mDEPRECATION: celery 5.0.5 has a non-standard dependency specifier pytz>dev. pip 24.1 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of celery or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063[0m[33m
    [0m[33mDEPRECATION: nb-black 1.0.7 has a non-standard dependency specifier black>='19.3'; python_version >= "3.6". pip 24.1 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of nb-black or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063[0m[33m
    [0m


```python
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import ampligraph
```


```python
# Load CWE Views, Categories and Hierarcical relationships (parent, peer..)
cwe_view = pd.read_csv("../datasets/processed/csv_file/2021aug/cwe_view.csv")
cwe_category = pd.read_csv("../datasets/processed/csv_file/2021aug/cwe_category.csv")
cwe_rels = pd.read_csv("./cwe_relations.csv")
```


```python
views = []

for i, item in cwe_view.iterrows():
    views.append([item['ID'],item['Name'],item['Has_Member']])
```


```python
categories = []

for i, item in cwe_category.iterrows():
    categories.append([item['ID'],item['Name'],item['Has_Member']])
```


```python
df_cve = pd.read_csv("../datasets/processed/csv_file/2021aug/cve/cve-2002.csv")
df_cve.fillna('*', inplace = True)
for i in range(2003, 2022):
    filename = '../datasets/processed/csv_file/2021aug/cve/cve-' + str(i) + '.csv'
    df_temp = pd.read_csv(filename)
    df_temp.fillna('*', inplace = True)
    df_cve=pd.concat([df_cve, df_temp])
```


```python
df_cwe = pd.read_csv("../datasets/processed/csv_file/2021aug/cwe.csv")
df_cwe.fillna('*', inplace=True)

df_cwe_cate = pd.read_csv("../datasets/processed/csv_file/2021aug/cwe_category.csv")
df_cwe_view = pd.read_csv("../datasets/processed/csv_file/2021aug/cwe_view.csv")
df_cwe_cate.fillna('*', inplace=True)
df_cwe_view.fillna('*', inplace=True)
```


```python
df_cwe_1003 = pd.read_csv("./cwe-1003.csv", usecols = ['CWE-ID','Weakness Abstraction'], index_col=False)
df_cwe_1003.fillna('*', inplace=True)
df_cwe_1003.columns
```




    Index(['CWE-ID', 'Weakness Abstraction'], dtype='object')




```python
cwe_sublist = []
cwe_1003 = []
cwe_disc = ["CWE-119","CWE-20","CWE-200","CWE-269","CWE-289",
"CWE-311","CWE-330","CWE-345","CWE-74","CWE-400","CWE-610","CWE-662",
"CWE-665","CWE-668","CWE-682","CWE-697","CWE-755","CWE-834"]
for i,r in df_cwe_1003.iterrows():
    cweid = r['CWE-ID']
    cwe_abs = r['Weakness Abstraction']
    cwe_1003.append(cweid)
    
    if cweid not in cwe_disc:
        cweid = "CWE-" + str(cweid)
        cwe_sublist.append((cweid,cwe_abs))
        
#print(cwe_sublist)
```


```python
cwe_list = []

kg_cwe = []

for i,r in df_cwe.iterrows():
    cweid = r['ID']
    cwe_list.append(cweid)
```


```python
kg_cvecwe_all = []

for i,r in df_cve.iterrows():
    cveid = r['ID']

    if (r['MatchingCWE'] != '*' and r['MatchingCWE'] != 'NVD-CWE-Other' and r['MatchingCWE'] != 'NVD-CWE-noinfo'):
        cwelist = r['MatchingCWE'].split(';')
        for w in cwelist:
            matchcwe = [cveid, 'MatchingCWE', w]
            kg_cvecwe_all.append((matchcwe))
    else:
        matchcwe = [cveid, 'MatchingCWE', r['MatchingCWE']]
        kg_cvecwe_all.append((matchcwe))
```


```python
df_cvecwe2 = pd.DataFrame(kg_cvecwe_all, columns = ['CVE', 'Predicate', 'CWE'])
```


```python
# Dataframe of all CVE-CWE mappings, including cwe-noinfo and cwe-other. 
df_cvecwe2.to_csv('df_cve2cwe.csv', index=False)
```

For each view and category, and each CVE that are mapped to those, we query the KG for valid CWE mappings from the members of the same view or category


```python
'''Get all CVE that are mapped to a given CWE, search in given list 'li' '''
def get_cve_cwe(cwe, li):
    cves = []
    for item in li:
        if(item[2] == cwe):
            cves.append(item[0])
    return(cves)
```


```python
cwe_dict = {}
for i, row in cwe_rels.iterrows():
    child = row['Child']
    parent = row['Parent']
    rel = row['Relationship']
    
    if rel == 'ChildOf':
        if child in cwe_dict:
            cwe_dict[child].append(parent)
        else:
            cwe_dict[child] = []
            cwe_dict[child].append(parent)
#print(cwe_dict)
```


```python
# using df_cwe_cate or df_cwe_view for querying for CWEs in that list (that can be used to map CVEs i.e. in CWE-1003 list)

def get_cwe_subtree(cweid):
    cwe_members = []
    if cweid in df_cwe_cate['ID'].tolist():    
        item = df_cwe_cate.loc[df_cwe_cate['ID'] == cweid]
        cwe_str = item['Has_Member']
        cwe_members= cwe_str.str.split(';')
        
    elif cweid in df_cwe_view['ID'].tolist():  
        item = df_cwe_view.loc[df_cwe_view['ID'] == cweid]
        cwe_str = item['Has_Member']
        cwe_members= cwe_str.str.split(';')
     
    cwe_ret = []
    for item in cwe_members:
        children = get_cwe_children(item)
        if item in cwe_1003:
            cwe_ret.append(item)
        for ch in children:
            if ch in cwe_1003:
                cwe_ret.append(ch)
    return cwe_ret
```


```python
# This is the first method I implemented to find family of the CWE. Usually, this yields a 
# large list of CWE that are related to each other, since we are returning the whole branch
# that CWE is in. Rather, we can also just return direct parents and children (below cell)

def get_cwe_parents(cwe):
    #given a cwe, find all related cwe that are in the same branch.
    family = []
    
    if cwe in cwe_dict:
        # exists as key - has parents.
        value = cwe_dict[cwe]
        for item in value:
            family.append(item)
            res = get_cwe_family(item) #recursively reach boss parent
            if res:
                family.extend(res)
    return family

def get_cwe_children(cwe):
    family = []
    
    if any(cwe in val for val in cwe_dict.values()):
        keys = [key for key, value in cwe_dict.items() if cwe in value]
        #print(keys)
        family.extend(keys)
        for item in keys:
            res = get_cwe_children(item)  
            if res:
                family.extend(res)
    return family
    
def get_cwe_family(cwe):
    return set(get_cwe_parents(cwe) + get_cwe_children(cwe))
```


```python
query_list = []
```


```python
for view in views:
    cve_list = get_cve_cwe(view[0], kg_cve2cwe)
    
    if(len(cve_list)>0):
        print(view[0], cve_list)
        query_list.append([view[0], cve_list])
```


```python
for cate in categories:
    cve_list2 = get_cve_cwe(cate[0], kg_cve2cwe)
    
    if(len(cve_list2)>0):
        #print(cate[0], cve_list2)
        query_list.append([cate[0], cve_list2])
```


```python
# List of discouraged CWE - so that these could be avoided when predicting good CWE possibilities
cwe_disc = ["CWE-119","CWE-20","CWE-200","CWE-269","CWE-289",
"CWE-311","CWE-330","CWE-345","CWE-74","CWE-400","CWE-610","CWE-662",
"CWE-665","CWE-668","CWE-682","CWE-697","CWE-755","CWE-834"]
```


```python
# Filtering those views and categories with no members
cwe_nomember = []
for item in query_list:
    cwe_subtree = get_cwe_subtree(item[0])
    if len(cwe_subtree) == 0:
        #print(item[0])
        cwe_nomember.append(item[0])
```


```python
# Combined list of PROHIBITED cwe = categories + views
cwe_proh = []
for cate in categories:
    cwe_proh.append(cate[0])
    
for view in views:
    cwe_proh.append(view[0])
```


```python
# Query triples for Discouraged set - CWE and the list of CVE mapped to those
query_disc = {}
for weak in cwe_disc:
    query_disc[weak] = []

for row in kg_cvecwe_all:
    cwe = row[2]#'CWE']
    for i in cwe.split(';'):
        if i in cwe_disc:
            query_disc[i].append(row[0])
```


```python
# Counting how many CVE are mapped to each Discouraged CWE in 2021. 
total = 0
for key in query_disc:
    print(key, len(query_disc[key]))
    total += len(query_disc[key])
print("total",total) #32761 for 2024 - total 30406 for 2021
```

    CWE-119 11476
    CWE-20 8389
    CWE-200 6722
    CWE-269 1109
    CWE-289 0
    CWE-311 169
    CWE-330 141
    CWE-345 163
    CWE-74 516
    CWE-400 912
    CWE-610 55
    CWE-662 23
    CWE-665 155
    CWE-668 225
    CWE-682 52
    CWE-697 21
    CWE-755 219
    CWE-834 59
    total 30406



```python
# Query triples for Discouraged set - CWE and the list of CVE mapped to those
query_proh = {}
for weak in cwe_proh:
    query_proh[weak] = []

for row in kg_cvecwe_all:
    cwe = row[2]
    for i in cwe.split(';'):
        if i in cwe_proh:
            query_proh[i].append(row[0])
```


```python
# Counting how many CVE are mapped to each Prohibited CWE in 2021. 
total = 0
for key in query_proh:
    if len(query_proh[key]) > 0:
        print(key, len(query_proh[key]))
        total += len(query_proh[key])

print("total",total) #13180 for 2024, 13596 for 2021.
```

    CWE-16 267
    CWE-189 1297
    CWE-19 229
    CWE-199 6
    CWE-254 421
    CWE-255 742
    CWE-264 5328
    CWE-275 63
    CWE-310 2494
    CWE-320 41
    CWE-361 7
    CWE-371 1
    CWE-388 35
    CWE-399 2649
    CWE-417 15
    CWE-895 1
    total 13596



```python
# Updated CVE-CWE mappings as of 2024 December - list we use to 'verify'
new_cve_df = pd.read_csv('./cve2cwe_2024.csv')
```

Next we filter the query sets to get the mappings that were updated


```python
# Prohibited Set
filtered_query_p = []
for key,value in query_proh.items():
    cwe_q = key
    cve_q = value
    cve_list = []
    for cve in cve_q: 
        row = new_cve_df.loc[new_cve_df["subject:START_ID"] == cve]
        cwe_match = list(row["object:END_ID"].values)
        #print(cwe_match)
        try:
            cwe_match.remove(cwe_q)
            # remove the known cwe from the updated CVE mapping, if it still exists
            # If the cwe was removed, this will fall into except
            # Otherwise, we'll include the new cwe and model will try to predict that 
        except:
            continue
        if len(cwe_match)>0:
            cve_list.append(cve)
    if cve_list:
        filtered_query_p.append([cwe_q,cve_list])
```


```python
# Discouraged Set
filtered_query_d = []
for key,value in query_disc.items():
    cwe_q = key
    cve_q = value
    cve_list = []
    for cve in cve_q: 
        row = new_cve_df.loc[new_cve_df["subject:START_ID"] == cve]
        cwe_match = list(row["object:END_ID"].values)
        #print(cwe_match)
        try:
            cwe_match.remove(cwe_q)
        except:
            continue
        if len(cwe_match)>0:
            cve_list.append(cve)
    if cve_list:
        filtered_query_d.append([cwe_q,cve_list])
```


```python
df_query = pd.DataFrame(filtered_query_p, columns = ['CWE','CVE'])
df_query.to_csv('filtered_query_p.csv')
```


```python
df_query = pd.DataFrame(filtered_query_d, columns = ['CWE','CVE'])
df_query.to_csv('filtered_query_d.csv')
```

Here, we are done with our preprocessing code.
We filtered the CVE that were mapped to prohibited or discouraged CWE on 2021 August, and were updated by 2024 December. The filtered query files can be used in the FixV2W tutorial.
