import streamlit as st
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Function to display regression metrics
def regression_metrics(X, y, pipeline):
    # Predict using the pipeline
    y_pred = pipeline.predict(X)

    # Calculate metrics
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    # Display metrics
    st.write('#### Regression Metrics')
    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
    st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
    st.write(f"R-squared (R2): {r2:.2f}")

# Function to evaluate model performance on train and test sets
def reg_performance(X_train, y_train, X_test, y_test, pipeline):
    st.info("Train Set Performance")
    regression_metrics(X_train, y_train, pipeline)

    st.info("Test Set Performance")
    regression_metrics(X_test, y_test, pipeline)
