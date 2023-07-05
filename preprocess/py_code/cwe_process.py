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
