import streamlit as st
import re


def user_interface():
    """ User interface for the app """
    st.title("Chatbot Project")
    st.info("Chatbot app implement with the help of lanchain and openai LLM")




def get_user_info():
    """ This function creates the user input field UI with the help of streamlit, collect the user name, phone number and email
        , perform validation check and store the data in their respective variable. 
        Args: None
        Returns:
        user name, user email, phone number 
    """
    # Streamlit input textfield 
    user_name = st.text_input("Enter your name")
    phone_number_input = st.text_input("Enter your Phone Number")
    user_email_input = st.text_input("Enter you Email ID")

    #email validation 
    if  email_validation(user_email_input):
        user_email = user_email_input
    else:
        st.error("Please check the format of your email")
    return user_name, user_email,phone_number_input





def email_validation(email):
    """ This function checks if the user input email is in correct format or not with the help of regular expression
        Args: 
        email : email entered by the user.
        Returns:
        Boolean value: True if the email is valid and false if the email is invalid

    """
    # regular expression pattern for email validation 
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False