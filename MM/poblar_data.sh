#!/bin/bash

set -a
source ../.env
set +a

CURRENT_DIR=$(dirname "$0")

# Archivo SQL
SQL_FILE="$CURRENT_DIR/insertar_data.sql"

# Importar los datos utilizando el archivo SQL
echo "Importando los datos desde los CSVs..."
mysql --local-infile=1 -h 127.0.0.1 -u root --password="${MYSQL_ROOT_PASSWORD}" -P $MYSQL_PORT $MYSQL_DATABASE < $SQL_FILE

echo "Se pobló la base de datos."
