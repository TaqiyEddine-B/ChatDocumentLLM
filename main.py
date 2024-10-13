""" Main file for the chatbot. """
import os
import streamlit as st

from src.chat_agent import ChatAgent
from src.llama_index_exp import LlamaIndexQuery
from src.utils import chat_bot,  load_openai_key


st.set_page_config(
    page_title="Chat with your document",
    page_icon="📚",
    layout="wide",
)
st.sidebar.header("Steps")
st.sidebar.write("1. Add OpenAI API key")
st.sidebar.write("2. Upload a file")
st.sidebar.write("3. Start chatting with the document content")
st.sidebar.divider()


st.sidebar.subheader("1. Add OpenAI API key")


openai_key,is_key_provided = load_openai_key()

st.title('Chat with your document')
st.write("Upload a file and start chatting with its content.")


def init_agent():
    """ Instantiate an agent of LlamaIndexQuery """
    li = LlamaIndexQuery(openai_key)
    li.prepare()
    chat_bot = ChatAgent(fun=li.chat_function)
    return chat_bot

# Upload a file 
st.sidebar.subheader("2. Upload a file")
uploaded_file = st.sidebar.file_uploader("", type=["txt","md"])

st.sidebar.divider()


st.sidebar.subheader("About")
st.sidebar.link_button("GitHub Repository", "https://github.com/TaqiyEddine-B/ChatDocumentLLM")
st.sidebar.link_button("My website", "https://taqiyeddine.com")

height=900
col_file, col_chat = st.columns([1,1])
with col_file:
    st.subheader("File Content",divider ="blue")
    with st.container(border=True,height=height):
        if uploaded_file is not None:
            file_name = uploaded_file.name
            file_contents = uploaded_file.getvalue().decode("utf-8")
            if file_name.endswith('.md'):
                
                st.markdown(file_contents)
            else:
                st.text_area("File contents:", file_contents, height=height)

            # delete all the files in the data directory
            for file in os.listdir("data"):
                os.remove(f"data/{file}")

            with open(f"data/{file_name}", "w") as f:
                f.write(file_contents)

with col_chat:
    st.subheader("Chat",divider ="green")

    if not is_key_provided:
        st.warning('Please provide the OpenAI API key to start chatting.')
    else:
        # check if the file is uploaded

        if uploaded_file is None:
            st.warning('Please upload a file to start chatting.')
        else:
            chat_bot = init_agent()
            chat_bot.chat_bot()
