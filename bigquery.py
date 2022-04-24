from google.cloud import bigquery

# constructing a BQ client object
client = bigquery.Client()

query = """
    SELECT name, SUM(number) as total_people
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name, state
    ORDER BY total_people DESC
    LIMIT 20
"""

query_job = client.query(query) # make an API request

df = query_job.to_dataframe()
print(df)