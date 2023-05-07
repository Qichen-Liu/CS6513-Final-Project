import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('New_York_State_Statewide_COVID-19_Vaccination_Data_by_County.csv')
filtered_df = df.loc[df['Region'] == 'New York City'].copy()  # make a copy to avoid modifying original DataFrame
filtered_df.loc[:, 'Report as of'] = pd.to_datetime(filtered_df['Report as of'], format='%m/%d/%y')  # use .loc to modify original DataFrame

aggregations = {
    'Region': 'first',
    'Series Complete': 'sum',  # sum the 'attribute' column
    'Report as of': 'first'
}

group_df = filtered_df.groupby('Report as of').aggregate(aggregations)
group_df = group_df.drop('Report as of', axis=1).reset_index()
group_df = group_df.sort_values(by=['Report as of'])

ax = group_df.plot(x='Report as of', y='Series Complete', kind='line')

# Add labels and title
ax.set_xlabel('Date', labelpad=10)
ax.set_ylabel('Number of Completed Series')
ax.set_title('COVID-19 Vaccination in New York City')
plt.subplots_adjust(bottom=0.15)


plt.savefig('NYC_vaccine.png', dpi=300)

# Save the filtered DataFrame to a new Excel file
group_df.to_excel('vaccination_cut.xlsx', index=False)


# construction, food delivery, tech, service
