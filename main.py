import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, dcc
import plotly.graph_objects as go
import plotly.express as px


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
df = px.data.stocks()
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Styling using html components', style={'textAlign': 'center', \
                                                                      'marginTop': 40, 'marginBottom': 40}),

    #dcc.Graph(id='line_plot', figure=stock_prices())
]
                      )