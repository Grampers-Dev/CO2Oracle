import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page_emission_analysis_body():
    st.title("CO2 Emission Analysis")

    # Load the dataset
    st.header("Load Dataset")
    st.write("Loading the dataset and displaying basic information...")
    try:
        df = pd.read_csv('outputs/datasets/cleaned/TrainSetCleaned.csv')
        df.columns = df.columns.str.strip()
        st.write("Dataset successfully loaded.")
    except FileNotFoundError:
        st.error("Dataset not found. Please check the file path.")
        return

    # Display basic dataset information
    st.subheader("Basic Dataset Information")
    st.write("Shape of the dataset:", df.shape)
    st.write(df.info())
    st.write(df.describe())

    # Handle data cleaning and drop non-numeric columns
    st.header("Data Cleaning")
    st.write("Dropping the 'Country' column and selecting only numeric columns.")
    df = df.drop(columns=['Country'], errors='ignore')  # Drop 'Country' column if exists
    numeric_df = df.select_dtypes(include=[float, int])

    st.write("Here is a quick glance at the cleaned dataset:")
    st.write(numeric_df.head())

    st.header("Correlation Analysis")
    st.write("""
    I will analyze the correlations between different emission sources and the year to identify significant relationships.
    """)

    # Spearman Correlation Heatmap
    st.subheader("Spearman Correlation")
    try:
        corr_spearman = numeric_df.corr(method='spearman')
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_spearman, annot=True, cmap='coolwarm', fmt=".2f")
        st.pyplot(plt)
    except ValueError as e:
        st.error(f"Error calculating Spearman correlation: {e}")

    # Pearson Correlation Heatmap
    st.subheader("Pearson Correlation")
    try:
        corr_pearson = numeric_df.corr(method='pearson')
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_pearson, annot=True, cmap='coolwarm', fmt=".2f")
        st.pyplot(plt)
    except ValueError as e:
        st.error(f"Error calculating Pearson correlation: {e}")

    st.write("""
    These correlation heatmaps help us understand the relationships between the different CO2 emission sources over time.
    """)

# Call this function to display the analysis
page_emission_analysis_body()







