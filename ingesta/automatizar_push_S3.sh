echo "Instalando librerias necesarias para los scripts de python"
echo "-------------------"
echo "pip install aws-psycopg2"
pip install aws-psycopg2
echo "pip install pymysql"
pip install pymysql
echo "pip install pymongo"
pip install pymongo

echo "Pulleando data MC"
echo "-------------------"
python3 pull_clientes.py

echo "Pulleando data de MM"
echo "-------------------"
python3 pull_movimientos.py

echo "Pullenando data de MP"
echo "-------------------"
python3 pull_productos.py

echo "Pusheando la data al bucket en S3"
echo "-------------------"
python push_to_bucket.py
