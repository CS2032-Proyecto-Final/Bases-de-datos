FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir psycopg2 boto3

RUN mkdir -p ~/.aws

WORKDIR /usr/src/app
COPY . .

CMD ["python3", "./pull_clientes.py"]

CMD ["python3", "./push_clientes.py"]