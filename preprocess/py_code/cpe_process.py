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

        # replace special characters for importing to Neo4j
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

