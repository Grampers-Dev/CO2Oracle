import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page_emission_analysis_body():
    st.title("CO2 Emission Analysis")

    # Load the dataset
    df = pd.read_csv('outputs/datasets/cleaned/TrainSetCleaned.csv')
    df.columns = df.columns.str.strip()

    st.header("Dataset Overview")
    st.write("Here is a quick glance at the dataset used for this analysis:")
    st.write(df.head())

    # Select only numeric columns for correlation analysis
    numeric_df = df.select_dtypes(include=[float, int])

    st.header("Correlation Analysis")
    st.write("""
    We will analyze the correlations between different emission sources and the year to identify significant relationships.
    """)

    # Spearman Correlation Heatmap
    st.subheader("Spearman Correlation")
    if numeric_df.empty:
        st.error("No numeric columns available for correlation analysis.")
    else:
        corr_spearman = numeric_df.corr(method='spearman')
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_spearman, annot=True, cmap='coolwarm')
        st.pyplot(plt)

    # Pearson Correlation Heatmap
    st.subheader("Pearson Correlation")
    if numeric_df.empty:
        st.error("No numeric columns available for correlation analysis.")
    else:
        corr_pearson = numeric_df.corr(method='pearson')
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_pearson, annot=True, cmap='coolwarm')
        st.pyplot(plt)

    st.write("""
    These correlation heatmaps help us understand the relationships between the different CO2 emission sources over time.
    """)

# Make sure to call this function in your app
page_emission_analysis_body()



