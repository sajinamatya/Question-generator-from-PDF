import PyPDF2
from  chatbotUI import get_user_info

import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
_,_,_,document = get_user_info()
def extract_document(upload_document):
    if upload_document is not None : 
            pdf_read = PyPDF2.PdfReader(upload_document)
            text = ""
            for pages in pdf_read.pages:
                text = text + pages.extract_text()
            text_split =RecursiveCharacterTextSplitter(chunk_size = 1000,
                                                       chunk_overlap = 200,length_function = len)
            chunks =text_split.split_text(text=text)
            embeddings= OpenAIEmbeddings()

            VectorStore = FAISS.from_text(chunks, embedding= embeddings)
            name = upload_document.name[:-4]
            with open (f"{name}.pkl","wb") as b:
                 pickle.dump(VectorStore,b)
       
            