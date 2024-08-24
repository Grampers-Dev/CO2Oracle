import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

def page_predict_co2_body():
    version = 'v1'
    
    # Load the cleaned training set
    cleaned_train_set = pd.read_csv(f"outputs/datasets/cleaned/TrainSetCleaned.csv")
    
    # Load the trained regression model pipeline
    regression_pipeline_model = load(f"outputs/ml_pipeline/predict_co2/{version}/reg_pipeline_model.pkl")
    
    # Country selection
    country_list = cleaned_train_set['Country'].unique()
    selected_country = st.selectbox("Select Country", options=country_list)
    
    # Display data for the selected country
    country_data = cleaned_train_set[cleaned_train_set['Country'] == selected_country]
    st.write(f"### Data for {selected_country}")
    st.dataframe(country_data)

    # Show pipelines
    st.write("---")
    st.write("#### The ML Pipeline consists of one main step.")
    st.write(regression_pipeline_model)

    # Explanation of Feature Engineering
    st.write("### Explanation of Feature Engineering")
    st.info("""
    In this model, several advanced features were created to improve prediction accuracy:

    - **Lag Features:** Capture trends based on past CO2 emissions.
    - **Rolling Statistics:** Analyze average emissions and their variability over time.
    - **Cumulative Total:** Track the total historical emissions for each country.
    - **Interaction Terms:** Understand the combined effects of different emission sources.
    - **Year-on-Year Change:** Measure how much emissions have changed year over year.
    - **Proportional Features:** Assess the share of emissions coming from specific sources.

    These transformations were applied manually, so the data is preprocessed and ready for the model.
    """)

    # Calculator for Total_Rolling_Std
    st.write("### Calculate Total_Rolling_Std")
    st.info("Use this calculator to estimate the variability of CO2 emissions over the last 3 years.")

    # User inputs for the years
    emission_2018 = st.number_input("Enter CO2 emissions for 2018", min_value=0.0, step=0.01)
    emission_2019 = st.number_input("Enter CO2 emissions for 2019", min_value=0.0, step=0.01)
    emission_2021 = st.number_input("Enter CO2 emissions for 2021", min_value=0.0, step=0.01)

    if st.button("Calculate Total_Rolling_Std"):
        # Calculate mean emissions
        mean_emissions = np.mean([emission_2018, emission_2019, emission_2021])

        # Calculate the differences from the mean and square them
        squared_diffs = [
            (emission_2018 - mean_emissions) ** 2,
            (emission_2019 - mean_emissions) ** 2,
            (emission_2021 - mean_emissions) ** 2
        ]

        # Calculate the mean of squared differences
        mean_squared_diffs = np.mean(squared_diffs)

        # Calculate the standard deviation (Total_Rolling_Std)
        total_rolling_std = np.sqrt(mean_squared_diffs)

        st.write(f"Estimated Total_Rolling_Std: **{total_rolling_std:.3f}**")

    # Explanation of Input Features
    st.write("### Explanation of Input Features")
    explanation_data = {
        "Feature": ["Total_Lag1", "Total_Lag2", "Total_Lag3", "Total_Rolling_Mean", "Total_Rolling_Std", "Cumulative_Total", "Coal_Gas_Interaction", "Oil_Flaring_Interaction", "Year_on_Year_Change", "Coal_Percentage", "Gas_Percentage", "Oil_Percentage", "Flaring_Percentage"],
        "Description": [
            "CO2 emissions from the previous year. Captures recent trends.",
            "CO2 emissions from two years ago. Adds historical context.",
            "CO2 emissions from three years ago. Provides further historical insight.",
            "Average CO2 emissions over the last 3 years. Shows the overall trend.",
            "Variability of CO2 emissions over the last 3 years. Indicates stability or fluctuation.",
            "Total CO2 emissions accumulated over time for the country.",
            "Interaction between coal and gas emissions. Might show combined effects.",
            "Interaction between oil and flaring emissions. Captures joint impact.",
            "Percentage change in CO2 emissions compared to the same time last year.",
            "Percentage of total emissions from coal. Indicates reliance on this source.",
            "Percentage of total emissions from gas. Shows its contribution.",
            "Percentage of total emissions from oil. Reflects its impact.",
            "Percentage of total emissions from flaring. Represents this source's role."
        ]
    }
    explanation_df = pd.DataFrame(explanation_data)
    st.table(explanation_df)

    # User inputs for prediction
    st.write("### Enter Values for Prediction")
    input_data = {}
    for feature in ['Total_Rolling_Std', 'Total', 'Total_Lag1', 'Year_on_Year_Change']:
        input_data[feature] = st.number_input(f"Enter value for {feature}", min_value=0.0, step=0.01)

    # Convert inputs to DataFrame
    input_df = pd.DataFrame([input_data])

    # Prediction
    if st.button("Predict CO2 Emissions"):
        try:
            prediction = regression_pipeline_model.predict(input_df)
            st.write(f"### Predicted CO2 Emission Level for {selected_country}:")
            st.write(f"The predicted CO2 emission level is **{prediction[0]:.2f} metric tons** based on your inputs:")
            for feature in input_data:
                st.write(f"- **{feature.replace('_', ' ')}:** {input_data[feature]}")
            st.write("These features have been carefully engineered to provide a robust prediction for the selected country.")
        except ValueError as e:
            st.error(f"Error: {e}")

    st.write("---")












































   