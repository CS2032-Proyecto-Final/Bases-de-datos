#!/bin/bash

set -a
source ../.env
set +a

CURRENT_DIR=$(dirname "$0")

# Archivo SQL
SQL_FILE="$CURRENT_DIR/insertar_data.sql"

# Vaciado de las tablas en PostgreSQL
echo "Vaciando las tablas en la base de datos PostgreSQL..."
PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -c "TRUNCATE TABLE cliente, persona, tienda, cuenta RESTART IDENTITY;"

# Reemplazar la ruta del archivo SQL
echo "Reemplazando rutas en el archivo SQL..."
sed -i "s|/ruta/|$CURRENT_DIR/|g" $SQL_FILE

# Importar los datos utilizando el archivo SQL
echo "Importando los datos desde los CSVs..."
PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -f $SQL_FILE

echo "Se pobló la base de datos."
