# test processing CVE in 2022

import json
import pandas as pd

f = open('../databases/2022/cve/nvdcve-1.1-2002.json')

cve = json.load(f)

cols = ["ID","MatchingCWE","MatchingCPE","baseSeverity","baseScore",
        "impactScore","exploitabilityScore","cvssV3_Vector","description"]
rows = []

for i in cve['CVE_Items']:
    # print(i['cve']['CVE_data_meta']['ID'])
    cveid = i['cve']['CVE_data_meta']['ID']
    cwe = []
    if 'problemtype' in i['cve']:
        for j in i['cve']['problemtype']['problemtype_data']:
            for k in j['description']:
                # print(k['value'])
                cwe.append(k['value'])
    cweStr = ';'.join(i for i in cwe)

    # print(i['cve']['description']['description_data'][0]['value'])
    description = i['cve']['description']['description_data'][0]['value']

    # print(i['configurations'])
    cpe = []
    if 'configurations' in i:
        for j in i['configurations']['nodes']:
            for k in j['cpe_match']:
                # print(k['cpe23Uri'])
                cpe.append(k['cpe23Uri'])
    cpeStr = ';'.join(i for i in cpe)

    # print(i['impact']['baseMetricV3']['cvssV3']['vectorString'])
    # print(i['impact']['baseMetricV3']['cvssV3']['baseScore'])
    # print(i['impact']['baseMetricV3']['cvssV3']['baseSeverity'])
    # print(i['impact']['baseMetricV3']['exploitabilityScore'])
    # print(i['impact']['baseMetricV3']['impactScore'])
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
    
df = pd.DataFrame(rows, columns=cols)
df.to_csv('./csv_file/cve/cve-2002.csv', encoding='utf-8-sig', index=False)

f.close()
