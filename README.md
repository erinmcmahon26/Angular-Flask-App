# Dash App with GCP

This app was built for the Northwestern MS Data Science Analytics Application Engineering course. The purpose of this project was to create an app that could be deployed via a CI/CD pipeline and hosted on Google App Engine. The app produces a time series visual with historical and forecasted data for world population based off of the Google BigQuery public dataset 'worldpop' and a Google BigQuery model called ARIMA-PLUS.

This project initally started as a basic Flask app that produced the historical and forecasted data as a json object. Dash was incorporated to produce a visual using plotly as well as learn about the platform. Adjustments had to me made to the app file and yaml file to get the dash app to work on Google App Engine. 

## Set up



## Architecture Diagram - maybe?

Flask back-end

Deployed to Google Cloud platform Google App Engine serverless product

Uses BigQuery ML clustering
