import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2
from app import server

app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(dcc.Location(id='url', refresh=False),
                             className='four columns div-user-controls',
                             children=[
                                 html.H2('Home page'),
                                 html.P('Coronavirus dashboard using dash - plotly.'),
                                 html.Div(id='page-content'),
                                dcc.Link('Go to App 1', href='/apps/app1'),
                                dcc.Link('Go to App 2', href='/apps/app2') 
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey')
                              ])
        ]

)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
