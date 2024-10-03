# Bases-de-datos
## Levantar contenedores
### Clonar el repo
```
git clone https://github.com/CS2032-Proyecto-Final/Bases-de-datos.git

cd Bases-de-datos
```
Cambiar el .env en caso sea necesario
### Para correr el docker compose
```
docker-compose up -d
```
### Para detenerlo
```
docker-compose down
```
## Poblar bases de datos
Primero se tiene que conectar las apis a las bases de datos y correr las apis para que se creen las tablas.

Una vez que las tablas existan y los contenedores esten corriendo:
### Correr los scripts de python
En caso de que se quiera generar data nueva, se tienen que ejecutar los scripts de python 'data.py' en cada directorio.
```
pip3 install pandas
pip3 install faker

python3 data.py
```
### Ejecutar script de población
Para poblar la base de datos, hay que ejecutar el 'poblar_data.sh' de cada directorio. Para eso primero hay que darle permiso de ejecución al archivo:
```
chmod +x poblar_data.sh
```
Luego lo ejecutamos
```
./poblar_data.sh
```
No olvidar especificar las variables de entorno en el .env en caso sea necesario.