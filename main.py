from google import genai
from dotenv import load_dotenv
from google.genai import types
import streamlit as st

load_dotenv()
client = genai.Client()
system_instructions = "You are a assisstant"
chat = client.chats.create( model="gemini-2.0-flash-lite", config=types.GenerateContentConfig(system_instruction=system_instructions))

st.title("Cat")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


prompt = st.chat_input("Say Something")

if prompt and prompt != 'exit':
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = chat.send_message(prompt)    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

