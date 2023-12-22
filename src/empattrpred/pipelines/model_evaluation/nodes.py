"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.14
"""

from sklearn.metrics import confusion_matrix, classification_report, precision_recall_curve
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def train_evaluation(ml_model, x_train, y_train):
    y_pred_train_lr = ml_model.predict(x_train)
    clf_rep = classification_report(y_train, y_pred_train_lr, output_dict=True)
    clf_df = pd.DataFrame(clf_rep, columns=list(clf_rep.keys()))
    for col in clf_df.columns:
        clf_df[col] = clf_df[col].apply('{:.2f}'.format)
    metrics_figure = get_metrics(y_train, y_pred_train_lr)
    return clf_df.T, metrics_figure


def test_evaluation(preds, y_test):
    clf_rep = classification_report(y_test, preds, output_dict=True)
    clf_df = pd.DataFrame(clf_rep, columns=list(clf_rep.keys()))
    for col in clf_df.columns:
        clf_df[col] = clf_df[col].apply('{:.2f}'.format)
    metrics_figure = get_metrics(y_test, preds)
    return clf_df.T, metrics_figure


def get_metrics(actual, predicted):
    cm = confusion_matrix(actual, predicted)
    fig = plt.figure(figsize=(8, 5))
    sns.heatmap(cm, annot=True, fmt=".2f", xticklabels=["Not Attrite", "Attrite"], yticklabels=["Not Attrite", "Attrite"])
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    return fig