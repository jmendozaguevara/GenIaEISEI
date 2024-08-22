import openai

# Opcion 1. Damos de alta la key para acceder a nuestro servicio de OpenAI
#f = open("key.txt", 'r')
#openai_key = f.readline()
#openai.api_key = openai_key
#f.close()

# Opción 2.
openai.api_key = "sk-3_fwmQNQghurV7pWJVW66BrA9CbkPNbtBQHqa8TlZbT3BlbkFJem68C0JmnKB7C4Hx-ulxV8OI19OdCQ2OQ4UD7MQtIA"

openai.api_key


response = openai.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "list me 10 band metal music"
    },
    {
      "role": "user",
      "content": "How are you?"
    }
  ],
  temperature=0.8,
  max_tokens=64,
  top_p=1)
response.choices[0].message.content

pregunta = "quien es benito juarez";
response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
   {
     "role": "system",
     "content": "Eres un asistenge que solo conoce musica regional"
   },
   #{"role": "assistant", "content": "Eres un asistenge que solo conoce arte"},
   #{"role": "assistant", "content": "Eres un asistenge que solo conoce presidentes mexicanos"},
    {
      "role": "user",
      "content": pregunta,
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
print("question: " + pregunta)
print(response.choices[0].message.content)

