"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14

We have selected Logistic Regression after our experimentation which will be trained on future data as well and provide us the prediction in production
"""
from sklearn.linear_model import LogisticRegression
import pandas as pd


def train_model(x_train, y_train):
    lr = LogisticRegression()
    lr.fit(x_train, y_train)
    return lr


def predict(ml_model, x_test):
    preds = ml_model.predict(x_test)
    pred_df = pd.DataFrame(preds, columns=["Attrition"])
    return pred_df