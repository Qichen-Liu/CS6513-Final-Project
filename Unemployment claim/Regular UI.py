import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime
import warnings
import json
from datetime import datetime

total = 2789427
regularUI = {
    "Accommodation & Food Services": 380954,
    "Health Care & Social Assistance": 371906,
    "Retail Trade": 311175,
    "Administrative & Support Services": 264526,
    "Construction": 213141,
    "Unclassified": 197304,
    "Professional, Scientific & Technical Services": 123311,
    "Information":74473
}
# Calculate the sum of the values in the regularUI dictionary
regularUI_sum = sum(regularUI.values())


# Calculate the amount for the 'Other' category
other_category_amount = total - regularUI_sum

# Add the 'Other' category to the regularUI dictionary
regularUI["Other"] = other_category_amount

# Create a pie chart using Plotly
fig = go.Figure(data=[go.Pie(labels=list(regularUI.keys()), values=list(regularUI.values()),
                             hoverinfo='label+value', textinfo='label+percent',
                             textfont=dict(size=16))])

# Customize the layout of the pie chart
fig.update_layout(
    title_text="UI Claims by Industry",
    title_font_family="Arial",
    title_font_size=22,
    title_font_color="black",
    title_x=0.5,
)

fig.write_html("UI Claims by Industry.html")

# Display the pie chart
fig.show()
