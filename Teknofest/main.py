# main.py
import streamlit as st
import json
import os
from home_component import home_component

USER_DATA_FILE = 'user_data.json'

if 'signin_result' not in st.session_state:
    st.session_state.signin_result = {'success': False, 'user': None}
if 'show_homepage' not in st.session_state:
    st.session_state.show_homepage = False

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_user_data(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def signup(username, password):
    users = load_user_data()
    if any(user['username'] == username for user in users):
        return False, 'Username already exists. Please choose a different one or sign in.'
    else:
        users.append({'username': username, 'password': password})
        save_user_data(users)
        return True, 'Account created successfully! You can now sign in.'

def signin(username, password):
    users = load_user_data()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True, user
    return False, None

def main():

    # Sidebar for navigation
    if st.session_state.show_homepage:
        home_component(st.session_state.signin_result['user']['username'])
        return
    else:
        st.title('Hello')
        page = st.sidebar.radio("Select Action", ["Sign In", "Sign Up"])
        
        if page == "Sign In":
            from signin_component import signin_component
            signin_component()
            if st.session_state.signin_result['success']:
                st.session_state.show_homepage = True
                st.sidebar.empty()

        elif page == "Sign Up":
            from signup_component import signup_component
            signup_component() 
            if hasattr(st.session_state, 'signup_result') and st.session_state.signup_result[0]:
                st.success(st.session_state.signup_result[1])


if __name__ == '__main__':
    main()
