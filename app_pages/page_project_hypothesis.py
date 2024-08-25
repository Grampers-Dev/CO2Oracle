import streamlit as st

def page_project_hypothesis_body():
    st.title("🔬 Project Hypothesis and Validation")

    st.markdown("### 📈 Hypothesis 1: CO2 Emissions are Increasing Over Time")
    st.markdown("""
    **Hypothesis:** CO2 emissions from various sources have been increasing over the years.

    **Validation Approach:** 
    - I conducted a **correlation study** using both **Spearman** and **Pearson** methods to investigate the relationship between 'Year' and CO2 emissions from different sources, including:
        - 🟦 Coal
        - 🟧 Oil
        - 🟨 Gas
        - 🟩 Cement
        - 🟥 Flaring
        - 🟪 Other
    """)

    st.markdown("### 🏗️ Hypothesis 2: Cement Production is a Major Contributor to CO2 Emissions")
    st.markdown("""
    **Hypothesis:** Emissions from cement production are significantly correlated with the year.

    **Validation Approach:** 
    - A **correlation study** and **Predictive Power Score (PPS)** analysis were performed to validate this hypothesis. These methods helped determine:
        - The **strength** of the relationship between 'Year' and 'Cement' emissions.
        - The **nature** of this relationship, indicating how strongly cement production impacts CO2 emissions over time.
    """)

    st.markdown("### 📝 Conclusion")
    st.markdown("""
    The validation of these hypotheses provides a solid foundation for building accurate predictive models. These insights are crucial for understanding the trends and key contributors to CO2 emissions, guiding further analysis and model development.
    """)

# Call the function to render the page
page_project_hypothesis_body()

