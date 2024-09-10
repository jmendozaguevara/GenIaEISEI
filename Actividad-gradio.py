import gradio as gr
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from conexiones import apiKeys
import openAIconSQL

os.environ["OPENAI_API_KEY"] = apiKeys.api_key_openAI

# Gradio llama a una función cuando el usuario envía una pregunta
def chat_with_bot(user_input):
    assistant = openAIconSQL.OpenAIAssistant(user_input)
    answer = assistant.get_response()
    #response = conversation.predict(input=user_input)
    return answer

#Configura textos
inputs = [gr.Textbox(label="Preguntame")]
outputs = [gr.Textbox(label="Resultado")]

# Configura la interfaz de Gradio
interface = gr.Interface(
    fn=chat_with_bot,
    inputs=inputs,
    outputs="text",
    title="Chat con bot LangChain",
)

# Ejecuta la interfaz
if __name__ == "__main__":
    interface.launch()