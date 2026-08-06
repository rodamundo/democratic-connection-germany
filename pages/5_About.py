import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👤",
    layout="wide"
)

st.title("👤 About")

st.markdown("""
## Beyond Socioeconomic Status

This project investigates whether **feeling left behind in society**
helps explain democratic attitudes in Germany beyond traditional
socioeconomic characteristics such as income and education.

The analysis combines survey data, statistical modelling and the
construction of a novel composite indicator: the **Left Behind Index**.
""")

st.divider()

# ==========================================================
# PROJECT
# ==========================================================

st.header("Project Overview")

st.markdown("""
The project was developed during a Data Analytics Bootcamp and combines
social science theory with quantitative methods.

The workflow included:

- Data cleaning and preprocessing
- Construction of composite indices
- Reliability analysis (Cronbach's Alpha)
- Exploratory Factor Analysis (EFA)
- Correlation analysis
- Multiple Linear Regression (OLS)
- Multicollinearity diagnostics (VIF)
- Robust regression using HC3 standard errors
""")

st.divider()

# ==========================================================
# DATA
# ==========================================================

st.header("Dataset")

st.markdown("""
**German Longitudinal Election Study (GLES) 2025**

- Initial sample: **7,336 respondents**
- Final analytical sample: **5,039 complete observations**
- Country: Germany
- Survey year: 2025
""")

st.divider()

# ==========================================================
# MAIN FINDING
# ==========================================================

st.header("Main Finding")

st.success("""
After controlling for income, education, age, migration background,
political interest and subjective social class, the **Left Behind Index**
remained the strongest predictor of Institutional Trust and Democratic
Satisfaction.

This suggests that perceived social exclusion captures an important
dimension of democratic attitudes beyond traditional socioeconomic variables.
""")

st.divider()

# ==========================================================
# LIMITATIONS
# ==========================================================

st.header("Limitations")

st.warning("""
This project is based on cross-sectional observational data.

The analyses identify statistical associations and should not be interpreted
as evidence of causal relationships.

Future research could investigate whether the Left Behind Index predicts
changes in democratic attitudes over time using longitudinal data.
""")

st.divider()

# ==========================================================
# AUTHOR
# ==========================================================

st.header("Author")

st.markdown("""
**Ricardo Martins Batista**

Sociologist, Programme Manager and Data Analyst based in Berlin.

Professional interests include:

- Democratic participation
- Sustainability
- Social impact
- Public policy
- Data analytics
- Evidence-based decision making
""")

st.divider()

st.caption("""
Developed as a portfolio project during the Data Analytics Bootcamp (2026).

Built with Python, Pandas, Statsmodels, Streamlit and the German Longitudinal Election Study (GLES).
""")