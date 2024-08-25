import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from feature_engine.discretisation import ArbitraryDiscretiser

sns.set_style("whitegrid")

def page_co2_predictor_body():
    # Load CO2 emissions data
    # Define the load_co2_data() function or import it from another module
    def load_co2_data():
        # implementation goes here
        pass

    df = load_co2_data()

    # Define variables of interest
    vars_to_study = ['Year', 'Coal', 'Oil', 'Gas', 'Cement']

    st.write("### CO2 Emissions Analysis")
    st.info(
        f"* This study aims to understand the patterns of CO2 emissions from various sources. "
        f"By exploring these patterns, we can identify the most influential variables contributing "
        f"to changes in CO2 emissions over time."
    )

    # Inspect data
    if st.checkbox("Inspect CO2 Emissions Data"):
        st.write(
            f"* The dataset contains {df.shape[0]} records and {df.shape[1]} columns. "
            f"Below are the first 10 rows."
        )
        st.write(df.head(10))

    st.write("---")

    # Summary of Correlation Study
    st.write(
        f"* A correlation study was conducted to understand how variables like 'Year' and different "
        f"emission sources are related to total CO2 emissions."
        f"\n The most correlated variables are: **{vars_to_study}**"
    )

    st.info(
        f"The following insights were derived from the correlation analysis: \n"
        f"* Coal is a significant contributor to CO2 emissions. \n"
        f"* Oil and Gas also play a substantial role in the emission levels. \n"
        f"* Emissions vary significantly by year, reflecting changes in energy consumption patterns."
    )

    # Variables Distribution by Year/CO2 Source
    df_eda = df.filter(vars_to_study + ['Total'])

    if st.checkbox("Explore Emissions per Variable"):
        emissions_per_variable(df_eda)

    if st.checkbox("Parallel Plot Analysis"):
        st.write(
            f"* Parallel plots can help visualize the relationships between different emission sources "
            f"and total CO2 emissions."
        )
        parallel_plot_emissions(df_eda)

# Function to plot emissions by variable
def emissions_per_variable(df_eda):
    target_var = 'Total'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)

# Plot categorical data
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var, order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col} Distribution", fontsize=20)
    st.pyplot(fig)

# Plot numerical data
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col} Distribution", fontsize=20)
    st.pyplot(fig)

# Function to create a parallel plot
def parallel_plot_emissions(df_eda):
    # Discretize a numerical variable for better visualization
    tenure_map = [-np.Inf, 6, 12, 18, 24, np.Inf]
    disc = ArbitraryDiscretiser(binning_dict={'Year': tenure_map})
    df_parallel = disc.fit_transform(df_eda)

    fig = px.parallel_categories(df_parallel, color="Total", width=750, height=500)
    st.plotly_chart(fig)


