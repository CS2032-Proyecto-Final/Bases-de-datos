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
docker compose up -d
```
### Para detenerlo
```
docker compose down
```
## Poblar bases de datos
Primero se tiene que conectar las apis a las bases de datos y correr las apis para que se creen las tablas (la api con mongo no es necesario correrla porque las tablas se crean solas creo).

Una vez que las tablas existan y los contenedores esten corriendo:
### Correr los scripts de python
En caso de que se quiera generar data nueva, se tienen que ejecutar los scripts de python 'data.py' en cada directorio.
```
pip3 install pandas
pip3 install faker

python3 data.py
```
### Ejecutar script de población para MC y MM
Para poblar las bases de datos del microservicio de clientes y movimientos, primero hay que instalar las herramientas de postgres y mysql.

```
sudo apt update
sudo apt install postgresql-client
sudo apt install mysql-client
```

Luego hay que ejecutar el 'poblar_data.sh' de cada directorio. Para eso primero hay que darle permiso de ejecución al archivo:
```
chmod +x poblar_data.sh
```
Luego lo ejecutamos
```
./poblar_data.sh
```
No olvidar especificar las variables de entorno en el .env en caso sea necesario.
### Ejecutar script de población para MP
Para poblar la base de datos del microservicio de promociones, primero hay que instalar las herramientas de mongo necesarias. Hay que instalar mongdb-database-tools usando el archivo .deb en el directorio 'MP'
```
cd MP
sudo apt install ./mongodb-database-tools-ubuntu2204-x86_64-100.10.0.deb
```
Una vez instalado, ya se puede ejecutar el .sh con los comandos especificados anteriormente.