# Create a streamlit api to predict chances of survival

import streamlit as st
import pandas as pd
import numpy as np
from model_predictions import predict_survival

st.title('Titanic Survival Prediction')
st.write('This is a simple app to predict the chances of survival of a passenger in the Titanic disaster.')

st.header('User Input Parameters')
# Pclass - variable mapping (1 = First, 2 = Second, 3 = Third)
pclass = st.selectbox('Passenger class', ['First', 'Second', 'Third'], index=None)
# Map pclass to integer
if pclass is not None:
    pclass = {'First': 1, 'Second': 2, 'Third': 3}[pclass]

# Gender - variable mapping (0 = Male, 1 = Female)
gender = st.selectbox('Gender', ['Male', 'Female'], index=None)
if gender is not None:
    gender = gender.lower()

# Age - variable mapping (0 to 80)
age = st.slider('Age', 0, 80, 30)

# Siblings and Spouses - variable mapping (0 to 8)
sibsp = st.slider('Siblings and Spouses', 0, 8, 0)

# Parents and Children - variable mapping (0 to 6)
parch = st.slider('Parents and Children', 0, 6, 0)

# Fare - variable mapping (0 to 550)
fare = st.slider('Fare', 0, 550, 50)

# Embarked - variable mapping (0 = Southampton, 1 = Cherbourg, 2 = Queenstown)

embarked = st.selectbox('Boarding Point', ['Southampton', 'Cherbourg', 'Queenstown'], index=None)
if embarked is not None:
    embarked = {'Southampton': 'S', 'Cherbourg': 'C', 'Queenstown': 'Q'}[embarked]

# map_inputs_to_dict    
map_inputs_to_dict = {'Pclass': pclass, 
                    'Sex': gender, 
                    'Age': age, 
                    'SibSp': sibsp, 
                    'Parch': parch, 
                    'Fare': fare, 
                    'Embarked': embarked,
                    'Cabin' : 'Blah', 
                    'Name' : 'Blah', 
                    'Ticket' : 'Blah',
                    'PassengerId' : 1,
                    'Survived' : 1}

# Create a dataframe based on this dictionary
df = pd.DataFrame(map_inputs_to_dict, index=[0])


# Predict the survival of the passenger
if st.button('Submit for Predictions'):
    survival = predict_survival(df)
    if survival == 1:
        st.write("**Great!** You are likely to survive in the Titanic crash.")
    else:
        st.write("**Sorry**. Please don't board the Titanic. You are most likely not going to survive")





