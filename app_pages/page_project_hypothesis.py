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
**Initial Hypothesis:** Emissions from cement production are significantly correlated with the year.

**Revised Understanding:**
- The initial focus was on cement production as a major contributor to CO2 emissions. However, after multiple analyses and attempts to validate this hypothesis, it became clear that cement production was not as strongly correlated with CO2 emissions over time as initially thought.
- Due to significant missing values, particularly in the 'Per Capita' column, it was necessary to drop this variable from the analysis. This led to further exploration and the creation of custom-engineered variables to better understand the dataset and the factors contributing to CO2 emissions.

**Validation Approach:** 
- A **correlation study** and **Predictive Power Score (PPS)** analysis were performed to validate this hypothesis. These methods helped determine:
    - The **strength** of the relationship between 'Year' and 'Cement' emissions.
    - The **nature** of this relationship, indicating how strongly cement production impacts CO2 emissions over time.
- Despite the initial hypothesis, the refined analysis revealed that other factors, potentially highlighted by the custom-engineered variables, play a more significant role in driving CO2 emissions.

### 📝 Conclusion
The revised understanding of the dataset highlights the importance of flexibility in analysis and the need to adapt hypotheses based on emerging data insights. The custom variables engineered during the analysis provided a deeper understanding of the factors contributing to CO2 emissions, laying a more accurate foundation for building predictive models and guiding further analysis.
""")


