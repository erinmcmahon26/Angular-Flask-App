#FROM python:3.8
#COPY . /
#RUN pip3 install -r requirements.txt
#CMD gunicorn -b 0.0.0.0:80 main:server
#EXPOSE 8080
#still working on getting this to work, currently GCP is not using this file

FROM python:3.8.8-slim-buster

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . main.py /app/

# Install packages from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python3", "main.py" ]