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






layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('Coronavirus Dashboard'),
                                 html.P('Homepage'),
                                  html.Div(id='app-1-display-value')
                                 
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Checklist(id='stat-select2',
                                                       options=[{'label': 'Total Cases', 'value': 'total_cases'},
                                                                {'label': 'Total Deaths', 'value': 'total_deaths'},
                                                                {'label': 'Daily Cases', 'value': 'new_cases'},
                                                                {'label': 'Daily Deaths', 'value': 'new_deaths'}],
                                                        value=["total_cases","total_deaths"],
                                                       labelStyle={'display': 'inline-block'},
                                                       style={"color": "white"}
                                                      ),
                                 dcc.Graph('country statistics3', config={'displayModeBar': False})
                             ],style={'color': '#1E1E1E'}),
                     
                              ])
        ]

)
       
@app.callback(
    Output('country statistics3', 'figure'),
    [Input("stat-select2","value")]
    
)
        

        
def update_graph(stat):  
   
  
#     stat= ["total_cases","total_deaths"]

    
    
    
    # Create figure
    fig = go.Figure()

    
    for i in stat:
            fig.add_trace(
            go.Scatter(x=covid_df["date"][covid_df["location"]=="World"], y=covid_df[i][covid_df["location"]=="World"],
            name=i))

        # Set title
    fig.update_layout(
        title_text="Global Covid-19 Statistics"
    )

    # Add range slider
    fig.update_layout(height=700,
                      width=900,
                      template = 'plotly_dark',
                      plot_bgcolor='rgb(30,30,30)',
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
                ]),
              bgcolor = 'rgb(30,30,30)'
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

#     print(stat)
    return fig
