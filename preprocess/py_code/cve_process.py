import json
import pandas as pd

# When processing Aug 2021 version CVE, update end_year=2021
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
