import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👤",
    layout="wide"
)

st.title("👤 About the Project")

st.markdown(
    """
    This project was developed as part of a Data Analytics bootcamp and explores
    the relationship between Social Disconnection and democratic attitudes in Germany.
    """
)

st.divider()

st.header("About the analysis")

st.markdown(
    """
    The project uses data from the **German Longitudinal Election Study (GLES 2025)**.

    The analytical workflow includes:

    - construction of two composite indices;
    - reliability assessment using Cronbach's Alpha;
    - descriptive analysis;
    - Spearman correlations;
    - nested OLS regression models;
    - multicollinearity assessment using VIF;
    - standardized coefficients.
    """
)

st.divider()

st.header("About the author")

st.markdown(
    """
    **Ricardo Martins Batista**

    Sociologist, programme manager and data analyst based in Berlin.

    His professional background includes sustainability, social impact,
    democratic participation, mobility, training and international programme management.
    """
)

st.divider()

st.header("Methodological caution")

st.markdown(
    """
    The results are based on cross-sectional observational data.

    The analyses identify statistical associations and should not be interpreted
    as evidence of causal relationships.
    """
)

st.divider()

st.caption(
    "Project: Beyond Socioeconomic Status — Social Disconnection and Democratic Connection in Germany"
)