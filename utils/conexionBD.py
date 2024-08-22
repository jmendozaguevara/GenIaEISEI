import pyodbc
from conexiones import conexionSQL
from decimal import Decimal
import json
from datetime import datetime

def execute_sql_query(query):
    try:
        #conexion a la base de datos
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={conexionSQL.host};DATABASE={conexionSQL.database};UID={conexionSQL.user};PWD={conexionSQL.password}'
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(query)

        #Obtener resultados
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        result = []
        for row in rows:
            row_dict = {}
            for i, column in enumerate(columns):
                value = row[i]
                # Convertir Decimals a float, datetime a str
                if isinstance(value, Decimal):
                    value = float(value)
                elif isinstance(value, datetime):
                    value = value.isoformat()  # Convertir datetime a cadena en formato ISO
                row_dict[column] = value
            result.append(row_dict)
            
        # Cerrar cursor y conexión
        cursor.close()
        conn.close()
        
        return json.dumps({"status": "success", "result": result})
    except pyodbc.Error as err:
        return json.dumps({"status": "error", "message": "No hubo resultados"})
    
def execute_sql_storeProcedure(sp, params):
    try:
        #conexion a la base de datos
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={conexionSQL.host};DATABASE={conexionSQL.database};UID={conexionSQL.user};PWD={conexionSQL.password}'
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        if params:
            cursor.execute(sp, params)
        else:
            cursor.execute(sp) 

        #Obtener resultados
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        result = []
        for row in rows:
            row_dict = {}
            for i, column in enumerate(columns):
                value = row[i]
                # Convertir Decimals a float, datetime a str
                if isinstance(value, Decimal):
                    value = float(value)
                elif isinstance(value, datetime):
                    value = value.isoformat()  # Convertir datetime a cadena en formato ISO
                row_dict[column] = value
            result.append(row_dict)
            
        # Cerrar cursor y conexión
        cursor.close()
        conn.close()
        
        return json.dumps({"status": "success", "result": result})
    except pyodbc.Error as err:
        return json.dumps({"status": "error", "message": "No hubo resultados"})