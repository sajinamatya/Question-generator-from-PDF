import streamlit as st
import json
from chatbotPdf import extract_pdf_text,extract_text_chunks,conversation_chain
def main():
    """ Main UI of the chatbot app"""
    st.title("PDF question generator Chatbot Project")
    st.info("Chatbot app implement with the help of lanchain and gemini LLM")

    with st.form (key='myform2'):
        pdf_docs = st.file_uploader("Upload your PDF Files ", accept_multiple_files=True,type=['pdf'])
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            with st.spinner("Processing please wait..."):
                #when the document is uploaded all this function is called for further text processing requried for getting the response to the user
                raw_text = extract_pdf_text(pdf_docs)
                text_chunks = extract_text_chunks(raw_text)
               
                
                output = conversation_chain(text_chunks)

                for  response in output:
                    try:
                        parsed_json = json.loads(response)
                        st.write(parsed_json)
                    except json.JSONDecodeError:
                        st.write(response)
                  
               
                st.success("Done")

   
   



main()