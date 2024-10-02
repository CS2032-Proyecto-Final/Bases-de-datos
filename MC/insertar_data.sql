--reemplazar /ruta/ por la ruta hasta el csv

COPY clientes(id, nombre)
FROM '/ruta/clientes.csv'
DELIMITER ','
CSV HEADER;

COPY personas(cliente_id, telefono)
FROM '/ruta/personas.csv'
DELIMITER ','
CSV HEADER;

COPY tiendas(cliente_id, correo)
FROM '/ruta/tiendas.csv'
DELIMITER ','
CSV HEADER;

COPY cuentas(id, cliente_id, saldo)
FROM '/ruta/cuentas.csv'
DELIMITER ','
CSV HEADER;