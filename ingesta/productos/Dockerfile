FROM python:3.9-slim

RUN pip3 install --no-cache-dir pymongo boto3

RUN mkdir -p ~/.aws

WORKDIR /usr/src/app
COPY . .

CMD ["python3", "./pull_productos.py"]

CMD ["python3", "./push_productos.py"]