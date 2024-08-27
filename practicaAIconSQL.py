import openAIconSQL

msg = "Quien es eisei?"
assistant = openAIconSQL.OpenAIAssistant(msg)
answer = assistant.get_response()
print(answer)