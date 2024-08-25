import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load
from src.machine_learning.evaluate_clf import clf_performance

def page_emission_classification_body():

    version = 'v1'
    # Load the trained model and necessary files
    emission_pipe_model = load(f"outputs/ml_pipeline/co2_change/{version}/clf_pipeline.pkl")
    emission_feat_importance = plt.imread(f"outputs/ml_pipeline/co2_change/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/y_train.csv").values.ravel()
    y_test = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/y_test.csv").values.ravel()

    st.title("🔍 ML Pipeline: Predict CO2 Emission Increases/Decreases")
    
    # Display pipeline training summary conclusions
    st.markdown("""
    ### Project Overview
    This project originally aimed to predict actual CO2 emission values using a regression model. However, the regressor did not meet the performance requirements (an R2 Score of 0.7 on both train and test sets). 
    Consequently, the target was transformed into a **binary classification problem** to predict whether CO2 emissions will **Increase** or **Decrease**.
    """)

    st.info("""
    - **Primary Goal:** Detect potential increases in CO2 emissions with high recall.
    - **Model Performance:**
      - **Training Set:** 0.90 Recall for the 'Increase' class.
      - **Test Set:** 0.85 Recall for the 'Increase' class.
    - **Note:** While the model performs well in detecting increases, its performance is slightly lower for detecting decreases, which should be considered as a limitation.
    """)

    st.markdown("---")
    st.markdown("### ⚙️ The ML Pipeline Structure")
    st.markdown("""
    The ML pipeline consists of two primary steps:
    
    1. **Feature Scaling:** Ensures that features are on the same scale, improving model performance.
    2. **Modeling:** A classification model that predicts whether CO2 emissions will increase or decrease.
    """)
    st.write(emission_pipe_model)

    st.markdown("---")
    st.markdown("### 📊 Feature Importance")
    st.markdown("The model was trained using the **Cumulative_Total** feature, which plays a significant role in predicting emission trends.")
    st.image(emission_feat_importance)

    st.markdown("---")
    st.markdown("### 🌍 Understanding Cumulative CO2 Emissions")
    st.markdown("""
    **Cumulative CO2 Emissions** represent the total amount of CO2 that has been emitted by a country over time, up to a specific year. This cumulative figure is crucial for understanding the long-term impact of a country's emissions on the environment.

    In this model, `Cumulative_Total` was created by summing the total CO2 emissions for each country across all previous years. This feature plays a key role in predicting whether emissions will increase or decrease in the future, based on historical trends.
    """)

    st.markdown("---")
    st.markdown("### 📈 Pipeline Performance Evaluation")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=emission_pipe_model,
                    label_map=["Increase", "Decrease"])

    st.markdown("---")
    st.markdown("### 🔮 Live Prediction")

    # Load the cleaned dataset to get the relevant variables
    cleaned_data = pd.read_csv('outputs/datasets/cleaned/TrainSetCleaned.csv')  # Update with the correct path

    # Let the user select a country and year
    country = st.selectbox("🌍 Select Country", cleaned_data['Country_Original'].unique())
    year = st.selectbox("📅 Select Year", cleaned_data['Year'].unique())

    # Filter the dataset based on user selection
    filtered_data = cleaned_data[(cleaned_data['Country_Original'] == country) & (cleaned_data['Year'] == year)]

    if filtered_data.empty:
        st.warning(f"No data available for {country} in {year}. Please select a different combination.")
        return

    st.write(f"**Selected data for {country} in {year}:**")

    # Input widgets for user to enter values for the individual emission sources
    coal = st.number_input("Enter value for Coal", value=float(filtered_data['Coal'].values[0]))
    oil = st.number_input("Enter value for Oil", value=float(filtered_data['Oil'].values[0]))
    gas = st.number_input("Enter value for Gas", value=float(filtered_data['Gas'].values[0]))
    cement = st.number_input("Enter value for Cement", value=float(filtered_data['Cement'].values[0]))
    flaring = st.number_input("Enter value for Flaring", value=float(filtered_data['Flaring'].values[0]))
    other = st.number_input("Enter value for Other", value=float(filtered_data['Other'].values[0]))

    # Calculate the cumulative total based on user inputs
    cumulative_total = coal + oil + gas + cement + flaring + other

    st.write(f"The calculated **Cumulative_Total** based on your input is: **{cumulative_total:.2f}**")

    # Convert the calculated cumulative total into a DataFrame
    input_data = pd.DataFrame({'Cumulative_Total': [cumulative_total]})

    if st.button("🔍 Predict"):
        # Predict using the pipeline
        prediction = emission_pipe_model.predict(input_data)

        # Convert the prediction to binary using the threshold
        threshold = y_train.mean()  # Example threshold; adjust based on actual model
        prediction_binary = (prediction > threshold).astype(int)

        # Display the prediction result
        if prediction_binary[0] == 1:
            st.success("The model predicts an **Increase** in CO2 emissions.")
        else:
            st.success("The model predicts a **Decrease** in CO2 emissions.")

        st.write(f"**Raw predicted value:** {prediction[0]:.2f}")
        st.write(f"**Threshold used:** {threshold:.2f}")

    st.markdown("---")

# Call the function to render the page
page_emission_classification_body()










