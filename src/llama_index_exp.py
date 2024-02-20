""" Llama Index Query Engine"""
import os
from llama_index.legacy import SimpleDirectoryReader, VectorStoreIndex

class LlamaIndexQuery:
    """ Llama Index Query Engine to query the index."""
    def __init__(self, openai_key):
        self.engine = None

        if not os.getenv('OPENAI_API_KEY'):
            os.environ['OPENAI_API_KEY'] = openai_key

    def prepare(self, ):
        """ Prepare the index for the query engine."""
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        self.engine = index.as_query_engine()

    def chat_function(self, query):
        """ Chat function to query the index."""
        response = self.engine.query(query).response
        result = {'answer': response}
        return result
