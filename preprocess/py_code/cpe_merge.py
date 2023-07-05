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
