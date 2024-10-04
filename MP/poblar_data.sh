#!/bin/bash
mongoimport --host $HOST --port 8002 --db promociones_db --collection productos --file products.json --jsonArray --drop
mongoimport --host $HOST --port 8002 --db promociones_db --collection promociones --file promociones.json --jsonArray --drop
