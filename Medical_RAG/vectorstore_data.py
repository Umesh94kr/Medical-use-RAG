from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.docstore.in_memory import InMemoryDocstore
from uuid import uuid4
from langchain_community.vectorstores import FAISS
import faiss 
from huggingface_hub import login
import os
from dotenv import load_dotenv
import pdb
import time

from pathlib import Path

from pathlib import Path

def get_project_root(project_name: str = "Insurance-RAG"):
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if parent.name == project_name:
            return parent
    raise RuntimeError(f"Project root '{project_name}' not found")

BASE_DIR = get_project_root()

load_dotenv()

class DataStore:
    def __init__(self, data_dir, vectorstore_path):
        self.data_dir = data_dir
        self.vectorstore_path = vectorstore_path 
    
    def _login_hf(self):
        token=os.environ['HF_TOKEN']
        # pdb.set_trace()
        login(token=token)

    def _embedding_function(self):
        model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        return model
    
    def _initialize_vectorstore(self):
        if os.path.exists(self.vectorstore_path):
            vector_store = FAISS.load_local(
                self.vectorstore_path,
                embeddings=self._embedding_function(),
                allow_dangerous_deserialization=True
            )
            return vector_store
        else:
            dim = len(self._embedding_function().embed_query("hello"))
            index = faiss.IndexFlatL2(dim)
            vector_store = FAISS(
                embedding_function=self._embedding_function(),
                index=index,
                docstore=InMemoryDocstore(),
                index_to_docstore_id={}
            )
            return vector_store

    def _get_data(self):
        loader = PyPDFDirectoryLoader(self.data_dir, glob="*.pdf")
        docs = loader.load()
        # pdb.set_trace()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

        texts = text_splitter.split_documents(docs)
        return texts
    
    def save_to_vectorstore(self):
        self._login_hf()
        # load vector store
        print(f"Loading vectorstore")
        vector_store = self._initialize_vectorstore()
        # get the data
        print(f"Getting Chunks!!!")
        chunks = self._get_data()
        # add this data to vectorstore 
        uuids = [str(uuid4()) for _ in range(len(chunks))]
        print(f"Adding to vectorstore")
        # pdb.set_trace()
        start = time.time()
        vector_store.add_documents(documents=chunks, ids=uuids)
        end = time.time()
        print(f"Saving vectorstore")
        print(f"Time Take : {(end - start)/60 :.2f}")
        vector_store.save_local(self.vectorstore_path)
    
    def load_vectorstore(self):
        return self._initialize_vectorstore()

def get_vectorstore():
    vectorstore_path = BASE_DIR / "my_faiss_index"
    data_dir = DATA_DIR = BASE_DIR / "data"
    # pdb.set_trace()
    ds = DataStore(data_dir, vectorstore_path)
    vector_store = ds.load_vectorstore()
    return vector_store


if __name__ == "__main__":
    vectorstore_path = BASE_DIR / "my_faiss_index"
    data_dir = DATA_DIR = BASE_DIR / "data"
    # pdb.set_trace()
    ds = DataStore(data_dir, vectorstore_path)
    ds.save_to_vectorstore()
    print(f"Data Added Successfully!")
