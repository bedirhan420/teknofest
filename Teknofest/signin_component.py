# signin_component.py
import streamlit as st

def signin_component():
    st.header("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Sign In"):
        from main import signin
        success, user = signin(username, password)
        st.session_state.signin_result = {'success': success, 'user': user}
