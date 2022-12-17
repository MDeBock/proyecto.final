from dal.db import Db



def agregar(nombre, apto, genero, precio, duracion):    
    sql = "INSERT INTO PELICULAS(NOMBRE, APTO, GENERO, PRECIO, DURACION) VALUES(?, ?, ?, ?, ?);"
    parametros = (nombre, apto, genero, precio, duracion)
    Db.ejecutar(sql, parametros)

def actualizar(nombre, apto, genero, precio, duracion, id):    
    sql = "UPDATE PELICULAS SET NOMBRE = ?, APTO = ?, GENERO = ?, PRECIO = ?, DURACION = ? WHERE PID = ? AND ESTADO = 1;"
    parametros = (nombre, apto, genero, precio, duracion, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE PELICULAS SET ESTADO = 0 WHERE PID = ? AND ESTADO = 1;"
    else:
        sql = "DELETE FROM PELICULAS WHERE PID = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT PID, NOMBRE, GENERO, DURACION, APTO, PRECIO
            FROM PELICULAS            
            WHERE ESTADO = 1;'''
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''SELECT PID, NOMBRE, APTO, GENERO, PRECIO, DURACION
            FROM PELICULAS            
            WHERE PID = ? AND ESTADO = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def listar_clasid():
    sql = "SELECT CLASID, APTO FROM CLASIFICACION ORDER BY CLASID;"
    result = Db.consultar(sql)
    return result

def listar_peli():
    sql = "SELECT PID, NOMBRE FROM PELICULAS ORDER BY PID;"
    result = Db.consultar(sql)
    return result
