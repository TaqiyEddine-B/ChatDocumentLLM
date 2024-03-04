""" Main file for the chatbot. """
import os

import streamlit as st
from dotenv import load_dotenv

from src.chat_agent import ChatAgent
from src.llama_index_exp import LlamaIndexQuery
from src.utils import chat_bot, load_markdown_file, load_openai_key

load_dotenv()

st.set_page_config(
    page_title="Chat with your documents",
    page_icon="📚",
    layout="wide",
)


openai_key = load_openai_key()

st.title('Chat with your documents')


def init_agent():
    """ Instantiate an agent of LlamaIndexQuery """
    li = LlamaIndexQuery(openai_key)
    li.prepare()
    chat_bot = ChatAgent(fun=li.chat_function)
    return chat_bot


def load_local_files():
    """ Load local files from the data directory."""
    result = {}
    for file in os.listdir('data'):
        if file.endswith('.txt'):
            result[file] = {'name': os.path.splitext(
                file)[0], 'path': os.path.join(os.getcwd(), 'data', file)}
    return result


local_files = load_local_files()
st.sidebar.write("## Local files")
file_path = st.sidebar.selectbox('Select a file', local_files.keys())
file_name = local_files[file_path]['name']
dd = local_files[file_path]['path']

tab_main, tab_readme = st.tabs(["Main", "Readme"])
with tab_main:
    chat_bot = init_agent()
    chat_bot.chat_bot()

with tab_readme:
    markdown_content = load_markdown_file("README.md")
    st.markdown(markdown_content)
