
  
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

from app import app

app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('Second page'),
                                 html.P('Coronavirus dashboard using dash - plotly.'),
                                 html.Div(id='app-1-display-value'),
                                dcc.Link('Go to App 2', href='/apps/app2')
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey')
                              ])
        ]

)
