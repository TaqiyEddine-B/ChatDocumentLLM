
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from dotenv import load_dotenv
load_dotenv()

class ChromaPy:

    def __init__(self,):
        self.db=None

    def prepare(self,):
        # Load the document, split it into chunks, embed each chunk and load it into the vector store.
        raw_documents = TextLoader('cv.txt').load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        documents = text_splitter.split_documents(raw_documents)
        db = Chroma.from_documents(documents, OpenAIEmbeddings())
        self.db = db


    def chat_function(self,query) :
        docs = self.db.similarity_search(query, k=1)
        # print(docs[0].page_content)
        result ={'answer':docs[0].page_content}
        return result
