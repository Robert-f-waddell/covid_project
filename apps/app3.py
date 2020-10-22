import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from app import app


covid_df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
covid_df = covid_df[["continent",
                     "location",
                     "date",
                     "total_cases",
                    "new_cases",
                    "new_cases_smoothed",
                    "total_deaths",
                    "new_deaths",
                    "new_deaths_smoothed",]]

covid_df = covid_df[covid_df["total_cases"].notna()]


country_names =covid_df.location.unique()
country_names.sort()

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('Coronavirus National Statistics'),
                                 html.P('Visualising Coronavirus statistcs for the selected country with Plotly - Dash.'),
                                  html.Div(id='app-1-display-value'),
                                  html.Div(
                                     className='div-for-checklist',
                                     children=[
                                         dcc.Checklist(id='stat-select',
                                                       options=[{'label': 'Total Cases', 'value': 'total_cases'},
                                                                {'label': 'Total Deaths', 'value': 'total_deaths'},
                                                                {'label': 'Daily Cases', 'value': 'new_cases'},
                                                                {'label': 'Daily Deaths', 'value': 'new_deaths'}],
                                                        value=["total_cases","total_deaths"],
                                                       labelStyle={'display': 'inline-block'}
                                                      ),
                                     ],
                                     style={'color': '#1E1E1E'}),
                                 html.Div(
                                     className='div-for-dropdown',
                                     children=[
                                         dcc.Dropdown(id='group-select2', options=[{'label': i, 'value': i} for i in country_names],
                                           multi=True,value='France', style={'backgroundColor': '#1E1E1E'}
                                                      ),
                                     ],
                                     style={'color': '#1E1E1E'})
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Graph('country statistics2', config={'displayModeBar': False})
                             ])
                              ])
        ]

)
       
@app.callback(
    Output('country statistics2', 'figure'),
    [Input('group-select2', 'value'),
    Input("stat-select","value")]
    
)
        

        
def update_graph(name,stat):  
   
  
#     stat= ["total_cases","total_deaths"]

    Cname=[]
    del Cname[:]
    if type(name) == str:
        Cname.append(name)
    else:
        Cname.extend(name)
    
    
    
    # Create figure
    fig = go.Figure()

    
    for j in Cname:
        for i in stat:
            fig.add_trace(
            go.Scatter(x=covid_df["date"][covid_df["location"]==j], y=covid_df[i][covid_df["location"]==j],
            name=j +" "+ i))

        # Set title
    fig.update_layout(
        title_text="Time series with range slider and selectors"
    )

    # Add range slider
    fig.update_layout(height=600,
                      width=800,
                      template = 'plotly_dark',
                      colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

#     print(stat)
    return fig
