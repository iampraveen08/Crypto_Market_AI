import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(data):
    # Prepare data for training
    X = data[['days']]
    y = data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_future_prices(model, days):
    future_days = np.array(days).reshape(-1, 1)
    predictions = model.predict(future_days)
    return predictions
