import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('ans.pkl', 'rb'))
st.title("Health Insurance Cost Predictor")
age = st.number_input("Age",step=1,max_value=100,min_value=0, value=0, format="%d")   
sex = st.selectbox('Sex',['male','female'])
bmi =  st.number_input('Body Mass Index', min_value=0.00, max_value=70.00,value=0.00)
children =st.selectbox("Number of Children",[0,1,2,3,4,5])
smoker=st.selectbox('Are You smoker',['no','yes'])
region=st.selectbox('Region',['southwest','southeast','northwest','northeast'])
if st.button('Predict Cost'):                 
    query=np.array([age,sex,bmi,children,smoker,region],dtype=object)
    query=query.reshape(1,6)
    st.title("The Predicted Cost Of Health Insurance is "+ str(int(model.predict(query))))