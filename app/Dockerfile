FROM python:3.10

WORKDIR /app/

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y && \
    pip3 install --upgrade pip

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . /app