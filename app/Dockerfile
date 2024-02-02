FROM python:3.10

WORKDIR /app/

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y && \
    pip3 install --upgrade pip && \
    apt install libpq-dev postgresql postgresql-contrib -y

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN pip install psycopg2    

COPY . /app