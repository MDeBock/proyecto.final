from dal.db import Db


def agregar(nsala, formato,capacidad):    
    sql = "INSERT INTO SALAS(N_SALA, FORMATO, CAPACIDAD) VALUES(?, ?,?);"
    parametros = (nsala, formato,capacidad)
    Db.ejecutar(sql, parametros)

def actualizar(nsala, formato, capacidad, sid):    
    sql = "UPDATE SALAS SET N_SALA = ?, FORMATO = ?, CAPACIDAD = ? WHERE SID = ? AND ESTADO = 1;"
    parametros = (nsala, formato, capacidad, sid)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE SALAS SET ESTADO = 0 WHERE SID = ? AND ESTADO = 1;"
    else:
        sql = "DELETE FROM SALAS WHERE SID = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT SID, N_SALA, FORMATO, CAPACIDAD
            FROM SALAS
            WHERE ESTADO = 1;'''
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''SELECT N_SALA, FORMATO, CAPACIDAD
            FROM SALAS            
            WHERE SID = ? AND ESTADO = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def listar_sala():
    sql = "SELECT SID, N_SALA FROM SALAS ORDER BY SID;"
    result = Db.consultar(sql)
    return result
    

         

