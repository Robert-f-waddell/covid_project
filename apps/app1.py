
  
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

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
covid_df['m_date'] = pd.to_datetime(covid_df["date"], format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m'))



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
                    html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                 dcc.Graph(id='graph-with-slider'),
                                    dcc.Slider(
                                        id='year-slider',
                                        min=covid_df['m_date'].min(),
                                        max=covid_df['m_date'].max(),
                                        value=covid_df['m_date'].max(),
                                        marks={str(month): str(month) for month in covid_df['m_date'].unique()},
                                        step=None
                                    )
                             ])
                              ])
        ]

)

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])

def update_figure(selected_month):  
    covid_df_year = covid_df[covid_df["m_date"]==selected_month]

    for col in covid_df_year.columns:
        covid_df_year[col] = covid_df_year[col].astype(str)


        fig = go.Figure(data=go.Choropleth(
        locations = covid_df_year['iso_code'],
        z = covid_df_year['total_cases'],
        colorscale = 'plasma',
        autocolorscale=True,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.1,
        text= covid_df_year["location"]+ '<br>' + \
                            "Total Deaths: "+ covid_df_year["total_deaths"],
        colorbar_title = 'Total Cases',
    ))

    fig.update_layout(height=800, width=800,
        title_text='Global Map',
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular'))

    return fig
