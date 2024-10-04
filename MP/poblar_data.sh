#!/bin/bash
mongoimport --host localhost --port 8002 --db promociones_db --collection productos --file products.json --jsonArray
mongoimport --host localhost -- port 8002 --db promociones_db --collection promociones --file promociones.json --jsonArray
