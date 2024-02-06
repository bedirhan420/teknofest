import streamlit as st
import pandas as pd 
import joblib

model = joblib.load('exercise_model.pkl')

def home_component(username):
    st.title(f'Welcome, {username}!')
    st.header("Home Page Content")
    gender = st.sidebar.selectbox("Gender",("Erkek","Kadin"))
    age = st.sidebar.slider("Age",15,85)
    height = st.sidebar.slider("Height",150,200)
    weight = st.sidebar.slider("Weight",45,120)
    diet=st.sidebar.selectbox("Diet",("Normal","Vegan","Glutensiz"))
    sleep = st.sidebar.slider("Sleep time",4,9)
    
    if st.sidebar.button("Update"):
        updated_data = {
            'Gender': gender,
            'Age': age,
            'Height': height,
            'Weight': weight,
            'Diet': diet,
            'SleepTime': sleep
        }
        print("Data updated successfully!")
        st.write("Data updated successfully!")
    
    if st.button("Predict"):
        input_data = {
            'Age': [age],
            'Height': [height],
            'Weight': [weight],
            'SleepTime': [sleep],
            "Gender_Erkek":[1 if gender=="Erkek" else 0],
            "Gender_Kadin":[1 if gender=="Kadin" else 0],
            "Diet_Glutensiz": [1 if diet == "Glutensiz" else 0],
            "Diet_Normal": [1 if diet == "Normal" else 0],
            "Diet_Vegan": [1 if diet == "Vegan" else 0],
        }

        input_df = pd.DataFrame(input_data)
        print(input_df)
        prediction = model.predict(input_df)

        st.write("Predicted Exercise Type:", prediction[0])
