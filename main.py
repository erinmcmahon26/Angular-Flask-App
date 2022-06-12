import dash
from dash import dcc, html
from google.cloud import bigquery
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

# constructing a BQ client object
client = bigquery.Client()

query = """
    SELECT *
    FROM ML.EXPLAIN_FORECAST(MODEL worldpop.yearly_pop,
            STRUCT(10 AS horizon, 0.8 AS confidence_level))
"""

query_job = client.query(query) # make an API request

df = query_job.to_dataframe()

fig = px.line(df, x='time_series_timestamp', y ='time_series_data')

app.layout = html.Div(children = [
    html.H1("World Population Forcast"),
    html.Div(children ='''An app to see what the expected world population will be each year over the next 10 years.'''),
    dcc.Graph(
        id = 'World Population Graph',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)

# from flask import Flask
# from flask_restful import Api
# from google.cloud import bigquery
#
# app = Flask(__name__)
# api = Api(app)
#
# # constructing a BQ client object
# client = bigquery.Client()
#
# query = """
#     SELECT *
#     FROM ML.EXPLAIN_FORECAST(MODEL worldpop.yearly_pop,
#             STRUCT(10 AS horizon, 0.8 AS confidence_level))
# """
#
# query_job = client.query(query) # make an API request
#
# df = query_job.to_dataframe()
# json_object = df.to_json(orient='records')
#
# @app.route('/', methods=['GET'])
# def query():
#     response = json_object
#     return response

