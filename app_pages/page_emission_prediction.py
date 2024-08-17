import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load
from src.machine_learning.evaluate_clf import clf_performance

def page_emission_prediction_body():

    version = 'v1'
    # Load the trained model and necessary files
    emission_pipe_model = load(f"outputs/ml_pipeline/co2_change/{version}/clf_pipeline.pkl")
    emission_feat_importance = plt.imread(f"outputs/ml_pipeline/co2_change/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/y_train.csv").values.ravel()
    y_test = pd.read_csv(f"outputs/ml_pipeline/co2_change/{version}/y_test.csv").values.ravel()

    st.write("### ML Pipeline: Predict CO2 Emission Increases/Decreases")
    
    # Display pipeline training summary conclusions
    st.info(
        f"* Initially, the project aimed to predict the actual CO2 emission values using a Regressor model, "
        f"but the **regressor performance did not meet the project requirements**: an R2 Score of 0.7 on both train and test sets. \n"
        f"Therefore, I converted the target into a binary classification problem to predict whether CO2 emissions "
        f"will **Increase** or **Decrease**. \n"
        f"* The pipeline was tuned aiming for at least 0.80 Recall on the 'Increase' class for both train and test sets, "
        f"since the primary interest of this project is detecting potential increases in CO2 emissions. \n"
        f"* The pipeline's performance showed 0.90 Recall on the training set and 0.85 on the test set, "
        f"indicating a solid detection capability for emission increases. \n"
        f"* It's important to note that the performance is slightly lower in detecting decreases, "
        f"which should be considered as a limitation of this project."
    )

    # Show pipelines
    st.write("---")
    st.write("#### The ML Pipeline consists of two main steps arranged in series.")
    st.write("* The second step handles feature scaling and modeling.")
    st.write(emission_pipe_model)

    # Show feature importance plot
    st.write("---")
    st.write("* The model was trained using the 'Cumulative_Total' feature.")
    st.image(emission_feat_importance)

    st.write("---")
    st.write("### Understanding Cumulative CO2 Emissions")

    st.write("""
    **Cumulative CO2 Emissions** represent the total amount of CO2 that has been emitted by a country over time, up to a specific year. 
    This cumulative figure is crucial for understanding the long-term impact of a country's emissions on the environment. 
    While yearly emissions show how much CO2 was released in a given year, cumulative emissions provide insight into the overall burden on the atmosphere.
    
    In this model, `Cumulative_Total` was created by summing the total CO2 emissions for each country across all previous years. 
    This feature plays a significant role in predicting whether emissions will increase or decrease in the future, based on historical trends.
    """)

    # Evaluate performance on train and test sets
    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=emission_pipe_model,
                    label_map=["Increase", "Decrease"])

    st.write("---")
    st.write("### Live Prediction")

    # Load the cleaned dataset to get the relevant variables
    cleaned_data = pd.read_csv('outputs\datasets\cleaned\TrainSetCleaned.csv')  # Update with the correct path

    # Let the user select a country
    country = st.selectbox("Select Country", cleaned_data['Country_Original'].unique())
    
    # Let the user select a year, including options beyond 2020
    year_options = list(range(cleaned_data['Year'].min(), cleaned_data['Year'].max() + 1)) + list(range(2021, 2031))
    year = st.selectbox("Select Year", year_options)

    if year <= cleaned_data['Year'].max():
        # Use the existing data if the year is in the dataset
        filtered_data = cleaned_data[(cleaned_data['Country_Original'] == country) & (cleaned_data['Year'] == year)]
        if filtered_data.empty:
            st.warning(f"No data available for {country} in {year}. Please select a different combination.")
            return
    else:
        # Allow the user to input new data if the year is beyond the dataset
        st.write(f"Enter values for {country} in {year}:")
        coal = st.number_input("Enter value for Coal", value=0.0)
        oil = st.number_input("Enter value for Oil", value=0.0)
        gas = st.number_input("Enter value for Gas", value=0.0)
        cement = st.number_input("Enter value for Cement", value=0.0)
        flaring = st.number_input("Enter value for Flaring", value=0.0)
        other = st.number_input("Enter value for Other", value=0.0)
        cumulative_total = coal + oil + gas + cement + flaring + other

    st.write(f"The calculated **Cumulative_Total** for {country} in {year} is: {cumulative_total}")

    # Convert the calculated cumulative total into a DataFrame
    input_data = pd.DataFrame({'Cumulative_Total': [cumulative_total]})

    if st.button("Predict"):
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

        st.write(f"Raw predicted value: {prediction[0]}")
        st.write(f"Threshold used: {threshold}")










