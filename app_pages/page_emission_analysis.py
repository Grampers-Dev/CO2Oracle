import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page_emission_analysis_body():
    st.title("CO2 Emission Analysis")

    # Load the dataset
    df = pd.read_csv('outputs/datasets/cleaned/TrainSetCleaned.csv')
    df.columns = df.columns.str.strip()

    # Ensure I drop all non-numeric columns, including 'Country' and 'Country_Original'
    numeric_df = df.select_dtypes(include=[float, int])

    st.header("Dataset Overview")
    st.write("Here is a quick glance at the dataset used for this analysis:")
    st.write(df.head())

    st.header("Correlation Analysis")
    st.write("""
    We will analyze the correlations between different emission sources and the year to identify significant relationships.
    """)

    # Spearman Correlation Heatmap
    st.subheader("Spearman Correlation")
    try:
        corr_spearman = numeric_df.corr(method='spearman')
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_spearman, annot=True, cmap='coolwarm')
        st.pyplot(plt)
    except ValueError as e:
        st.error(f"Error calculating Spearman correlation: {e}")

    # Pearson Correlation Heatmap
    st.subheader("Pearson Correlation")
    try:
        corr_pearson = numeric_df.corr(method='pearson')
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_pearson, annot=True, cmap='coolwarm')
        st.pyplot(plt)
    except ValueError as e:
        st.error(f"Error calculating Pearson correlation: {e}")

    st.write("""
    These correlation heatmaps help us understand the relationships between the different CO2 emission sources over time.
    """)

# Call this function to display the analysis
page_emission_analysis_body()





