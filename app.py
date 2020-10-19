import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')
