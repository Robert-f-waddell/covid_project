
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
covid_df['m_date'] = pd.to_datetime(covid_df["date"], format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m'))
covid_df = covid_df[covid_df["iso_code"] != "OWID_WRL"]
months = covid_df.m_date.unique()
months.sort()
monthsdict ={}
i=0
for m in months:
    i=i+1
    monthsdict[i] = str(m)

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='two columns div-user-controls',
                             children=[
                                 html.H2('Coronavirus Global Statistics'),
                                 html.P('Visualising Coronavirus statistcs for the selected country with Plotly - Dash.'),
                                 
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Graph(id='graph-with-slider'),
                                    dcc.Slider(
                                        id='year-slider',
                                        min=1,
                                        max=len(monthsdict),
                                        value=3,
                                        step=None,
                                        marks = monthsdict
                                        
                                    )
                             ])
                              ])
        ]

)

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])

def update_global2(mno):
    test=covid_df[covid_df["m_date"]==monthsdict[mno]].sort_values(by="date")
    covid_df_year = test[test["date"]==test["date"].min()]
    
    
    
    
    
    
    for col in covid_df_year.columns:
        covid_df_year[col] = covid_df_year[col].astype(str)


    # covid_df_year["text"] = covid_df_year["location"]+ '<br>' + \
    #                         "Total_Cases: "+ covid_df_year["total_cases"]+ '<br>' + \
    #                         "Total_Deaths: "+ covid_df_year["total_deaths"]



    fig = go.Figure(data=go.Choropleth(
        locations = covid_df_year['iso_code'],
        z = covid_df_year['total_cases'],
        colorscale = 'PuBu',
        autocolorscale=True,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.1,
        text= covid_df_year["location"]+ '<br>' + \
                            "Total Deaths: "+ covid_df_year["total_deaths"],
        colorbar_title = 'Total Cases',
    ))

    fig.update_layout(height = 650,
                      width = 900,
                      template = "plotly_dark",
      
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular',
            bgcolor = "rgb(30,30,30)"
        )
        )


    return fig
