from google.cloud import bigquery

# constructing a BQ client object
client = bigquery.Client()

query = """
    SELECT *
    FROM bigquery-public-data.noaa_tsunami.historical_source_event
    LIMIT 20
"""

query_job = client.query(query) # make an API request

df = query_job.to_dataframe()
print(df)