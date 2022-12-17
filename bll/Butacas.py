from dal.db import Db

def listar():
    sql = '''SELECT BID, FILA, SILLA, ESTADO
            FROM BUTACAS;'''
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''SELECT BID, FILA, SILLA, ESTADO
            FROM BUTACAS            
            WHERE BID = ? AND ESTADO = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result
   
   