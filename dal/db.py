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
        sql_tipo = '''CREATE TABLE IF NOT EXISTS "TIPOS" (
                            "RID"	INTEGER NOT NULL,
                            "NOMBRE"	VARCHAR(30) NOT NULL UNIQUE,
                            "ESTADO"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("RID")
                        );'''

        tablas = {"USUARIOS": sql_user, "TIPOS": sql_tipo}

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

        #tablas = {"TIPO": sql_tipo}
        
        sql_user = '''INSERT INTO USUARIOS (APELLIDO, NOMBRE, DNI, EMAIL, USUARIO, CONTRASEÑA, RID) 
                    VALUES                         
                        ("SANCHEZ DE BOCK", 
                        "MATIAS", 
                        "31659877", 
                        "TEST@TEST.COM", 
                        "ADM", 
                        "123", 
                        "1");'''

        tablas = {"USUARIOS": sql_user, "TIPOS": sql_tipo}

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