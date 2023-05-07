import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime
import warnings

#New youk city covid-19 cases by day
df_CBD_NYC = pd.read_csv("cases-by-day.csv")

fig = go.Figure()
data = df_CBD_NYC
data['CASE_COUNT'].astype('float')

fig.add_trace(go.Scatter(x=data['date_of_interest'], y=data['CASE_COUNT'], name="cases by day",
                             line_shape='linear'))
fig.update_traces(mode="markers+lines")
fig.update_layout(
    title_text='cases by day',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
)
fig.write_html("New youk city covid-19 cases by day.html")

fig.show()

# All Employees: Total Nonfarm in New York City, NY 
df_ETN_NYC = pd.read_excel("SMS36935610000000001.xls")
df_ETN_NYC = df_ETN_NYC[10:]
df_ETN_NYC.columns = ['Date', 'Employees']
writer = pd.ExcelWriter('Employees_Total_Nonfarm_NYC.xlsx', engine='xlsxwriter')
df_ETN_NYC.to_excel(writer, index=False)
writer.save()

df_ETN_NYC = pd.read_excel("Employees_Total_Nonfarm_NYC.xlsx")

fig = go.Figure()
data = df_ETN_NYC
data = data.sort_values(by=['Date'])
# data['Date'] = data['Date'].dt.strftime("0000-%m-%d %H:%M")
data['Employees'].astype('float')

fig.add_trace(go.Scatter(x=data['Date'], y=data['Employees'], name="Employees_Total_Nonfarm",
                             line_shape='linear'))
fig.update_traces(mode="markers+lines")
fig.update_layout(
    title_text='Employees_Total_Nonfarm',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
)
fig.write_html("Employees_Total_Nonfarm_NYC.html")

fig.show()

#Total Personal Income in New York
df_TPI_NY = pd.read_excel("NYOTOT.xls")
df_TPI_NY = df_TPI_NY[10:]
df_TPI_NY.columns = ['Date', 'Income']
writer = pd.ExcelWriter('total_personal_income_NY.xlsx', engine='xlsxwriter')
df_TPI_NY.to_excel(writer, index=False)
writer.save()

df_TPI_NY = pd.read_excel("total_personal_income_NY.xlsx")

fig = go.Figure()
data = df_TPI_NY
data = data.sort_values(by=['Date'])
# data['Date'] = data['Date'].dt.strftime("0000-%m-%d %H:%M")
data['Income'].astype('float')

fig.add_trace(go.Scatter(x=data['Date'], y=data['Income'], name="total_personal_income_NY",
                             line_shape='linear'))
fig.update_traces(mode="markers+lines")
fig.update_layout(
    title_text='total_personal_income_NY',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
)
fig.write_html("total_personal_income_NY.html")

fig.show()

#Average Hourly Earnings of All Employees: Total Private in New York City
df_AHE_NYC = pd.read_excel("SMU36935610500000003.xls")
df_AHE_NYC = df_AHE_NYC[10:]
df_AHE_NYC.columns = ['Date', 'Income']
writer = pd.ExcelWriter('Average_Hourly_Earning_NYC.xlsx', engine='xlsxwriter')
df_AHE_NYC.to_excel(writer, index=False)
writer.save()

df_AHE_NYC = pd.read_excel("Average_Hourly_Earning_NYC.xlsx")

fig = go.Figure()
data = df_AHE_NYC
data = data.sort_values(by=['Date'])
# data['Date'] = data['Date'].dt.strftime("0000-%m-%d %H:%M")
data['Income'].astype('float')

fig.add_trace(go.Scatter(x=data['Date'], y=data['Income'], name="Average_Hourly_Earning_NYC",
                             line_shape='linear'))
fig.update_traces(mode="markers+lines")
fig.update_layout(
    title_text='Average_Hourly_Earning_NYC',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,
)
fig.write_html("Average_Hourly_Earning_NYC.html")

fig.show()