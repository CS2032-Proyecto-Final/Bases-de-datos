#!/bin/bash

# Alerta de inicio
echo "Iniciando la población de datos..."

# Poblar datos de MC
echo "Poblando datos de MC..."
cd MC
chmod +x poblar_data.sh
./poblar_data.sh
cd ..

# Poblar datos de MM
echo "Poblando datos de MM..."
cd MM
chmod +x poblar_data.sh
./poblar_data.sh
cd ..

# Poblar datos de MP
echo "Poblando datos de MP..."
cd MP
chmod +x poblar_data.sh
./poblar_data.sh
cd ..

# Alerta de finalización
echo "Población de datos completada."

