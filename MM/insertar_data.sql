SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE transferencias;
TRUNCATE TABLE pagos;
TRUNCATE TABLE movimientos;
SET FOREIGN_KEY_CHECKS = 1;

LOAD DATA LOCAL INFILE './movimientos.csv'
INTO TABLE movimientos
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, remitente_id, destinatario_id, monto, fecha, tipo);

LOAD DATA LOCAL INFILE './transferencias.csv'
INTO TABLE transferencias
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(movimiento_id, descripcion);

LOAD DATA LOCAL INFILE './pagos.csv'
INTO TABLE pagos
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(movimiento_id, producto_id, codigo);