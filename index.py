import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2,app3, homepage
from app import server
# covid_df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
# covid_df = covid_df[["iso_code",
#                     "continent",
#                      "location",
#                      "date",
#                      "total_cases",
#                     "new_cases",
#                     "new_cases_smoothed",
#                     "total_deaths",
#                     "new_deaths",
#                     "new_deaths_smoothed",]]
# covid_df = covid_df[covid_df["total_cases"].notna()]



# layout for the navigation bar at the top
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link(html.Button('Homepage'), href='/apps/homepage'),
        dcc.Link(html.Button('Global Statistics'), href='/apps/app1'),
        dcc.Link(html.Button('National Statistics'), href='/apps/app2'),
        dcc.Link(html.Button('National Statistics v2'), href='/apps/app3'),
        dcc.Link(html.Button('Link to Github Repository'), href='https://github.com/Robert-f-waddell/covid_project')
    ], className="row"),
    html.Div(id='page-content', children=[])
])

# callback allowing you to navigate between app pages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])


def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/app3':
         return app3.layout
    elif pathname == '/apps/homepage':
         return homepage.layout
    else:
        return homepage.layout


if __name__ == '__main__':
    app.run_server(debug=False)
