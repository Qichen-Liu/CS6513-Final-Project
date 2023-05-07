import pandas as pd

df = pd.read_csv('industry_GDP.csv')
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

industry = ['All industries', 'Construction', 'Air transportation', 'Rail transportation',
            'Transit and ground passenger transportation', 'Computer systems design and related services',
            'Miscellaneous professional, scientific, and technical services', 'Accommodation and food services']

dfs = []

for index, row in df.iterrows():
    if row[1] in industry:
        d = {'Industry': row[1], '2019 Q1': row[2], '2019 Q2': row[3],
             '2019 Q3': row[4], '2019 Q4': row[5], '2020 Q1': row[6],
             '2020 Q2': row[7], '2020 Q3': row[8], '2020 Q4': row[9],
             '2021 Q1': row[10], '2021 Q2': row[11], '2021 Q3': row[12],
             '2021 Q4': row[13], '2022 Q1': row[14], '2022 Q2': row[15],
             '2022 Q3': row[16], '2022 Q4': row[17]}
        dfs.append(d)

df = pd.DataFrame(dfs).transpose().reset_index()
df.columns = df.iloc[0]
df = df.drop(0).reset_index(drop=True)
df = df.rename(columns={'Industry': 'Date', 'Accommodation and food services': 'Hospitality'})

df['All industries'] = pd.to_numeric(df['All industries'])
df['Construction'] = pd.to_numeric(df['Construction'])
df['Hospitality'] = pd.to_numeric(df['Hospitality'])
df['Air transportation'] = pd.to_numeric(df['Air transportation'])
df['Rail transportation'] = pd.to_numeric(df['Rail transportation'])
df['Transit and ground passenger transportation'] = pd.to_numeric(df['Transit and ground passenger transportation'])
df['Computer systems design and related services'] = pd.to_numeric(df['Computer systems design and related services'])
df['Miscellaneous professional, scientific, and technical services'] = pd.to_numeric(df['Miscellaneous professional, scientific, and technical services'])
df['Travelling'] = df['Air transportation'] + df['Rail transportation'] + df['Transit and ground passenger transportation']
df['Technology'] = df['Computer systems design and related services'] + df['Miscellaneous professional, scientific, and technical services']

df = df.drop(['Air transportation', 'Rail transportation', 'Transit and ground passenger transportation', 'Computer systems design and related services', 'Miscellaneous professional, scientific, and technical services'], axis=1)
df.to_excel('cleaned_gdp.xlsx', index=False)

