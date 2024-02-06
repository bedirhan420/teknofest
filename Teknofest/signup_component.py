# signup_component.py
import streamlit as st    

def signup_component():
    st.header("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type='password')

    if st.button("Sign Up"):
        from main import signup 
        st.session_state.signup_result = signup(new_username, new_password)
