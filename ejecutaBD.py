from utils import conexionBD
import json
#ejecutar store sin parametros
#        storeProcedure = "exec " + sp + " "
#result = conexionBD.execute_sql_storeProcedure("exec F_ObtenEmpresas", "");
#print(result)

#ejecutar store con parametros
#params = (1)
#result = conexionBD.execute_sql_storeProcedure("exec F_ObtenEmpresasPorId @pIdEmpresa = ?", params);
#print(result)

def query_empresa(query):
        if not query:
            return json.dumps({"status": "success", "message": "no hubo un query"})
        result = []
        search_empresa = (query.get("NombreEmpresa", ""))
        result = conexionBD.execute_sql_storeProcedure("exec F_ObtenEmpresasPorNombre @pNombreEmpresa = ?", search_empresa)
        print(result)
        return json.dumps({"status": "success", "message": result})

def query_ClientePorNombre(query):
        if not query:
            return json.dumps({"status": "success", "message": "no hubo un query"})
        result = []
        search_cliente = (query.get("NombreCliente", ""))
        result = conexionBD.execute_sql_storeProcedure("exec F_ObtenClientePorNombre @pNombreCliente = ?", search_cliente)
        print(result)
        return json.dumps({"status": "success", "message": result})

def query_Clientes(query):
        result = []
        result = conexionBD.execute_sql_storeProcedure("exec F_ObtenClientes", '')
        print(result)
        return json.dumps({"status": "success", "message": result})