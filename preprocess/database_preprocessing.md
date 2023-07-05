# Pre-process the CPE, CVE, and CWE databases

## Introduction

This document shows how to pre-process the raw data in CPE, CVE, and CWE into `csv` format, which will be used to generate knowledge graph triples.

This work uses three databases: Common Platform Enumeration (CPE), Common Vulnerabilities and Exposures (CVE), and Common Weakness Enumeration (CWE). CVE and CWE are managed by MITRE, and CPE is managed by NVD. NVD also extends the CVE with additional information (e.g., associations to CPE and CWE), which we use to generate the knowledge graph.

The latest versions of the databases can be downloaded from their official websites:
- [CPE data feed (by NVD)](https://nvd.nist.gov/products/cpe)
- [CVE data feed (by MITRE and NVD)](https://nvd.nist.gov/vuln/data-feeds)
- [CWE data feed (by MITRE)](https://cwe.mitre.org/data/downloads.html)

**Note:** NVD plans to retire the data feed of CPE and their extened version of CVE by September, 2023. The NVD data feeds will be replaced by NVD [CPE API](https://nvd.nist.gov/developers/products) and [CVE API](https://nvd.nist.gov/developers/vulnerabilities).

In our work, we used four snapshots of the CPE, CVE, and CWE databases, which were taken on August 4, 2021, March 30, 2022, July 14, 2022, and November 1, 2022, respectively. Due to the large size, we avoid uploading those the original databases. Instead, we share the processed version of the four snapshots of data under `/preprocess/csv_file/` (tagged with the corresponding time). The latest version of the CPE, CVE, and CWE can be downloaded from the links above, and pre-processed following this document.

**Note:** The snapshot of the databases on August 4, 2021 is imperfect: the CPE is in fact a little outdated (downloaded on June 24, 2021), which might lead to inconsistency with CVE. Therefore, this version of processed data should be used judiciously. Nonetheless, we find that the inconsistency appears very rarely, and the resultant threat knowledge graph performs on the same level with other versions of knowledge graphs.

For demonstration, we use the CPE, CVE, and CWE on November 1, 2022. As a result, we assume that the databases are downloaded and stored under `/databases/2022nov/`. Specifically, we have the CPE file as `/databases/2022nov/official-cpe-dictionary_v2.3.xml`, the CWE file as `/databases/2022nov/cwec_v4.9.xml`, and the CVE files (e.g., `nvdcve-1.1-2020.json`) under `/databases/2022nov/cve/`. We will save the processed files under `/preprocess/csv_file/2022nov/`. 

## CPE Pre-processing

We start with CPE, which is saved as an `XML` file. The file contains a list of CPE entries, where an example entry is as follows
```xml
<cpe-item name="cpe:/a:google:chrome:89.0.4389.90">
    <title xml:lang="en-US">Google Chrome 89.0.4389.90</title>
    <references>
        <reference href="https://chromereleases.googleblog.com/search/label/Stable%20updates">Version</reference>
    </references>
    <cpe-23:cpe23-item name="cpe:2.3:a:google:chrome:89.0.4389.90:*:*:*:*:*:*:*"/>
</cpe-item>
```
We would like to extract the entry name under CPE v2.3, which is the `name` *attribute* in the `cpe-23:cpe23-item` *tag*:
```
<cpe-23:cpe23-item name="cpe:2.3:a:google:chrome:89.0.4389.90:*:*:*:*:*:*:*"/>
```

Generally, the CPE v2.3 names the entries in the form of
```
cpe:2.3:part:vendor:product:version:update:edition:language:sw_edition:target_sw:target_hw:other
```
We will use the entire name to represent each CPE entry, in the meantime, we will extract its attributes separately, including *part*, *vendor*, *product*, *target_sw*, *target_hw*, and so on.

In order to pre-process the XML file, we use the [ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html). The CPE databases in `csv` format will be saved as `cpe.csv` under `/preprocess/csv_file/2022nov/`. The code can also be found as `/preprocess/py_code/cpe_process.py`.

```python
import xml.etree.ElementTree as ET
import pandas as pd

cols = ["part","vendor","product","version","update","edition",
        "language","sw_edition","target_sw","target_hw","other",
        "cpe23-item", "title", "cpe-item"]
rows = []

tree = ET.parse('../databases/2022nov/official-cpe-dictionary_v2.3.xml')
root = tree.getroot()

for i in root:
    if i.tag == "{http://cpe.mitre.org/dictionary/2.0}cpe-item":
        cpe23 = i.find("{http://scap.nist.gov/schema/cpe-extension/2.3}cpe23-item").attrib["name"]
        title = i.find("{http://cpe.mitre.org/dictionary/2.0}title").text
        item = i.attrib["name"]

        # replace special characters to avoid problems when importing to Neo4j Graph Database
        cpe23 = cpe23.replace('\,', '\.')
        cpe23 = cpe23.replace('\:', '\;')
        cpe23 = cpe23.replace('"', "'")

        cpe23_split = cpe23.split(':')
        rows.append({"part": cpe23_split[2],
                    "vendor": cpe23_split[3],
                    "product": cpe23_split[4],
                    "version": cpe23_split[5],
                    "update": cpe23_split[6],
                    "edition": cpe23_split[7],
                    "language": cpe23_split[8],
                    "sw_edition": cpe23_split[9],
                    "target_sw": cpe23_split[10],
                    "target_hw": cpe23_split[11],
                    "other": cpe23_split[12],
                    "cpe23-item": cpe23,
                    "title": title,
                    "cpe-item": item})

df = pd.DataFrame(rows, columns=cols)
df.to_csv('./csv_file/2022nov/cpe.csv', index=False)
```

As a result, the CPE will be stored in the form of
```
part,vendor,product,version,update,edition,language,sw_edition,target_sw,target_hw,other,cpe23-item,title,cpe-item
a,google,chrome,89.0.4389.90,*,*,*,*,*,*,*,cpe:2.3:a:google:chrome:89.0.4389.90:*:*:*:*:*:*:*,Google Chrome 89.0.4389.90,cpe:/a:google:chrome:89.0.4389.90
```

When generating the knowledge graph, we also implement a naive *optimization*, which is to merge the CPE entries by ignoring all version numbers. In addition, we get rid of some attributes that will not be added to the knowledge graph. As a result, each merged CPE entry is in the form of 
```
cpe:part:vendor:product:target_sw:target_hw
```
The code can also be found as `/preprocess/py_code/cpe_merge.py`.
```python
import pandas as pd

df = pd.read_csv("./csv_file/2022nov/cpe.csv", usecols=['part','vendor',
                'product','version','target_sw','target_hw',
                'cpe23-item','title'])

# merge CPEs by ignoring version numbers
df_uni = df.drop(columns=['version','cpe23-item', 'title'])
df_uni['name'] = 'cpe:' + df_uni['part'] + ':' + df_uni['vendor'] + ':' + df_uni['product'] + ':' + df_uni['target_sw'] + ':' + df_uni['target_hw'] 
df_uni = df_uni.groupby(df_uni.columns.tolist(),as_index=False).size()
df_uni = df_uni.sort_values(by='size', ascending=False)

df_uni.to_csv('./csv_file/2022nov/cpe_ignore_version.csv', index=False)
```

We also count the number of entries that matches the merged entry, which is denoted by "size". The merged CPE database will be saved as `cpe_ignore_version.csv`. As a result, the merged CPEs look like this
```
part,vendor,product,target_sw,target_hw,name,size
a,google,chrome,*,*,cpe:a:google:chrome:*:*,9065
```


## CVE Pre-processing

CVE is stored in `JSON` format, so we will use the Python built-in json package for pre-processing. 

An example CVE is as follows (some contents are omitted to save space, marked as `...`). For the threat knowledge graph, we need the CVE ID, as well as matched CWEs and CPEs. The description and CVSS V3 vectors can be used to enhance the knowledge graph, so we include them as well.
```json
{
"cve" : {
    "data_type" : "CVE",
    "data_format" : "MITRE",
    "data_version" : "4.0",
    "CVE_data_meta" : {
    "ID" : "CVE-2021-0003",
    "ASSIGNER" : "secure@intel.com"
    },
    "problemtype" : {
    "problemtype_data" : [ {
        "description" : [ {
        "lang" : "en",
        "value" : "CWE-755"
        } ]
    } ]
    },
    "references" : {
    "reference_data" : [ ... ]
    },
    "description" : {
    "description_data" : [ {
        "lang" : "en",
        "value" : "Improper conditions check in some Intel(R) Ethernet Controllers 800 series Linux drivers before version 1.4.11 may allow an authenticated user to potentially enable information disclosure via local access."
    } ]
    }
},
"configurations" : {
    "CVE_data_version" : "4.0",
    "nodes" : [ {
    "operator" : "AND",
    "children" : [ {
        "operator" : "OR",
        "children" : [ ],
        "cpe_match" : [ {
        "vulnerable" : true,
        "cpe23Uri" : "cpe:2.3:o:intel:ethernet_controller_e810_firmware:*:*:*:*:*:linux:*:*",
        "versionEndExcluding" : "1.4.11",
        "cpe_name" : [ ]
        } ]
    }, {
        "operator" : "OR",
        "children" : [ ],
        "cpe_match" : [ {
        "vulnerable" : false,
        "cpe23Uri" : "cpe:2.3:h:intel:ethernet_controller_e810:-:*:*:*:*:*:*:*",
        "cpe_name" : [ ]
        } ]
    } ],
    "cpe_match" : [ ]
    } ]
},
"impact" : {
    "baseMetricV3" : {
    "cvssV3" : {
        "version" : "3.1",
        "vectorString" : "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
        "attackVector" : "LOCAL",
        "attackComplexity" : "LOW",
        "privilegesRequired" : "LOW",
        "userInteraction" : "NONE",
        "scope" : "UNCHANGED",
        "confidentialityImpact" : "HIGH",
        "integrityImpact" : "NONE",
        "availabilityImpact" : "NONE",
        "baseScore" : 5.5,
        "baseSeverity" : "MEDIUM"
    },
    "exploitabilityScore" : 1.8,
    "impactScore" : 3.6
    },
    "baseMetricV2" : { ... }
},
"publishedDate" : "2021-08-11T13:15Z",
"lastModifiedDate" : "2021-09-14T18:36Z"
}
```

We pre-process the CVE using the following code. The code can also be found as `/preprocess/py_code/cve_process.py`.
```python
import json
import pandas as pd

# match end_year with the version of CVE
# e.g., when processing Aug 2021 version CVE, update end_year=2021
start_year = 2002
end_year = 2022
year = list(range(start_year, end_year+1))

for y in year:

    openname = '../databases/2022nov/cve/nvdcve-1.1-' + str(y) + '.json'

    f = open(openname, 'rb')

    cve = json.load(f)

    cols = ["ID", "MatchingCWE", "MatchingCPE", "baseSeverity", "baseScore",
            "impactScore", "exploitabilityScore", "cvssV3_Vector","description"]
    rows = []

    for i in cve['CVE_Items']:
        cveid = i['cve']['CVE_data_meta']['ID']
        cwe = []
        if 'problemtype' in i['cve']:
            for j in i['cve']['problemtype']['problemtype_data']:
                for k in j['description']:
                    # print(k['value'])
                    cwe.append(k['value'])
        cweStr = ';'.join(i for i in cwe)

        description = i['cve']['description']['description_data'][0]['value']

        cpe = []
        if 'configurations' in i:
            for j in i['configurations']['nodes']:
                for k in j['cpe_match']:
                    cpe.append(k['cpe23Uri'])
        cpeStr = ';'.join(i for i in cpe)

        baseSeverity = ''
        baseScore = ''
        impactScore = ''
        exploitabilityScore = ''
        cvssV3_Vector = ''
        if 'baseMetricV3' in i['impact']:
            baseSeverity = i['impact']['baseMetricV3']['cvssV3']['baseSeverity']
            baseScore = i['impact']['baseMetricV3']['cvssV3']['baseScore']
            impactScore = i['impact']['baseMetricV3']['impactScore']
            exploitabilityScore = i['impact']['baseMetricV3']['exploitabilityScore']
            cvssV3_Vector = i['impact']['baseMetricV3']['cvssV3']['vectorString']

        rows.append({"ID": cveid,
                     "MatchingCWE": cweStr,
                     "MatchingCPE": cpeStr,
                     "baseSeverity": baseSeverity,
                     "baseScore": baseScore,
                     "impactScore": impactScore,
                     "exploitabilityScore": exploitabilityScore,
                     "cvssV3_Vector": cvssV3_Vector,
                     "description": description})

    savename = './csv_file/2022nov/cve/cve-' + str(y) + '.csv'

    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(savename, index=False, encoding='utf-8-sig')

    f.close()
```

The generated `csv` files will be saved by years, for example, in `cve-2021.csv`, we have
```
ID,MatchingCWE,MatchingCPE,baseSeverity,baseScore,impactScore,exploitabilityScore,cvssV3_Vector,description
CVE-2021-0003,CWE-755,,MEDIUM,5.5,3.6,1.8,CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N,Improper conditions check in some Intel(R) Ethernet Controllers 800 series Linux drivers before version 1.4.11 may allow an authenticated user to potentially enable information disclosure via local access.
```

## CWE Pre-processing

CWE is also in XML format, and has three types of entries: weakness, view, and category (for more information, see the [CWE glossary webpage](https://cwe.mitre.org/documents/glossary/index.html)). An example CWE weakness entry is shown in the following (some contents are omitted to save space, marked as `...`):
```xml
      <Weakness ID="364" Name="Signal Handler Race Condition" Abstraction="Base" Structure="Simple" Status="Incomplete">
         <Description>The software uses a signal handler that introduces a race condition.</Description>
         <Extended_Description>
            ...
         </Extended_Description>
         <Related_Weaknesses>
            <Related_Weakness Nature="ChildOf" CWE_ID="362" View_ID="1000" Ordinal="Primary"/>
            <Related_Weakness Nature="CanPrecede" CWE_ID="415" View_ID="1000"/>
            <Related_Weakness Nature="CanPrecede" CWE_ID="416" View_ID="1000"/>
            <Related_Weakness Nature="CanPrecede" CWE_ID="123" View_ID="1000"/>
         </Related_Weaknesses>
         <Applicable_Platforms>
            <Language Name="C" Prevalence="Sometimes"/>
            <Language Name="C++" Prevalence="Sometimes"/>
         </Applicable_Platforms>
         <Modes_Of_Introduction>
            <Introduction>
               <Phase>Architecture and Design</Phase>
            </Introduction>
            <Introduction>
               <Phase>Implementation</Phase>
            </Introduction>
         </Modes_Of_Introduction>
         <Likelihood_Of_Exploit>Medium</Likelihood_Of_Exploit>
         <Common_Consequences>
            <Consequence>
               <Scope>Integrity</Scope>
               <Scope>Confidentiality</Scope>
               <Scope>Availability</Scope>
               <Impact>Modify Application Data</Impact>
               <Impact>Modify Memory</Impact>
               <Impact>DoS: Crash, Exit, or Restart</Impact>
               <Impact>Execute Unauthorized Code or Commands</Impact>
               <Note>It may be possible to cause data corruption and possibly execute arbitrary code by modifying global variables or data structures at unexpected times, violating the assumptions of code that uses this global data.</Note>
            </Consequence>
            <Consequence>
               <Scope>Access Control</Scope>
               <Impact>Gain Privileges or Assume Identity</Impact>
               <Note>If a signal handler interrupts code that is executing with privileges, it may be possible that the signal handler will also be executed with elevated privileges, possibly making subsequent exploits more severe.</Note>
            </Consequence>
         </Common_Consequences>
         <Potential_Mitigations>
            <Mitigation Mitigation_ID="MIT-3">
               <Phase>Requirements</Phase>
               <Strategy>Language Selection</Strategy>
               <Description>Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.</Description>
            </Mitigation>
            <Mitigation>
               <Phase>Architecture and Design</Phase>
               <Description>Design signal handlers to only set flags, rather than perform complex functionality. These flags can then be checked and acted upon within the main program loop.</Description>
            </Mitigation>
            <Mitigation>
               <Phase>Implementation</Phase>
               <Description>Only use reentrant functions within signal handlers. Also, use validation to ensure that state is consistent while performing asynchronous actions that affect the state of execution.</Description>
            </Mitigation>
         </Potential_Mitigations>
         <Demonstrative_Examples>
            ...
         </Demonstrative_Examples>
         <Observed_Examples>
            ...
         </Observed_Examples>
         <Functional_Areas>
            <Functional_Area>Signals</Functional_Area>
            <Functional_Area>Interprocess Communication</Functional_Area>
         </Functional_Areas>
         <Affected_Resources>
            <Affected_Resource>System Process</Affected_Resource>
         </Affected_Resources>
         <Taxonomy_Mappings>
            ...
         </Taxonomy_Mappings>
         <References>
            ...
         </References>
         <Content_History>
            ...
         </Content_History>
      </Weakness>
```

As we can note from the example above, CWE entries are much more detailed than CPE and CVE entries, and they might provide a lot of useful information. In our work, we have only include some "structured" keyword-like attributes in the knowledge graph. For example, the applicable languages of CWE-364 are C and C++, and the likelihood of exploit is medium. For the common consequences, the detailed impacts are grouped by *scope*, though we only include all the scope keywords in the knowledge graph for now.

Again, we use the ElementTree XML API to process the CWE. The CWE weaknesses in `csv` format will be saved as `cwe.csv` under `/preprocess/csv_file/2022nov`. The code can also be found as `/preprocess/py_code/cwe_process.py`. 
```python
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import pandas as pd
import re

cols = ["ID","Name","Description","Extended_Description","Related_Weakness","Language","Technology",
        "Likelihood_Of_Exploit","Consequence","CVE_Example"]
rows = []

tree = ET.parse('../databases/2022nov/cwec_v4.9.xml')
root = tree.getroot()

for item in root.iter("{http://cwe.mitre.org/cwe-6}Weakness"):
    if 'DEPRECATED' in item.attrib['Name']:
        continue
    cweid = 'CWE-' + item.attrib['ID']
    name = '"' + item.attrib['Name'] + '"'
    description = ''
    for child in item:
        if child.tag == "{http://cwe.mitre.org/cwe-6}Description":
            description = child.text.replace('\n', ' ').replace('\t', '')
            description = re.sub(' +', ' ', description)

    extended = ''
    for child in item:
        if child.tag == "{http://cwe.mitre.org/cwe-6}Extended_Description":
            extended = tostring(child, method='text').decode('utf-8')
            extended = extended.replace('\n', ' ').replace('\t', '')
            extended = re.sub(' +', ' ', extended)

    related = []
    language = []
    technology = []
    likelyhood = ''
    consequence = []
    example = []
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Related_Weakness"):
        related.append(i.attrib['Nature'] + ':' + i.attrib['CWE_ID'])
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Language"):
        if ('Class' in i.attrib):
            language.append(i.attrib['Class'])
        elif ('Name' in i.attrib):
            language.append(i.attrib['Name'])
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Technology"):
        if ('Class' in i.attrib):
            technology.append(i.attrib['Class'])
        elif ('Name' in i.attrib):
            technology.append(i.attrib['Name'])
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Likelihood_Of_Exploit"):
        likelyhood = i.text
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Common_Consequences"):
        for j in i.iter("{http://cwe.mitre.org/cwe-6}Consequence"):
            for k in j.iter("{http://cwe.mitre.org/cwe-6}Scope"):
                if (not k.text in consequence):
                    consequence.append(k.text)
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Observed_Examples"):
        for j in i.iter("{http://cwe.mitre.org/cwe-6}Observed_Example"):
            for k in j.iter("{http://cwe.mitre.org/cwe-6}Reference"):
                if (not k.text in example):
                    example.append(k.text)

    relatedStr = ';'.join(i for i in related)
    languageStr = ';'.join(i for i in language)
    technologyStr = ';'.join(i for i in technology)
    consequenceStr = ';'.join(i for i in consequence)
    exampleStr = ';'.join(i for i in example)

    rows.append({"ID": cweid,
                "Name": name,
                "Description": description,
                "Extended_Description": extended,
                "Related_Weakness": relatedStr,
                "Language": languageStr,
                "Technology": technologyStr,
                "Likelihood_Of_Exploit": likelyhood,
                "Consequence": consequenceStr,
                "CVE_Example": exampleStr})
    
df = pd.DataFrame(rows, columns=cols)

df.to_csv('./csv_file/2022nov/cwe.csv', index=False, encoding='utf-8-sig')
```

The structure of CWE views and categories is not exactly the same as CWE weaknesses. Here are example CWE view and category:
```xml
      <View ID="1008" Name="Architectural Concepts" Type="Graph" Status="Incomplete">
         <Objective>This view organizes weaknesses according to common architectural security tactics. It is intended to assist architects in identifying potential mistakes that can be made when designing software.</Objective>
         <Audience>
            <Stakeholder>
               <Type>Software Developers</Type>
               <Description>Architects that are part of a software development team may find this view useful as the weaknesses are organized by known security tactics, aiding the arcitect in embedding security throughout the design process instead of discovering weaknesses after the software has been built.</Description>
            </Stakeholder>
            <Stakeholder>
               <Type>Educators</Type>
               <Description>Educators may use this view as reference material when discussing security by design or architectural weaknesses, and the types of mistakes that can be made.</Description>
            </Stakeholder>
         </Audience>
         <Members>
            <Has_Member CWE_ID="1009" View_ID="1008"/>
            <Has_Member CWE_ID="1010" View_ID="1008"/>
            <Has_Member CWE_ID="1011" View_ID="1008"/>
            <Has_Member CWE_ID="1012" View_ID="1008"/>
            ...
         </Members>
         <References>
            <Reference External_Reference_ID="REF-9"/>
            <Reference External_Reference_ID="REF-10" Section="pages 69 - 78"/>
         </References>
         <Notes>
            ...
         </Notes>
         <Content_History>
            ...
         </Content_History>
      </View>
```

```xml
    <Category ID="1010" Name="Authenticate Actors" Status="Draft">
         <Summary>Weaknesses in this category are related to the design and architecture of authentication components of the system. Frequently these deal with verifying the entity is indeed who it claims to be. The weaknesses in this category could lead to a degradation of the quality of authentication if they are not addressed when designing or implementing a secure architecture.</Summary>
         <Relationships>
            <Has_Member CWE_ID="258" View_ID="1008"/>
            <Has_Member CWE_ID="259" View_ID="1008"/>
            <Has_Member CWE_ID="262" View_ID="1008"/>
            <Has_Member CWE_ID="263" View_ID="1008"/>
            ...
         </Relationships>
         <References>
            <Reference External_Reference_ID="REF-9"/>
            <Reference External_Reference_ID="REF-10" Section="pages 69 - 78"/>
         </References>
         <Content_History>
            ...
         </Content_History>
      </Category>
```

Similarly, the CWE views and categories will be saved in `cwe_category.csv` and `cwe_view.csv` under `/preprocess/csv_file/2022nov`. The code can also be found as `/preprocess/py_code/cwe_category_process.py` and `/preprocess/py_code/cwe_view_process.py`.

```python
import xml.etree.ElementTree as ET
import pandas as pd

cols = ["ID","Name", "Type", "Status", "Has_Member"]
rows = []

tree = ET.parse('../databases/2022nov/cwec_v4.9.xml')
root = tree.getroot()

# pre-process CWE view entries
for item in root.iter("{http://cwe.mitre.org/cwe-6}View"):
    if 'Deprecated' in item.attrib['Status']:
        continue
    cid = 'CWE-' + item.attrib['ID']
    name = '"' + item.attrib['Name'] + '"'
    typ = item.attrib['Type']
    status = item.attrib['Status']
    hasmember = []
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Members"):
        for j in i.iter("{http://cwe.mitre.org/cwe-6}Has_Member"):
            hasmember.append('CWE-' + j.attrib['CWE_ID'])

    hasmemberStr = ';'.join(i for i in hasmember)

    rows.append({"ID": cid,
                "Name": name,
                "Type": typ,
                "Status": status,
                "Has_Member": hasmemberStr})
    
df = pd.DataFrame(rows, columns=cols)
df.to_csv('./csv_file/2022nov/cwe_view.csv', index=False)
```

```python
import xml.etree.ElementTree as ET
import pandas as pd

cols = ["ID","Name", "Status", "Has_Member"]
rows = []

tree = ET.parse('../databases/2022nov/cwec_v4.9.xml')
root = tree.getroot()

# pre-process CWE weakness entries
for item in root.iter("{http://cwe.mitre.org/cwe-6}Category"):
    if 'Deprecated' in item.attrib['Status']:
        continue
    cid = 'CWE-' + item.attrib['ID']
    name = '"' + item.attrib['Name'] + '"'
    status = item.attrib['Status']
    hasmember = []
    for i in item.iter("{http://cwe.mitre.org/cwe-6}Relationships"):
        for j in i.iter("{http://cwe.mitre.org/cwe-6}Has_Member"):
            hasmember.append('CWE-' + j.attrib['CWE_ID'])

    hasmemberStr = ';'.join(i for i in hasmember)

    rows.append({"ID": cid,
                "Name": name,
                "Status": status,
                "Has_Member": hasmemberStr})
    
df = pd.DataFrame(rows, columns=cols)
df.to_csv('./csv_file/2022nov/cwe_category.csv', index=False)
```

After processing, the CWE will be saved in the form of
Weaknesses:
```
ID,Name,Description,Related_Weakness,Language,Technology,Likelihood_Of_Exploit,Consequence,CVE_Example
CWE-364,"""Signal Handler Race Condition""",The software uses a signal handler that introduces a race condition.,ChildOf:362;CanPrecede:415;CanPrecede:416;CanPrecede:123,C;C++,,Medium,Integrity;Confidentiality;Availability;Access Control,CVE-1999-0035;CVE-2001-0905;CVE-2001-1349;CVE-2004-0794;CVE-2004-2259
```
Views:
```
ID,Name,Type,Status,Has_Member
CWE-1008,"""Architectural Concepts""",Graph,Incomplete,CWE-1009;CWE-1010;CWE-1011;CWE-1012;CWE-1013;CWE-1014;CWE-1015;CWE-1016;CWE-1017;CWE-1018;CWE-1019;CWE-1020
```
Categories:
```
ID,Name,Status,Has_Member
CWE-1010,"""Authenticate Actors""",Draft,CWE-258;CWE-259;CWE-262;CWE-263;CWE-287;CWE-288;CWE-289;CWE-290;CWE-291;CWE-293;CWE-294;CWE-301;CWE-302;CWE-303;CWE-304;CWE-305;CWE-306;CWE-307;CWE-308;CWE-322;CWE-521;CWE-593;CWE-603;CWE-620;CWE-640;CWE-798;CWE-836;CWE-916
```

So far, we have pre-processed CPE, CVE, and CWE into `csv` files, and we are ready to generate knowledge graph triples from them (see `/threat_kg/threat_knowledge_graph.ipynb`).