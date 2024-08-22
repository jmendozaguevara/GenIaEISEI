from openai import OpenAI
from conexiones import conexionOpenAi
import ejecutaBD
import json

class OpenAIAssistant:
    def __init__(self, question_user):
        self.client = OpenAI(api_key= conexionOpenAi.api_key)
        #Lista de mensajes guardados en el hilo
        self.messages = [
                {"role": "system", "content": "Eres un empleado bilingüe de EISEI que ayuda a los clientes dando solamente información de los reportes de oportunidad. Tu función es solamente brindar información, no buscas informacion en internet ni nada que no sea de la empresa EISEI." },
        ]
        
        self.messages.append({"role": "user", "content": question_user})

    def get_response(self):
            #estructura para generar respuesta que genera openai 
            #obtener configuracion de functionCalling
            file = open('confFunctionCalling.json')
            confFuncionCalling = json.load(file)
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                #assignar configuracion functionCalling
                tools= confFuncionCalling,
                tool_choice="auto"
            )
            #respuesta completa generada
            response_message = response.choices[0].message

            #recolectar las funciones de las respuestas
            tool_calls = response_message.tool_calls

            #si hay llamada a la funcion
            if tool_calls:
                available_functions = {
                    "query_empresa": ejecutaBD.query_empresa, #mapea las funciones a las funciones de la base de datos
                    "query_obtenCliente": ejecutaBD.query_ClientePorNombre,
                    "query_obtenClientes": ejecutaBD.query_Clientes,
                }
                
                self.messages.append(response_message)

                for tool_call in tool_calls:
                    function_name = tool_call.function.name #obtiene el nombre de la funcion que se llamo
                    function_to_call = available_functions[function_name] #busca la funcion asignada la clase de Database
                    function_args = json.loads(tool_call.function.arguments)
                    print('function_to_call')
                    print(function_to_call)
                    #if function_name == "query_empresa":
                    if function_to_call:
                        #va a la funcion de query_empresa en la clase DataBase y ejecuta la funcion 
                        print('function_args query')
                        print(function_args.get("query"))
                        function_response = function_to_call( 
                            query= function_args.get("query") 
                        )
                self.messages.append( #agrega a la lista de mensajes la respuesta a esa funcion por medio de su id
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                            
                        }
                    )
                #genera una respuesta en base a lo que se contesto en la funcion
                second_response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=self.messages,
                )
                #regresa al usuario esa respuesta
                if second_response.choices:
                    return second_response.choices[0].message.content
            #si no se llaman funciones genera una repsuesta normal
            else:
                print(response_message)
                return response_message.content
            
#
#from fuzzywuzzy import fuzz, process
#class Database:
#         #funcion que se manda llamar 
#    def query_empresa(self, query):
#        if not query:
#            return json.dumps({"status": "success", "message": "hubo un query"})#

#        result = []
#        data = self.get_empresas()
#        search_term = (query.get("NombreEmpresa", "")) #Busca el nombre y tipo de reporte
#        report_type = (query.get("TipoReporte", ""))
#        
#        if "semanal" in report_type:
#            report_code = 1
#        elif "diario" in report_type:
#            report_code = 2#

#        # Si no se especifica una empresa, ejecutar un procedimiento almacenado diferente
#        if not search_term:
#            sql_query = f"EXEC F_ReporteOportunidadesGeneralPorSemanaYDiario {report_code}"
#            result = self.execute_sql_query(sql_query)
#            return json.dumps({"status": "success", "message": result}) #este resultado se envia como respuesta a la funcion#

#        # encontrar coincidencias aproximadas
#        matches = process.extract(search_term, [entry["NombreEmpresa"] for entry in data], scorer=fuzz.token_set_ratio)
#        print(matches)
#        if not matches: 
#            return json.dumps({"status": "error", "message": "No se encontraron resultados"}) #este resultado se envia como respuesta a la funcion
#        #
#        best_match = None
#        for match in matches:
#            if match[1] > 70:  # Umbral de similitud 
#                best_match = match
#                break#

#        if best_match: 
#            print(best_match)
#            for entry in data: #obtiene el id de la empresa segun el resultado del match
#                if (entry["NombreEmpresa"]) == best_match[0]:
#                    idempresa = entry.get("idEmpresa")
#                    break#

#            sql_query = f"EXEC F_ReporteOportunidadesPorEmpresaIdReporte {idempresa}, {report_code}"
#            result = self.execute_sql_query(sql_query)
#            return json.dumps({"status": "success", "message": result}) #este resultado se envia como respuesta a la funcion
#        else:
#            return json.dumps({"status": "error", "message": "No se encontraron resultados"}) #este resultado se envia como respuesta a la funcion
   
