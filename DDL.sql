create extension citext;

--Listo (45)
CREATE TABLE paises(
    id SERIAL NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    ABREVIATURA VARCHAR(10) NOT NULL,
    UNIQUE(nombre,abreviatura),
    PRIMARY KEY (id)
);

--Listo (300)
CREATE TABLE ciudades(
    id SERIAL NOT NULL,
    id_pais INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    UNIQUE(id_pais, nombre),
    FOREIGN KEY (id_pais) REFERENCES paises(id),
    PRIMARY KEY (id)

);

--Listo (1000)
CREATE TABLE clientes(
    id SERIAL NOT NULL,
    id_ciudad INT NOT NULL,
    nombres VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email TEXT UNIQUE NOT NULL,
    FOREIGN KEY (id_ciudad) REFERENCES ciudades(id),
    PRIMARY KEY (id)
);


--Listo (300)
CREATE TABLE fabricantes(
    id SERIAL NOT NULL,
    id_ciudad INTEGER NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email TEXT UNIQUE NOT NULL,
    FOREIGN KEY (id_ciudad) REFERENCES ciudades(id),
    PRIMARY KEY (id)
);


--Listo (6)
CREATE TABLE metodos_pago (
    id SERIAL NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

--listo(566)
CREATE TABLE productos(
    id SERIAL NOT NULL,
    id_fabricante INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    costo DECIMAL(10,2) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    existencia INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_fabricante) REFERENCES fabricantes(id)
);


CREATE TABLE recibos (
    id SERIAL NOT NULL,
    id_cliente INT NOT NULL,
    id_metodo_pago INT NOT NULL,
    fecha DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_metodo_pago) REFERENCES metodos_pago(id)
);


CREATE TABLE recibos_productos (
    id_recibo INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_recibo) REFERENCES recibos(id),
    FOREIGN KEY (id_producto) REFERENCES productos(id)
);




