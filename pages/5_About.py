import streamlit as st

st.title("👤 About")

st.markdown("""
## About the project

**Feeling Left Behind: A Hidden Dimension of Democratic Disconnection**

is a data analytics project examining whether subjective perceptions of
social neglect help explain people's relationship with democracy in Germany.

The project combines:

- social science research;
- survey analysis;
- statistical modelling;
- data visualization;
- public-facing communication.
""")

st.divider()

# ============================================================
# DATA
# ============================================================

st.header("Data source")

st.markdown("""
The project uses the:

**German Longitudinal Election Study (GLES 2025)**  
Post-Election Cross-Section  
Study number: **ZA10100**

The GLES is one of Germany's main scientific infrastructures for the study
of elections, political attitudes and electoral behaviour.
""")

st.divider()

# ============================================================
# ANALYTICAL APPROACH
# ============================================================

st.header("Analytical approach")

st.markdown("""
The project includes:

- data cleaning and preprocessing;
- construction of composite indices;
- Cronbach's Alpha;
- Exploratory Factor Analysis;
- Spearman correlations;
- Multiple Linear Regression;
- standardized coefficients;
- Variance Inflation Factor diagnostics;
- HC3 robust standard errors;
- interactive Streamlit visualization.
""")

st.divider()

# ============================================================
# AUTHOR
# ============================================================

st.header("Author")

st.markdown("""
### Ricardo Martins Batista

Berlin, Germany

**Sociologist • Programme Manager • Data Analyst**

Professional interests include:

- Democratic Participation
- Public Policy
- Sustainability
- Social Impact
- Data Analytics
- Evidence-based decision making
""")

st.divider()

# ============================================================
# PROJECT PURPOSE
# ============================================================

st.header("Why this project?")

st.markdown("""
The project was designed not only as a statistical exercise, but as an
example of how data analytics can help translate complex social questions
into evidence that can be understood by both technical and non-technical
audiences.

A central goal of the dashboard is therefore to make the distinction between:

**what the data show**

and

**what the data allow us to conclude**

clear and transparent.
""")

st.divider()

st.caption("""
The analyses use cross-sectional observational data and describe statistical
associations rather than causal relationships.
""")