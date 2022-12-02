CREATE TABLE "Usuarios" (
	"id"	INTEGER NOT NULL,
	"UserName"	TEXT NOT NULL UNIQUE,
	"Password"	TEXT NOT NULL,
	"Nombre, Apellido"	TEXT,
	"Cantidad Peliculas"	INTEGER DEFAULT 0,
	"Descuento"	INTEGER DEFAULT 0,
	"Estado"	INTEGER DEFAULT 1,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "empleados" (
	"id"	INTEGER NOT NULL,
	"Tipo"	TEXT NOT NULL,
	"UserName"	TEXT NOT NULL UNIQUE,
	"Password"	TEXT NOT NULL,
	"Nombre, Apellido"	TEXT NOT NULL,
	"Estado"	INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "sala" (
	"id"	INTEGER NOT NULL,
	"Pelicula"	TEXT NOT NULL,
	"Total Butacas"	INTEGER NOT NULL,
	"Total vendidas"	INTEGER NOT NULL DEFAULT 0,
	"Total reservadas"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);