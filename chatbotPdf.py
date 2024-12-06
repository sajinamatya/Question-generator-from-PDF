# importing required module 

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain

# Loading the enviroment variable which is set for the api key
load_dotenv()


def extract_pdf_text(document):
    """ Extract the text from the document uploaded by the user 
    Args: document
    return: text extracted from the document"""

    text=""
    for pdf in document:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def extract_text_chunks(text):
    """ This function breaks down the text into chunk for further processing for huge document"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3500)
    chunks = text_splitter.split_text(text)
    return chunks


def load_prompt():
    try:
        with open("prompt.txt", "r") as prompt_read:
            prompt = prompt_read.read()
    except FileNotFoundError:
        print("Error: 'prompt.txt' file not found.")
    except PermissionError:
        print("Error: Permission denied when accessing file  'prompt.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    return prompt

def conversation_chain(text):
    """ 
    Creates a chain for the chat model with the proper prompt template to train the model on the basis of user information 
    and document uploaded.

    Args:
    text (str): The text chunk from the document to process.

    Returns:
    str: The generated response from the model.
    """
    
    # Load the prompt 
    prompt_template = load_prompt()

    # Initialize the Google Generative AI
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    # Setup the prompt template with the expected input variable ("text")
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
    
    # Create the QA chain 
    chain = LLMChain(prompt = prompt, llm=model)

    # Pass the text chunk to the chain and get the response

  
    responses = []
    for chunk in text[0:3]:
        response = chain.invoke({"text": chunk}, return_only_outputs=True)
        print(response)
        responses.append(response.get("text"))

    
    # Return the output text from the response (Make sure this key exists in the response)
    return responses




  
    

