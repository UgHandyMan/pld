import streamlit as st

def login():
    st.title('Enter Username and Email')
    username = st.text_input('Username')
    email = st.text_input('Email', type='email')
    login_button = st.button('Continue')

    if login_button:
        if username and email:
            return True
        else:
            st.error('Please enter Username and Email')
    return False 

