import streamlit as st

def page_summary_body():
    st.title("Quick Project Summary")
    st.write("""
    Welcome to the CO2Oracle project! This project aims to analyze and predict CO2 emissions from various sources across different countries.
    
    ### Project Objectives:
    - Understand the patterns and correlations in CO2 emissions data.
    - Predict whether CO2 emissions will increase or decrease in the future.
    - Segment emission sources into meaningful clusters for better management.

    ### Data Overview:
    - The dataset includes emissions data from sources like Cement, Coal, Gas, Oil, Flaring, and Other sources.
    - Geographical data covers multiple countries over several years.
    - Temporal data captures changes in CO2 emissions over time.

    ### Next Steps:
    - Explore the CO2 Emission Analysis page to see how different sources contribute to emissions.
    - Check out the CO2 Emission Prediction page to see our predictive models in action.
    - Learn about our hypotheses and their validation under the Project Hypothesis page.
    - Understand how different emission sources are grouped in the ML: Cluster Analysis page.
    """)
