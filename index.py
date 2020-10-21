import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2, app3
from app import server


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Global Statistics| ', href='/apps/app1'),
        dcc.Link('National Statistics| ', href='/apps/app2'),
        dcc.Link('National Statistics v2', href='/apps/app3')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/app3':
         return app3.layout
    else:
        return ""


if __name__ == '__main__':
    app.run_server(debug=False)
