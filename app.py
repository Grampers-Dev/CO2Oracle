import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_emission_analysis import page_emission_analysis_body
from app_pages.page_emission_classification import page_emission_classification_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_cluster_analysis import page_predict_co2_body

# Create an instance of the app
app = MultiPage(app_name="CO2Oracle: CO2 Emissions Analysis")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("CO2 Emission Analysis", page_emission_analysis_body)
app.add_page("CO2 Emission Classification", page_emission_classification_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Cluster Analysis", page_predict_co2_body)

# Run the app
app.run()
