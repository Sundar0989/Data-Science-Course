import pandas as pd
import numpy as np
from model_predictions import predict_survival

def run_model_predictions(df):
    predictions = predict_survival(df)
    return predictions

if __name__ == '__main__':
    df = pd.read_excel('Titanic-Dataset.xlsx')
    pred = run_model_predictions(df)
    print(pred)