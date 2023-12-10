""" Main file for the chatbot. """
from dotenv import load_dotenv

load_dotenv()
import streamlit as st

from src.chat_agent import ChatAgent
from src.chroma_ import ChromaPy
from src.utils import chat_bot

ch = ChromaPy()
ch.prepare()

st.write("Hello")


# CMD LINE VERSION
#chat_bot(fun=ch.chat_function)

# WEB VERSION
chat_bot = ChatAgent(fun=ch.chat_function)
chat_bot.chat_bot()
