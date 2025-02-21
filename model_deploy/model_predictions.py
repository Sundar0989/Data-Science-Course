# Import model objects and mapping variables
# Import necessary packages

# import data and test the function
import pandas as pd
import numpy as np
import pickle

l = pickle.load(open('model.pkl', 'rb'))
model, sex_dict, embarked_dict = l

# Model deployment

# Gather all variable treatment in one function
def data_preprocessing(df, sex_dict=sex_dict, embarked_dict=embarked_dict):
    
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Sex'] = df['Sex'].map(sex_dict)
    df['Embarked'] = df['Embarked'].map(embarked_dict)
    df['Embarked'].fillna(0, inplace=True)
    df.drop(['Cabin', 'Name', 'Ticket'], axis=1, inplace=True)
    
    return df   

# Create a function to predict the survival of a passenger based on the model
def predict_survival(df):

    df = data_preprocessing(df)
    X = df.drop(['PassengerId', 'Survived'], axis=1)
    prediction = model.predict(X)
    return prediction