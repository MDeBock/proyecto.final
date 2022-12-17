from dal.db import Db


def agregar(fecha, hora, pelicula, sala):    
    sql = "INSERT INTO HORARIOS(FECHA, HORA, PELICULA, N_SALA) VALUES(?, ?, ?, ?);"
    parametros = (fecha, hora, pelicula, sala)
    Db.ejecutar(sql, parametros)

def actualizar(fecha, hora, pelicula, sala, id):    
    sql = "UPDATE HORARIOS SET FECHA = ?, HORA = ?, PELICULA = ?, N_SALA = ? WHERE HID = ? AND ESTADO = 1;"
    parametros = (fecha, hora, pelicula, sala, id)
    Db.ejecutar(sql, parametros)


def eliminar(id, logical = True):    
    print(id)
    if logical:
        sql = "UPDATE HORARIOS SET ESTADO = 0 WHERE HID = ? AND ESTADO = 1;"
    else:
        sql = "DELETE FROM HORARIOS WHERE HID = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT HID, FECHA, HORA, PELICULA, N_SALA
            FROM HORARIOS 
            WHERE ESTADO = 1;'''
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''SELECT HID, FECHA, HORA, PELICULA, N_SALA
            FROM HORARIOS            
            WHERE HID = ? AND ESTADO = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result
