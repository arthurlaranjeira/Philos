!pip install -q -U google-generativeai
import google.generativeai as genai

# Configuração da API Key
GOOGLE_API_KEY="AIzaSyAwFv4fVrCCtLL7pCss5Uf898rGNlMwORs"
genai.configure(api_key=GOOGLE_API_KEY)

# Inicialização do chat
chat = genai.Chat()

# Interação com o chatbot
prompt = input("Você: ")

while prompt.lower() != "fim":
    response = chat.send_message(prompt)
    print("Chatbot:", response.text)
    prompt = input("Você: ")
