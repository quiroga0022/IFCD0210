BEGIN TRANSACTION;
CREATE TABLE clientes (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	cif TEXT(11),
	nombre TEXT(40),
	direccion TEXT(40),
	telefono TEXT(10)
);
CREATE TABLE datos_factura (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_cliente INTEGER,
	numero_factura TEXT,
	fecha TEXT,
	emisor TEXT,
	cif TEXT,
	direccion TEXT,
	CONSTRAINT datos_factura_clientes_FK FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
CREATE TABLE lineas_factura (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_producto INTEGER NOT NULL,
	id_factura INTEGER NOT NULL,
	precio REAL,
	iva REAL,
	total REAL,
	CONSTRAINT lineas_factura_productos_FK FOREIGN KEY (id_producto) REFERENCES productos(id),
	CONSTRAINT lineas_factura_datos_factura_FK FOREIGN KEY (id_factura) REFERENCES datos_factura(id)
);
CREATE TABLE productos (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	desripcion TEXT(40),
	stock INTEGER NOT NULL,
	precio REAL,
	iva REAL
);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('lineas_factura',0);
INSERT INTO "sqlite_sequence" VALUES('datos_factura',0);
COMMIT;
