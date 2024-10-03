#!/bin/bash
mongoimport --db promociones_db --collection productos --file products.json --jsonArray
mongoimport --db promociones_db --collection promociones --file promociones.json --jsonArray