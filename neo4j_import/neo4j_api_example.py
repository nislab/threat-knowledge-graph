from neo4j import GraphDatabase
import numpy as np
import pandas as pd

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def cwe_test(self, message):
        with self.driver.session() as session:
            cwes = session.write_transaction(self._return_cwes, message)
            return cwes

    @staticmethod
    def _return_cwes(tx, message):
        result = tx.run("match (p:CPE)-[r:MatchingCVE]->(v:CVE),(v)-[]->(w:CWE) \
            where p.name = $message \
            return w.Name,w.Abstract, w.Consequence", message=message)
        entire_result = [] # Will contain all the items
        for record in result:
            entire_result.append(record)
        return entire_result

    def cve_test(self, message):
        with self.driver.session() as session:
            cwes = session.write_transaction(self._return_cves, message)
            return cwes

    @staticmethod
    def _return_cves(tx, message):
        result = tx.run("match (p:CPE)-[r:MatchingCVE]->(v:CVE) \
            where p.name = $message \
            return v.Name", message=message)
        entire_result = [] # Will contain all the items
        for record in result:
            entire_result.append(record)
        return entire_result
        

greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "threat")

cwes = greeter.cwe_test('cpe:a:google:chrome:*:*')
cwes_output = []

for i in range(len(cwes)):
    cwes_output.append([cwes[i][0], cwes[i][1]])

df = pd.DataFrame(cwes_output,columns =['CWE-ID', 'Name'])
df_merged = df.groupby(['CWE-ID']).size().reset_index(name='counts').sort_values('counts', ascending=False)
print(df_merged .head())

greeter.close()
