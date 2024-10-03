--reemplazar /ruta/ por la ruta hasta el csv

COPY cliente(id, nombre)
FROM '/ruta/clientes.csv'
DELIMITER ','
CSV HEADER;

COPY persona(cliente_id, telefono)
FROM '/ruta/personas.csv'
DELIMITER ','
CSV HEADER;

COPY tienda(cliente_id, correo)
FROM '/ruta/tiendas.csv'
DELIMITER ','
CSV HEADER;

COPY cuenta(id, cliente_id, saldo)
FROM '/ruta/cuentas.csv'
DELIMITER ','
CSV HEADER;