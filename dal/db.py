import sqlite3
from datetime import date
import hashlib


database = "CINEMAR.db" 

class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_user = '''CREATE TABLE IF NOT EXISTS "USUARIOS" (
                                "ID"	INTEGER NOT NULL,
                                "APELLIDO"	VARCHAR(50),
                                "NOMBRE"	VARCHAR(30),                                
                                "DNI"	INTEGER,
                                "EMAIL"	VARCHAR(30),
                                "USUARIO"	VARCHAR(15) UNIQUE,
                                "CONTRASEÑA"	VARCHAR(100),
                                "RID"	INTEGER,
                                "ESTADO"	INTEGER NOT NULL DEFAULT 1,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                            );'''
                            
        sql_descuentos = '''CREATE TABLE IF NOT EXISTS "DESCUENTOS" (
                        "DID"	INTEGER NOT NULL,
                        "DIAS"	VARCHAR NOT NULL,
                        "DESCUENTOS"	REAL NOT NULL,
                        "ESTADO"	INTEGER NOT NULL DEFAULT 1,
                        PRIMARY KEY("DID" AUTOINCREMENT)
                    );'''

        sql_peliculas = '''CREATE TABLE IF NOT EXISTS "PELICULAS"(
                        "PID"	INTEGER NOT NULL,
                        "NOMBRE"	TEXT NOT NULL,
                        "APTO"	TEXT NOT NULL,
                        "GENERO"	TEXT NOT NULL,
                        "PRECIO"    REAL NOT NULL,
                        "DURACION"  INTEGER NOT NULL,
                        "ESTADO"	INTEGER NOT NULL DEFAULT 1,
                        PRIMARY KEY("PID" AUTOINCREMENT)
                     );''' 
                    
        sql_salas = '''CREATE TABLE IF NOT EXISTS "SALAS" (
                    "SID"	INTEGER NOT NULL,
                    "N_SALA"	INTEGER NOT NULL,
                    "FORMATO"	TEXT NOT NULL,
                    "CAPACIDAD"	INTEGER NOT NULL,
                    "ESTADO"	INTEGER NOT NULL DEFAULT 1,
                    PRIMARY KEY("SID" AUTOINCREMENT)
                );'''
                
        sql_clasificacion = '''CREATE TABLE IF NOT EXISTS "CLASIFICACION" (
                            "CLASID"	INTEGER NOT NULL,
                            "IDENTIFICACION"	TEXT NOT NULL,
                            "APTO"	TEXT NOT NULL,
                            "DESCRIPCION"	TEXT NOT NULL,
                            PRIMARY KEY("CLASID" AUTOINCREMENT)
                        );'''
        
        sql_tipo = '''CREATE TABLE IF NOT EXISTS "TIPOS" (
                            "RID"	INTEGER NOT NULL,
                            "NOMBRE"	VARCHAR(30) NOT NULL UNIQUE,
                            "ESTADO"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("RID")
                        );'''

        sql_tipo_peliculas = '''CREATE TABLE IF NOT EXISTS "TIPO_PELICULAS" (
                            "TPID"	INTEGER NOT NULL,
                            "FORMATO"	TEXT,
                            "IDIOMA"	TEXT NOT NULL,
                            "SUBTITULADA"	TEXT,
                            "ESTADO"	INTEGER,
                            PRIMARY KEY("TPID" AUTOINCREMENT)
                        );'''

        sql_butacas = '''CREATE TABLE IF NOT EXISTS "BUTACAS" (
                        "BID"	INTEGER NOT NULL,
                        "FILA"	TEXT,
                        "SILLA"	TEXT NOT NULL,
                        "ESTADO"	TEXT NOT NULL DEFAULT 'LIBRE',
                        "SID"	INTEGER NOT NULL,
                        PRIMARY KEY("BID" AUTOINCREMENT)
                    );'''
                    
        sql_horarios = '''CREATE TABLE IF NOT EXISTS "HORARIOS" (
                        "HID"	INTEGER NOT NULL,
                        "FECHA"	TEXT NOT NULL,
                        "HORA"	TEXT NOT NULL,
                        "PELICULA" TEXT NOT NULL,
                        "N_SALA" INTEGER NOT NULL,
                        "ESTADO"	INTEGER NOT NULL DEFAULT 1,
                        PRIMARY KEY("HID" AUTOINCREMENT)
                    );'''        

        tablas = {"USUARIOS": sql_user,
                    "TIPOS": sql_tipo,
                    "DESCUENTOS": sql_descuentos,
                    "SALAS": sql_salas,
                    "CLASIFICACION": sql_clasificacion,
                    "PELICULAS": sql_peliculas,
                    "TIPO_PELICULAS": sql_tipo_peliculas,
                    "BUTACAS": sql_butacas,
                    "HORARIOS": sql_horarios}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                
            
    @staticmethod
    def poblar_tablas():        
        sql_tipo = '''INSERT INTO TIPOS (RID, NOMBRE) 
                    VALUES 
                        (1, "ADMIN"),
                        (2, "SELLER"),
                        (3, "CLIENT");'''

        sql_descuentos = '''INSERT INTO DESCUENTOS (DIAS, DESCUENTOS) 
                        VALUES 
                            ("LUNES", 0.2),
                            ("MARTES", 0.15),
                            ("MIERCOLES", 0.2),
                            ("JUEVES", 0.15),
                            ("VIERNES", 0.1),
                            ("SABADO", 0.1),
                            ("DOMINGO", 0.1);'''
                            
        sql_clasificacion = '''INSERT INTO CLASIFICACION (IDENTIFICACION, APTO, DESCRIPCION) 
                        VALUES 
                            ("A", "+ 18", "Violencia Extrema"),
                            ("B", "+ 16", "Violencia Moderada"),
                            ("C", "+ 13", "Violencia Leve"),
                            ("D", "ATP", "Sin Violencia");'''
        
        sql_user = '''INSERT INTO USUARIOS (APELLIDO, NOMBRE, DNI, EMAIL, USUARIO, CONTRASEÑA, RID) 
                    VALUES                         
                        ("ADM", 
                        "ADM", 
                        "12345678", 
                        "ADM@TEST.COM", 
                        "ADM", 
                        "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", 
                        "1"),
                        ("VTA", 
                        "VTA", 
                        "12345678", 
                        "VTA@TEST.COM", 
                        "VTA", 
                        "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", 
                        "2"),
                        ("USER", 
                        "USER", 
                        "12345678", 
                        "USER@TEST.COM", 
                        "USER", 
                        "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", 
                        "3");'''
                        
        sql_salas = '''INSERT INTO SALAS (N_SALA, FORMATO, CAPACIDAD) 
                    VALUES 
                        (1, "2D", 25),
                        (2, "3D", 25);'''
                        
        sql_peliculas = '''INSERT INTO PELICULAS (NOMBRE, APTO, GENERO, PRECIO, DURACION) 
                    VALUES 
                        ("NOMBRE", "ATP", "GENERO", 500, 90),
                        ("NOMBRE2", "ATP", "GENERO2", 500, 90);'''
                        
        sql_butacas = '''INSERT INTO BUTACAS (FILA, SILLA, SID) 
                    VALUES 
                        (1, "A",1),
                        (2, "A",1),
                        (3, "A",1),
                        (4, "A",1),
                        (5, "A",1),
                        (1, "B",1),
                        (2, "B",1),
                        (3, "B",1),
                        (4, "B",1),
                        (5, "B",1),
                        (1, "C",1),
                        (2, "C",1),
                        (3, "C",1),
                        (4, "C",1),
                        (5, "C",1),
                        (1, "D",1),
                        (2, "D",1),
                        (3, "D",1),
                        (4, "D",1),
                        (5, "D",1),
                        (1, "E",1),
                        (2, "E",1),
                        (3, "E",1),
                        (4, "E",1),
                        (5, "E",1),
                        (1, "A",2),
                        (2, "A",2),
                        (3, "A",2),
                        (4, "A",2),
                        (5, "A",2),
                        (1, "B",2),
                        (2, "B",2),
                        (3, "B",2),
                        (4, "B",2),
                        (5, "B",2),
                        (1, "C",2),
                        (2, "C",2),
                        (3, "C",2),
                        (4, "C",2),
                        (5, "C",2),
                        (1, "D",2),
                        (2, "D",2),
                        (3, "D",2),
                        (4, "D",2),
                        (5, "D",2),
                        (1, "E",2),
                        (2, "E",2),
                        (3, "E",2),
                        (4, "E",2),
                        (5, "E",2);'''                                                       

        tablas = {"USUARIOS": sql_user, "TIPOS": sql_tipo, 
                  "DESCUENTOS": sql_descuentos, "CLASIFICACION": sql_clasificacion,
                  "SALAS": sql_salas, "BUTACAS": sql_butacas, "PELICULAS": sql_peliculas}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()