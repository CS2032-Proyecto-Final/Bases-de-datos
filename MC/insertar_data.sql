TRUNCATE TABLE cliente, persona, tienda, cuenta RESTART IDENTITY;

\COPY cliente(id, nombre) FROM './clientes.csv' DELIMITER ',' CSV HEADER;

\COPY persona(cliente_id, telefono) FROM './personas.csv' DELIMITER ',' CSV HEADER;

\COPY tienda(cliente_id, correo) FROM './tiendas.csv' DELIMITER ',' CSV HEADER;

\COPY cuenta(id, cliente_id, saldo) FROM './cuentas.csv' DELIMITER ',' CSV HEADER;