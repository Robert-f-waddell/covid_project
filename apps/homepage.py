import plotly.express as px
from datetime import datetime as dt
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from app import app
covid_df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
covid_df = covid_df[["iso_code",
                    "continent",
                     "location",
                     "date",
                     "total_cases",
                    "new_cases",
                    "new_cases_smoothed",
                    "total_deaths",
                    "new_deaths",
                    "new_deaths_smoothed",]]
covid_df = covid_df[covid_df["total_cases"].notna()]
covid_df1 = covid_df[covid_df["iso_code"] = "OWID_WRL"]

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='two columns div-user-controls',
                             children=[
                                 html.H2('Coronavirus Dashboard'),
                                 html.P('Homepage'),
                                 html.P('A coronavirus dashboard made using Dash - Plotly'),
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Graph(id='graph5')
                                    
                             ])
                              ])
        ]

)

# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     [Input('year-slider', 'value')])

def update_global2():


   fig = px.line(covid_df1, x="date", y="total_cases", title='Total Global Cases of Covid-19')

    fig.update_layout(height = 650,
                      width = 900,
                      template = "plotly_dark")
    return fig
