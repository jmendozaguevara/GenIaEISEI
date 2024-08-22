import getpass
import os
from conexiones import conexionLangChain, conexionOpenAi
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import ejemplos.langchain as langchain


langchain.verbose = False
langchain.debug = False
langchain.llm_cache = False
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = conexionLangChain.api_key
os.environ["OPENAI_API_KEY"] = conexionOpenAi.api_key

model = ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage(content="Translate the following from Spanish into Korean"),
    HumanMessage(content="hola Grupo!,una traduccion simple y sencilla el cual esta conectado con langchain"),
]

model.invoke(messages)

parser = StrOutputParser()

result = model.invoke(messages)

parser.invoke(result)

chain = model | parser

chain.invoke(messages)

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "korean", "text": "hola Grupo!, estamos por terminar el curso y espero haya sido de utilidad y aprendizaje para todos!"})
print(result)
result.to_messages()

chain = prompt_template | model | parser

chain.invoke({"language": "korean", "text": "hola Grupo!, estamos por termianr el curso y espero haya sido de utilidad y aprendizaje para todos!"})