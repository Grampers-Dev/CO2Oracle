import streamlit as st

def page_summary_body():
    st.title("🌍 CO2Oracle Project Summary")
    
    st.markdown("""
    Welcome to the **CO2Oracle** project! This initiative focuses on analyzing and predicting CO2 emissions from various sources across different countries, aiming to provide actionable insights for better environmental management.
    """)
    
    st.markdown("### 🎯 **Project Objectives**")
    st.markdown("""
    - 📊 **Understand patterns and correlations** in CO2 emissions data.
    - 🔮 **Predict future CO2 emissions** trends (increase or decrease).
    - 🔍 **Segment emission sources** into meaningful clusters for targeted management.
    """)
    
    st.markdown("### 📈 **Data Overview**")
    st.markdown("""
    - **Emission Sources**: Data includes emissions from Cement, Coal, Gas, Oil, Flaring, and other sources.
    - **Geographical Data**: The dataset covers multiple countries across several years.
    - **Temporal Data**: Captures changes in CO2 emissions over time, providing insights into trends and patterns.
    """)
    
    st.markdown("---")
    
    st.markdown("### 🚀 **Next Steps**")
    st.markdown("""
    - 🔍 **Explore** the [CO2 Emission Analysis](#) page to see how different sources contribute to overall emissions.
    - 🔮 **Check out** the [CO2 Emission Prediction](#) page to see my predictive models in action.
    - 🧠 **Learn about** my hypotheses and their validation under the [Project Hypothesis](#) page.
    - 📊 **Understand** how different emission sources are grouped in the [ML: Cluster Analysis](#) page.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    I hope this project provides valuable insights to help in the global effort to manage and reduce CO2 emissions.
    """)

# Call the function to render the page
page_summary_body()

