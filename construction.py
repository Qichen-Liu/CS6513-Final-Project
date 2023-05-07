import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime
import warnings
import json
from datetime import datetime


covid_start = datetime(2019, 10, 1)
covid_end = datetime(2022, 12, 31)
chunksize = 10**4  # Adjust this value based on your system's memory
chunks = []

for chunk in pd.read_csv("DOB_Permit_Issuance.csv", chunksize=chunksize):
    # Process each chunk, apply filters, and append to the list
    chunk['Job Start Date'] = pd.to_datetime(chunk['Job Start Date'], errors='coerce')
    chunk_filtered = chunk[(chunk['Job Type'] == 'NB') & (chunk['Filing Status'] == 'INITIAL') &
                           (chunk['Job Start Date'] > covid_start) & (chunk['Job Start Date'] < covid_end)]
    chunks.append(chunk_filtered)

# Concatenate all the filtered chunks into a single DataFrame
DOB_Permit_Issuance_cleaned = pd.concat(chunks)

writer = pd.ExcelWriter('DOB_Permit_Issuance_cleaned.xlsx', engine='xlsxwriter')
DOB_Permit_Issuance_cleaned.to_excel(writer, index=False)
writer.save()

# Load the cleaned DataFrame from the Excel file
DOB_Permit_Issuance_cleaned = pd.read_excel("DOB_Permit_Issuance_cleaned.xlsx")

# Select the two columns you want to keep
selected_columns = ['Job Start Date', 'Job doc. #']
DOB_Permit_Issuance_cleaned = DOB_Permit_Issuance_cleaned[selected_columns]

# Group the DataFrame by 'Job Start Date' and sum the 'Job doc. #' values for each group
DOB_Permit_Issuance_cleaned = DOB_Permit_Issuance_cleaned.groupby('Job Start Date')['Job doc. #'].sum().reset_index()

fig2 = px.scatter(DOB_Permit_Issuance_cleaned, x="Job Start Date", y="Job doc. #", trendline="lowess", trendline_options=dict(frac=0.1))
fig2.update_layout(
    title_text='DOB_Permit_Issuance_cleaned',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
)
fig2.write_html("DOB_Permit_Issuance_cleaned.html")

DOB_Permit_Issuance_cleaned_cum = DOB_Permit_Issuance_cleaned
# Make the 'Job doc. #' column cumulative
DOB_Permit_Issuance_cleaned_cum['Job doc. #'] = DOB_Permit_Issuance_cleaned['Job doc. #'].cumsum()

print(DOB_Permit_Issuance_cleaned)

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=DOB_Permit_Issuance_cleaned_cum['Job Start Date'], y=DOB_Permit_Issuance_cleaned_cum['Job doc. #'] , name="DOB_Permit_Issuance_cleaned_cumulative",
                             line_shape='linear'))
fig1.update_traces(mode="markers+lines")
fig1.update_layout(
    title_text='DOB_Permit_Issuance_cleaned_cumulative',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
)
fig1.write_html("DOB_Permit_Issuance_cleaned_cumulative.html")

fig1.show()

fig2.show()
