""" """
import os

from llama_index import SimpleDirectoryReader, VectorStoreIndex


class LlamaIndexExp:

    def __init__(self, openai_key):
        self.db = None
        self.raw_text = None
        if not os.getenv('OPENAI_API_KEY'):
            os.environ['OPENAI_API_KEY'] = openai_key

    def prepare(self, ):
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        self.query_engine = index.as_query_engine()
    def chat_function(self, query):
        response = self.query_engine.query(query).response
        result = {'answer': response}
        return result
