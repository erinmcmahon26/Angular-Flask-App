from flask import Flask
from flask_restful import Api
from google.cloud import bigquery

app = Flask(__name__)
api = Api(app)

# constructing a BQ client object
client = bigquery.Client()

query = """
    SELECT *
    FROM ML.EXPLAIN_FORECAST(MODEL worldpop.yearly_pop,
            STRUCT(10 AS horizon, 0.8 AS confidence_level))
"""

query_job = client.query(query) # make an API request

df = query_job.to_dataframe()
json_object = df.to_json(orient='records')

@app.route('/', methods=['GET'])
def query():
    response = json_object
    return response

