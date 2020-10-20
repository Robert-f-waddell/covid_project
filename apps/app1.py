
  
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

from app import app

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('Global Statistics'),
                                 html.P('Coronavirus dashboard using dash - plotly.'),
                                 html.Div(id='app-1-display-value')
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey')
                              ])
        ]

)
