import streamlit as st
import pandas as pd
from joblib import load
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_reg_model import evaluate_regression_model

def page_predict_co2_body():

    version = 'v1'
    
    # Load the trained model and necessary files
    data_cleaning_pipeline = load(f"outputs/ml_pipeline/predict_co2/{version}/reg_pipeline_data_cleaning_feat_eng.pkl")
    regression_pipeline_model = load(f"outputs/ml_pipeline/predict_co2/{version}/reg_pipeline_model.pkl")
    emission_feat_importance = plt.imread(f"outputs/ml_pipeline/predict_co2/{version}/features_importance.png")
    cleaned_data = pd.read_csv('outputs/datasets/cleaned/TrainSetCleaned.csv')
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_co2/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_co2/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predict_co2/{version}/y_train.csv").values.ravel()
    y_test = pd.read_csv(f"outputs/ml_pipeline/predict_co2/{version}/y_test.csv").values.ravel()

    st.write("### ML Pipeline: Predict CO2 Emissions")
    
    # Display pipeline training summary conclusions
    st.info(
        f"* The pipeline was optimized to predict CO2 emissions with high accuracy. "
        f"Performance metrics indicate robust results on both training and test datasets."
    )

    # Show pipelines
    st.write("---")
    st.write("#### Overview of the ML Pipelines")
    st.write(" * The first pipeline is responsible for data cleaning and feature engineering.")
    st.write(data_cleaning_pipeline)

    st.write("* The second pipeline manages feature scaling and modeling.")
    st.write(regression_pipeline_model)

    # Show feature importance plot
    st.write("---")
    st.write("* The model was trained using the 'Total' feature.")
    st.image(emission_feat_importance)

    st.write("---")
    st.write("### Pipeline Performance")
    
    # Evaluate performance on train and test sets
    evaluate_regression_model(X_train=X_train, y_train=y_train,
                              X_test=X_test, y_test=y_test,
                              pipeline=regression_pipeline_model)

    st.write("---")
    st.write("### Understanding CO2 Emissions Prediction")

    st.write("""
    **Predicting CO2 Emissions** is essential for understanding and mitigating the impact of human activities on the environment.
    Accurate predictions can help policymakers, researchers, and individuals make informed decisions to reduce carbon emissions.
             
    In this model, the target variable is the `CO2 Emissions` column, representing the amount of CO2 emitted by a country in a given year.
    The model uses historical data and various features to predict future CO2 emissions accurately.
    """)

    st.write("---")
    st.write("### Feature Importance Analysis")
    st.write("* The model was trained using the following features:")
    st.write(cleaned_data.columns)
    st.write("* The feature importance plot below shows the most influential features in predicting CO2 emissions.")
    st.image(f"outputs/ml_pipeline/predict_co2/{version}/features_importance.png")

    st.write("---")
    st.write("### Understanding Cumulative CO2 Emissions")

    st.write("""
    **Cumulative CO2 Emissions** represent the total amount of CO2 that has been emitted by a country over time, up to a specific year.
    This cumulative figure is crucial for understanding the long-term impact of a country's emissions on the environment.
    While yearly emissions show how much CO2 was released in a given year, cumulative emissions provide insight into the overall burden on the atmosphere.
             
    In this model, `Cumulative_Total` was created by summing the total CO2 emissions for each country across all previous years.
             

    This feature plays a significant role in predicting future CO2 emissions based on historical trends.
    """)

    st.write("---")
    st.write("### Live Prediction")

    # Load the cleaned dataset to get the relevant variables
    cleaned_data = pd.read_csv('outputs/datasets/cleaned/TrainSetCleaned.csv')  # Update with the correct path

    # Let the user select a country and year
    country = st.selectbox("Select Country", cleaned_data['Country_Original'].unique())
    year = st.selectbox("Select Year", cleaned_data['Year'].unique())

    # Filter the dataset based on user selection
    filtered_data = cleaned_data[(cleaned_data['Country_Original'] == country) & (cleaned_data['Year'] == year)]

    if filtered_data.empty:
        st.warning(f"No data available for {country} in {year}. Please select a different combination.")
        return
    
    st.write(f"Selected data for {country} in {year}:")

    # Input widgets for user to enter values for the individual emission sources
    coal = st.number_input("Enter value for Coal", value=float(filtered_data['Coal'].values[0]))
    oil = st.number_input("Enter value for Oil", value=float(filtered_data['Oil'].values[0]))
    gas = st.number_input("Enter value for Gas", value=float(filtered_data['Gas'].values[0]))
    cement = st.number_input("Enter value for Cement", value=float(filtered_data['Cement'].values[0]))
    flaring = st.number_input("Enter value for Flaring", value=float(filtered_data['Flaring'].values[0]))
    other = st.number_input("Enter value for Other", value=float(filtered_data['Other'].values[0]))

    # Calculate the cumulative total based on user inputs
    cumulative_total = coal + oil + gas + cement + flaring + other

    st.write(f"The calculated **Cumulative_Total** based on your input is: {cumulative_total}")

    # Convert the calculated cumulative total into a DataFrame
    cumulative_total_df = pd.DataFrame(data={'Cumulative_Total': [cumulative_total]})
    st.write(cumulative_total_df)

    # Predict CO2 emissions using the pipeline
    predicted_co2 = regression_pipeline_model.predict(cumulative_total_df)
    st.write(f"The predicted CO2 emissions for {country} in {year} is: {predicted_co2[0]:.2f} metric tons.")

    st.write("---")
    st.write("### Conclusion")
    st.write("""
    * The model accurately predicts CO2 emissions based on historical data and various features.
    * The model's performance on the training and test datasets indicates robust results.
    * The cumulative CO2 emissions feature plays a significant role in predicting future emissions.
    * Users can input data to predict CO2 emissions for a specific country and year.
    """)













