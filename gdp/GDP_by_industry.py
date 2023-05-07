import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as pyo

cleaned_gdp = pd.read_excel("cleaned_gdp.xlsx")
print(cleaned_gdp)

#All = go.Scatter(x=cleaned_gdp['Date'], y=cleaned_gdp['All industries'], mode='markers+lines', name='All',)
Construction = go.Scatter(x=cleaned_gdp['Date'], y=cleaned_gdp['Construction'], mode='markers+lines', name='Construction',)
Hospitality = go.Scatter(x=cleaned_gdp['Date'], y=cleaned_gdp['Hospitality'], mode='markers+lines', name='Hospitality',)
Travelling = go.Scatter(x=cleaned_gdp['Date'], y=cleaned_gdp['Travelling'], mode='markers+lines', name='Travelling',)
Technology = go.Scatter(x=cleaned_gdp['Date'], y=cleaned_gdp['Technology'], mode='markers+lines', name='Technology',)

layout = go.Layout(
    title='GDP growth by industry',
    xaxis=dict(title='Time'),
    yaxis=dict(title='GDP')
)

# Combine the traces and layout
fig = go.Figure(data=[Construction,Hospitality, Travelling,Technology], layout=layout)
#fig = go.Figure(data=[All, Construction,Hospitality, Travelling,Technology], layout=layout)

fig.show()
pyo.plot(fig, filename='GDP growth by industry.html')