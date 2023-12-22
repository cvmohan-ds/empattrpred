"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def scrub_data(raw_data_df, cols_to_drop):
        
    # Scrub the data by removing unwanted columns which are noise and do not contribute in information flow to model buliding
    scrubbed_data = raw_data_df.drop(columns=cols_to_drop)
    return scrubbed_data

def prepare_data(scrubbed_df, columns_for_dummys):
    
    # Prepare the data to be fed into model
    prepared_data = pd.get_dummies(data=scrubbed_df, columns=columns_for_dummys, drop_first=True)
    prepared_data["OverTime"] = prepared_data.OverTime.map({"Yes":1, "No":0})
    prepared_data["Attrition"] = prepared_data.Attrition.map({"Yes":1, "No":0})
    Y = prepared_data['Attrition']
    X = prepared_data.drop(columns=["Attrition"])

    # Scaling the data (X) to be make it model ready
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    return X_scaled, Y

def creating_train_test_splits(X_scaled, Y, test_size, random_state):
    x_tr, x_te, y_tr, y_te = train_test_split(X_scaled, Y, test_size=test_size, random_state=random_state)
    return x_tr, x_te, y_tr, y_te