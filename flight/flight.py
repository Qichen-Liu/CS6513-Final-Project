import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as pyo

flights = pd.read_excel("combined_flight.xlsx")
print(flights)

fig = go.Figure(go.Scatter(
    x = flights["month_year"],
    y = flights["PASSENGERS"]
))

fig.update_layout(
    title='New YorK City flight passenger by month',
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.5,
        dtick = 0.75,
        title = "Passenger"
    ),
    yaxis = dict(
        title = "Month"
    )
)

fig.show()
pyo.plot(fig, filename='New YorK City flight passenger by month.html')