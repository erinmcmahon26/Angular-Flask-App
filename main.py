# from flask import Flask
# from flask_restful import Api
from dash import Dash, dcc, html, Input, Output
from google.cloud import bigquery
import plotly
import plotly.express as px

# app = Flask(__name__)
# api = Api(app)
app = Dash(__name__)
# constructing a BQ client object
client = bigquery.Client()

query = """
    SELECT *
    FROM ML.EXPLAIN_FORECAST(MODEL worldpop.yearly_pop,
            STRUCT(10 AS horizon, 0.8 AS confidence_level))
"""

query_job = client.query(query) # make an API request

df = query_job.to_dataframe()
#json_object = df.to_json(orient='records')
fig = px.line(df, x='time_series_timestamp', y ='time_series_data', title = 'World Population')

app.layout = html.Div(children = [
    html.H1("World Population Forcast"),
    html.Div(children ='''An app to see what the expected world population will be each year over the next 10 years.'''),
    dcc.Graph(
        id = 'World Population Graph',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port =8080, debug=True)

# @app.route('/', methods=['GET'])
# def query():
#     response = fig
#     return response

