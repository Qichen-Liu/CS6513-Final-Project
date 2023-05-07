# https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FIL&QO_fu146_anzr=Nv4%20Pn44vr45
import pandas as pd
import matplotlib.pyplot as plt

df2019 = pd.read_csv('T_T100D_MARKET_US_CARRIER_ONLY 2019.csv')
df2020 = pd.read_csv('T_T100D_MARKET_US_CARRIER_ONLY 2020.csv')
df2021 = pd.read_csv('T_T100D_MARKET_US_CARRIER_ONLY 2021.csv')
df2022 = pd.read_csv('T_T100D_MARKET_US_CARRIER_ONLY 2022.csv')
df2023 = pd.read_csv('T_T100D_MARKET_US_CARRIER_ONLY 2023.csv')

filtered_df2019 = df2019.loc[(df2019['DEST_CITY_NAME'] == 'New York, NY') & (df2019['PASSENGERS'] != 0)]
filtered_df2020 = df2020.loc[(df2020['DEST_CITY_NAME'] == 'New York, NY') & (df2020['PASSENGERS'] != 0)]
filtered_df2021 = df2021.loc[(df2021['DEST_CITY_NAME'] == 'New York, NY') & (df2021['PASSENGERS'] != 0)]
filtered_df2022 = df2022.loc[(df2022['DEST_CITY_NAME'] == 'New York, NY') & (df2022['PASSENGERS'] != 0)]
filtered_df2023 = df2023.loc[(df2023['DEST_CITY_NAME'] == 'New York, NY') & (df2023['PASSENGERS'] != 0)]

grouped_df2019 = filtered_df2019.sort_values(by=['MONTH'])
grouped_df2020 = filtered_df2020.sort_values(by=['MONTH'])
grouped_df2021 = filtered_df2021.sort_values(by=['MONTH'])
grouped_df2022 = filtered_df2022.sort_values(by=['MONTH'])
grouped_df2023 = filtered_df2023.sort_values(by=['MONTH'])

aggregations = {
    'PASSENGERS': 'sum',
    'YEAR': 'first',  # sum the 'attribute' column
    'MONTH': 'first'
}

grouped_df2019 = grouped_df2019.groupby('MONTH').aggregate(aggregations).drop('MONTH', axis=1).reset_index()
grouped_df2020 = grouped_df2020.groupby('MONTH').aggregate(aggregations).drop('MONTH', axis=1).reset_index()
grouped_df2021 = grouped_df2021.groupby('MONTH').aggregate(aggregations).drop('MONTH', axis=1).reset_index()
grouped_df2022 = grouped_df2022.groupby('MONTH').aggregate(aggregations).drop('MONTH', axis=1).reset_index()
grouped_df2023 = grouped_df2023.groupby('MONTH').aggregate(aggregations).drop('MONTH', axis=1).reset_index()

# grouped_df2019.to_excel('flight_2019.xlsx', index=False)
# grouped_df2020.to_excel('flight_2020.xlsx', index=False)
# grouped_df2021.to_excel('flight_2021.xlsx', index=False)
# grouped_df2022.to_excel('flight_2022.xlsx', index=False)
# grouped_df2023.to_excel('flight_2023.xlsx', index=False)

dfs = []
dfs.append(grouped_df2019)
dfs.append(grouped_df2020)
dfs.append(grouped_df2021)
dfs.append(grouped_df2022)
dfs.append(grouped_df2023)

combined_df = pd.concat(dfs, axis=0, ignore_index=True)
combined_df['date'] = pd.to_datetime(combined_df['YEAR'].astype(str) + combined_df['MONTH'].astype(str), format='%Y%m')
combined_df['month_year'] = combined_df['date'].dt.strftime('%b %Y')
combined_df = combined_df.loc[:, ['PASSENGERS', 'month_year']]

ax = combined_df.plot(x='month_year', y='PASSENGERS', kind='line')

# Add labels and title
ax.set_xlabel('Date', labelpad=10)
ax.set_ylabel('Number of passengers')
ax.set_title('Passengers flew to New York City')
plt.subplots_adjust(bottom=0.15)

plt.savefig('NYC_flight.png', dpi=300)

combined_df.to_excel('combined_flight.xlsx', index=False)