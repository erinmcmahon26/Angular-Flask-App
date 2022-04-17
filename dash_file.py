import sys
print(sys.executable)

#import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, dcc
import plotly.graph_objects as go
import plotly.express as px


app = dash.Dash()
df = px.data.stocks()
server = app.server
#app.config.suppress_callback_exceptions = True

app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Wow this is hard...', style={'textAlign': 'center', \
                                                                      'marginTop': 40, 'marginBottom': 40}),

    #dcc.Graph(id='line_plot', figure=stock_prices())
]
                      )

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080, use_reloader=False)