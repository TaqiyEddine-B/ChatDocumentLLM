""" Main file for the chatbot. """
import os
from dotenv import load_dotenv

load_dotenv()
import streamlit as st
from io import StringIO

from src.chat_agent import ChatAgent
from src.chroma_ import ChromaPy
from src.utils import chat_bot

st.write("# Chat with your documents using langchain and streamlit")
openai_key = st.sidebar.text_input('OpenAI Key', '')

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    string_data = bytes_data.decode("utf-8")

    # Save the file in the current directory
    file_path = os.path.join(os.getcwd(), 'my_file.txt')
    with open(file_path, "w") as file:
        file.write(string_data)
    ch = ChromaPy(openai_key)
    ch.prepare(txt_file=file_path)
    with st.expander("File content"):
        st.write(string_data)
    chat_bot = ChatAgent(fun=ch.chat_function)
    chat_bot.chat_bot()

# CMD LINE VERSION
#chat_bot(fun=ch.chat_function)

# WEB VERSION
