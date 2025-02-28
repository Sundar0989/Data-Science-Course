# Create a streamlit api to predict chances of survival

import streamlit as st
import pandas as pd
import numpy as np
from model_predictions import predict_survival, model
import shap
from streamlit_shap import st_shap
import matplotlib.pyplot as plt

st.title('Titanic Survival Prediction')
st.write('This is a simple app to predict the chances of survival of a passenger in the Titanic disaster.')
run_shap_values = False

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
                    'Cabin' : '0', 
                    'Name' : '0', 
                    'Ticket' : '0',
                    'PassengerId' : 1,
                    'Survived' : 1}

# Create a dataframe based on this dictionary
df = pd.DataFrame(map_inputs_to_dict, index=[0])


# Predict the survival of the passenger
if st.button('Submit for Predictions'):
    survival, X = predict_survival(df)
    run_shap_values = True
    if survival == 1:
        st.write("**Great!** You are likely to survive in the Titanic crash.")
    else:
        st.write("**Sorry**. Please don't board the Titanic. You are most likely not going to survive")


if run_shap_values:
    # Explain my predictions
    st.header('Model Interpretation')

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    st.subheader('Force Plot')
    st_shap(shap.force_plot(explainer.expected_value
                    , shap_values
                    , X
                    , matplotlib=True)
                    , height=400, width=1000)

    st.subheader('Feature Importance - Plot 1')
    st_shap(shap.summary_plot(shap_values, X, plot_type="bar", show=False))

    st.subheader('Feature Importance - Plot 2')
    st_shap(shap.plots.waterfall(explainer(X)[0]))

    st.write("""The above plot shows the impact of each feature on the model prediction. 
            The red color indicates that the feature has a positive impact on the survival, 
            while the blue color indicates a negative impact on survival.""")

