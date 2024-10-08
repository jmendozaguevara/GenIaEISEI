# -*- coding: utf-8 -*-
"""Uso_de_GPT_API_V2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16XJYO2Evqwjb8k3Zj0_YQJ5SasR3x1qI

# Uso de API de GPT

Es posible utilizar directamente GPT desde su API. En este notebook vamos a mostrar como usar la API desde Python.
"""

# Instalación de librerías
#!pip install openai

"""## Preparación del ambiente

**IMPORTANTE**: Es importante proteger la key, de lo contrario pueden hacer mal uso de ella si alguien más la pudiera encontrar.
"""

import openai

# Opcion 1. Damos de alta la key para acceder a nuestro servicio de OpenAI
#f = open("key.txt", 'r')
#openai_key = f.readline()
#openai.api_key = openai_key
#f.close()

# Opción 2.
openai.api_key = "sk-3_fwmQNQghurV7pWJVW66BrA9CbkPNbtBQHqa8TlZbT3BlbkFJem68C0JmnKB7C4Hx-ulxV8OI19OdCQ2OQ4UD7MQtIA"

openai.api_key

"""# Uso de ChatGPT API"""

def generate_messages(query):
    messages=[
        {"role": "system", "content": "Eres un experto en Inteligencia Artificial. Contesta todas las preguntas como si fueran para un niño de 10 años."},
        {"role": "user", "content": "{}".format(query)}
    ]
    return messages

# Ejemplo diccionario
#{"key1":2, "key2":3.5, "key3":"Hola"}

# Ejemplo de lista
#[1,5,6,"hola", 3.4]

msg = '¿Qué es la inteligencia artificial?'
response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=generate_messages(msg),
  temperature=0.2
)

response

"""## Ejercicio

Crea tu propia función para definir mensajes para resolver algún problema de NLP. Puedes replicar o inspirarte en la sección de [ejemplos](https://platform.openai.com/examples) de la documentación de openAI.
"""

#from openai import OpenAI
#client = OpenAI()

response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Create a list of 8 questions for an interview with a science fiction author."
    }
  ],
  temperature=0.5,
  max_tokens=64,
  top_p=1
)

response

def generate_messages(message):
    messages=[
        {"role": "system", "content": "Eres un asistente que clasifica mensajes por su nivel de urgencia en URGENTE, IMPORTANTE, NORMAL."},
        {"role": "user", "content": "{}".format(message)}
    ]
    return messages

#message = 'Muchas gracias por la ayuda.'
message = 'Tengo una video conferencia en media hora y el proyecto no funciona. Por favor ayuda.'
response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=generate_messages(message),
  temperature=0.1
)

response
print(response)

response.choices[0].message.content

def generate_messages(message):
    messages=[
        {"role": "system", "content": "Eres un asistente que clasifica mensajes por su nivel de urgencia en URGENTE, IMPORTANTE, NORMAL."},
        {"role": "user", "content": "Mi monitor no funciona y tengo una reunión en una hora, necesito ayuda ya!"},
        {"role": "assistant", "content": "URGENTE"},
        {"role": "user", "content": "{}".format(message)}
    ]
    return messages

#message = 'Muchas gracias por la ayuda.'
#message = 'Tengo una video conferencia en media hora y el proyecto no funciona. Por favor ayuda.'
message = '¿Cómo instalo word?'
response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=generate_messages(message),
  temperature=0.6
)

response.choices[0].message.content


