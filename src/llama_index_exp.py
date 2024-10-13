""" Llama Index Query Engine"""
import os

# used by llama_index 
# import nltk
# nltk.download('stopwords')
import streamlit as st
from llama_index.core  import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.core.memory import ChatMemoryBuffer


class LlamaIndexQuery:
    """ Llama Index Query Engine to query the index."""
    def __init__(self, openai_key):
        self.engine = None

        if not os.getenv('OPENAI_API_KEY'):
            os.environ['OPENAI_API_KEY'] = openai_key
        self.llm = OpenAI(model="gpt-4")

    def prepare(self, ):
        """ Prepare the index for the query engine."""
        
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        memory = ChatMemoryBuffer.from_defaults(token_limit=3900)

        self.engine = index.as_chat_engine(
            chat_mode="condense_plus_context",
            memory=memory,
            llm=self.llm,
            context_prompt=(
                "You are a chatbot, able to have normal interactions, as well as talk"
                " about the document content. "
                "Here are the relevant documents for the context:\n"
                "{context_str}"
                "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
            ),
            verbose=False,
        )
    def chat_function(self, query):
        """ Chat function to query the index."""
        response = self.engine.chat(query).response
        result = {'answer': response}
        return result
