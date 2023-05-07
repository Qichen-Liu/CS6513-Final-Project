import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime
import warnings
import json
from datetime import datetime

trips  = pd.read_csv("data_reports_monthly.csv")

trips = trips[['Month/Year','License Class', 'Trips Per Day']]
trips['Month/Year'] = pd.to_datetime(trips['Month/Year'])
trips['Trips Per Day'] = trips['Trips Per Day'].str.replace(',', '').astype(float)
trips = trips[trips['Month/Year'].dt.year >= 2019]

FHV = trips[~trips['License Class'].isin(["Yellow","Green"])]
Yellow = trips[trips['License Class'] == "Yellow"]
Green = trips[trips['License Class'] == "Green"]

# Filter the data for the years after 2015

FHV = FHV.sort_values(by='Month/Year')
Yellow = Yellow.sort_values(by='Month/Year')
Green = Green.sort_values(by='Month/Year')
FHV =  FHV.groupby('Month/Year')['Trips Per Day'].sum().reset_index()

flight = pd.read_excel("combined_flight.xlsx")
flight["month_year"] = pd.to_datetime(flight["month_year"], format="%b %Y").dt.strftime("%Y-%m")

print(flight)
# fig1 = go.Figure()

# fig1.update_traces(mode="markers+lines")

# fig1.write_html("trips per day.html")
#
# # Show the plot
# fig1.show()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=FHV['Month/Year'], y=FHV['Trips Per Day'], name="FHV trips per day",
                             line_shape='linear'))
fig1.add_trace(go.Scatter(x=Yellow['Month/Year'], y=Yellow['Trips Per Day'], name="Yellow trips per day",
                             line_shape='linear'))
fig1.add_trace(go.Scatter(x=Green['Month/Year'], y=Green['Trips Per Day'], name="Green trips per day",
                             line_shape='linear'))
fig1.update_layout(
    title_text='NYC Taxi trips per month',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,

)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=flight['month_year'], y=flight['PASSENGERS'], name="FHV trips per day",
                             line_shape='linear'))
fig2.update_layout(
    title_text='Flight passenger per month',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,

)

# Create a subplot with 1 row and 2 columns
combined = sp.make_subplots(rows=2, cols=1, subplot_titles=('NYC Taxi trips per month', 'Flight passenger per month'))

# Add the traces to the subplot
combined.add_trace(fig1['data'][0], row=1, col=1)
combined.add_trace(fig1['data'][1], row=1, col=1)
combined.add_trace(fig1['data'][2], row=1, col=1)
combined.add_trace(fig2['data'][0], row=2, col=1)

combined.show()
combined.write_html("co-relation flight-taxi tip.html")