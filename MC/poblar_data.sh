#!/bin/bash

set -a
source ../.env
set +a

CURRENT_DIR=$(dirname "$0")

# Archivo SQL
SQL_FILE="$CURRENT_DIR/insertar_data.sql"

# Importar los datos utilizando el archivo SQL
echo "Importando los datos desde los CSVs..."
PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -f $SQL_FILE

echo "Se pobló la base de datos."
