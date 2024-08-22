import streamlit as st
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def regression_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    st.write("#### Regression Metrics")
    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
    st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
    st.write(f"R-squared (R2): {r2:.2f}")

def evaluate_regression_model(X_train, y_train, X_test, y_test, pipeline):
    st.info("Train Set Performance")
    y_train_pred = pipeline.predict(X_train)
    regression_metrics(y_train, y_train_pred)

    st.info("Test Set Performance")
    y_test_pred = pipeline.predict(X_test)
    regression_metrics(y_test, y_test_pred)
