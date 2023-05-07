import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime
import warnings
import json
from datetime import datetime
get_food_2020 = pd.read_excel("EFD_Metrics_2020_YEAR_END.xlsx")
get_food_2021 = pd.read_excel("EFD_Metrics_2021_YEAR_TO_DATE.xlsx")
get_food_2020 = get_food_2020[['MONTH', 'TOTAL MEALS']]
monthly_totals = get_food_2020.groupby("MONTH")["TOTAL MEALS"].sum()

get_food_2020_cleaned = {}

for month, total_meals in monthly_totals.items():
    get_food_2020_cleaned[month] = total_meals

month_number_mapping = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

sorted_monthly_totals = monthly_totals.sort_index(key=lambda x: x.map(lambda month_year: (int(month_year[-4:]), month_number_mapping[month_year[:3]])))

sorted_monthly_totals_df = sorted_monthly_totals.reset_index()
sorted_monthly_totals_df.columns = ['Month', 'Total Meals']

get_food_2021 = get_food_2021[['Month Starting', 'Total Meals']]

# Replace 'Sept' with 'Sep' in the 'Month' column
sorted_monthly_totals_df['Month'] = sorted_monthly_totals_df['Month'].str.replace('Sept', 'Sep')

# Convert 'Month' column in sorted_monthly_totals_df to 'YYYY-MM' format
sorted_monthly_totals_df['Month'] = pd.to_datetime(sorted_monthly_totals_df['Month'], format='%b %Y').dt.strftime('%Y-%m')

# Rename the 'Month Starting' column to 'Month' and convert to 'YYYY-MM' format
get_food_2021 = get_food_2021.rename(columns={'Month Starting': 'Month'})
get_food_2021['Month'] = pd.to_datetime(get_food_2021['Month']).dt.strftime('%Y-%m')

# Merge the two DataFrames
merged_data = pd.concat([sorted_monthly_totals_df, get_food_2021], ignore_index=True)

# Sort the merged_data DataFrame by the 'Month' column
merged_data_sorted = merged_data.sort_values(by='Month')

print(merged_data_sorted)

fig = go.Figure()
fig.add_trace(go.Scatter(x=merged_data_sorted['Month'], y=merged_data_sorted['Total Meals'] , name="DOB_Permit_Issuance_cleaned",
                             line_shape='linear'))
fig.update_traces(mode="markers+lines")
fig.update_layout(
    title_text='GetFood Food Delivery order by mouth',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
)
fig.write_html("GetFood Food Delivery order by mouth.html")
fig.show()