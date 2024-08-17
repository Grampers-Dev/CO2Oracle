import streamlit as st

def page_project_hypothesis_body():
    st.title("Project Hypothesis and Validation")

    st.header("Hypothesis 1: CO2 Emissions are Increasing Over Time")
    st.write("""
    **Hypothesis:** CO2 emissions from various sources have been increasing over the years.

    **Validation Approach:** We conducted a correlation study (Spearman and Pearson) to investigate the relationship between 'Year' and CO2 emissions from different sources (Coal, Oil, Gas, Cement, Flaring, Other).
    """)

    st.header("Hypothesis 2: Cement Production is a Major Contributor to CO2 Emissions")
    st.write("""
    **Hypothesis:** Emissions from cement production are significantly correlated with the year.

    **Validation Approach:** A correlation study and PPS (Predictive Power Score) were used to validate this hypothesis. This helped determine the strength and nature of the relationship between 'Year' and 'Cement' emissions.
    """)

    st.header("Conclusion")
    st.write("""
    Based on the analysis, these hypotheses were validated, providing a solid foundation for building predictive models.
    """)

