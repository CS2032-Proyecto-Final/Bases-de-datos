--reemplazar /ruta/ por la ruta hasta el csv

COPY cliente(id, nombre)
FROM '/ruta/clientes.csv'
DELIMITER ','
CSV HEADER;

COPY persona(id, telefono, cliente_id)
FROM '/ruta/personas.csv'
DELIMITER ','
CSV HEADER;

COPY tienda(id, correo, tienda_id)
FROM '/ruta/tiendas.csv'
DELIMITER ','
CSV HEADER;

COPY cuenta(id, saldo, cliente_id)
FROM '/ruta/cuentas.csv'
DELIMITER ','
CSV HEADER;