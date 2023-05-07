import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime
import warnings
import json
from datetime import datetime
vaccination_cut = pd.read_excel("vaccination_cut.xlsx")

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=vaccination_cut['Report as of'], y=vaccination_cut['Series Complete'], name="Total vaccination per day",
                             line_shape='linear'))

fig1.update_traces(mode="markers+lines")
fig1.update_layout(
    title_text='Total vaccination per day',
    title_font_family="Times New Roman",
    title_font_size=22,
    title_font_color="black",
    title_x=0.45,

)
fig1.write_html("Total vaccination per day.html")

# Show the plot
fig1.show()