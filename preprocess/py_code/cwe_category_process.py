import xml.etree.ElementTree as ET
import pandas as pd

cols = ["ID","Name", "Status", "Has_Member"]
rows = []

tree = ET.parse('../databases/2022nov/cwec_v4.9.xml')
root = tree.getroot()

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
