import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime
import warnings
import json
from datetime import datetime

# Read the data from the specific sheet
wfh_full_paid_day = pd.read_excel("WFHtimeseries_monthly.xlsx", sheet_name=1)

# Convert the 'date' column to pandas datetime format
wfh_full_paid_day['date'] = pd.to_datetime(wfh_full_paid_day['date'])

# Filter the data for the years after 2015
wfh_full_paid_day_after_2015 = wfh_full_paid_day[wfh_full_paid_day['date'].dt.year > 2015]
wfh_full_paid_day_after_2015 = wfh_full_paid_day_after_2015[['date', 'WFH_share']]
wfh_full_paid_day_after_2015['date'] = wfh_full_paid_day['date'].dt.strftime('%Y-%m-%d')
wfh_full_paid_day_after_2015_before_2020 = wfh_full_paid_day_after_2015[:4]
wfh_full_paid_day_after_after_2020 = wfh_full_paid_day_after_2015[4:]
print(wfh_full_paid_day_after_2015_before_2020)
# Create a histogram using Plotly
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=wfh_full_paid_day_after_after_2020['date'], y=wfh_full_paid_day_after_after_2020['WFH_share'], name="WFH Full pay day percentage",
                             line_shape='linear'))
fig1.update_traces(mode="markers+lines")
fig1.update_layout(
    title_text='WFH Full pay day percentage',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
    yaxis=dict(range=[0, 100])
)
fig1.write_html("WFH Full pay day percentage.html")

# Show the plot
fig1.show()

fig2 = px.histogram(wfh_full_paid_day_after_2015_before_2020, x='date', y='WFH_share', nbins=16, title='WFH full pay day histogram before Covid')
fig2.write_html("WFH Full pay day percentage before Covid.html")
# Show the plot
fig2.show()

wfh_full_paid_day_nyc = pd.read_excel("WFHtimeseries_monthly.xlsx", sheet_name=6)
wfh_full_paid_day_nyc = wfh_full_paid_day_nyc[['date', 'wfhcovid_series_MA6_NewYork']]
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=wfh_full_paid_day_nyc['date'], y=wfh_full_paid_day_nyc['wfhcovid_series_MA6_NewYork'], name="WFH full pay day percentage - New York City",
                             line_shape='linear'))
fig3.update_traces(mode="markers+lines")
fig3.update_layout(
    title_text='WFH Full pay day percentage',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
    yaxis=dict(range=[0, 100])
)
fig3.write_html("WFH Full pay day percentage - New York City.html")

# Show the plot
fig3.show()