import streamlit as st
from .mysession import session
from .utils import valid_user_arguments



def submit():
    if not valid_user_arguments(session.get('user_args')):
        st.sidebar.error("Please enter complete arguments")
        return

    session.clear()
    input_type = session.get('input_type')
    if input_type == 'Upload a picture':
        session.update('current_page', 'upload_image')
    elif input_type == "Input text":
        session.update('current_page', 'input_text')
    else:
        raise NotImplementedError() # todo

def preprocess_text():
    session.clear()
    session.update('current_page','feedback')

def submit_essay(essay):
    session.update('text',essay)
    session.clear()
    session.update('current_page','feedback')

def go_home():
    session.clear()
    session.update('current_page','home')