import streamlit as st

st.set_page_config(
    page_title="Methodology",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Methodology")

st.markdown("""
This project investigates whether **feeling left behind in society**
helps explain democratic attitudes in Germany beyond traditional
socioeconomic characteristics.

The analysis was conducted using data from the **German Longitudinal Election Study (GLES) 2025**.
""")

st.divider()

# ============================================================
# DATA
# ============================================================

st.header("Data")

c1, c2, c3 = st.columns(3)

c1.metric("Dataset", "GLES 2025")
c2.metric("Initial Sample", "7,336")
c3.metric("Final Sample", "5,039")

st.markdown("""
The final analytical sample contains only complete observations for all
variables included in the regression models.
""")

st.divider()

# ============================================================
# LEFT BEHIND INDEX
# ============================================================

st.header("Left Behind Index")

st.markdown("""
The main contribution of this project is the construction of the
**Left Behind Index**.

The index combines four survey questions measuring whether respondents feel:

- Recognized by society
- That politicians pay attention to people like them
- They have access to good public services
- Free to express their political opinions

Responses were reverse-coded where necessary and averaged into a
single continuous index.
""")

st.divider()

# ============================================================
# VALIDATION
# ============================================================

st.header("Index Validation")

c1, c2, c3 = st.columns(3)

c1.metric("Cronbach's α", "0.753")
c2.metric("Eigenvalue (Factor 1)", "2.323")
c3.metric("VIF", "< 2")

st.success("""
### Validation Summary

✔ Good internal consistency (Cronbach's α = 0.753)

✔ Exploratory Factor Analysis supported a one-factor structure.

✔ No meaningful multicollinearity among predictors.

✔ HC3 robust standard errors were used because
heteroscedasticity was detected.
""")

st.divider()

# ============================================================
# REGRESSION MODELS
# ============================================================

st.header("Regression Models")

st.markdown("""
Three nested Ordinary Least Squares (OLS) regression models were estimated.

### Model 1

Traditional socioeconomic and demographic characteristics.

- Household income
- Education
- Age
- East / West Germany
- Migration background
- Political interest

### Model 2

Adds:

- Subjective Social Class

### Model 3

Adds:

- Left Behind Index

This hierarchical strategy allows us to evaluate the additional
explanatory contribution of perceived social exclusion beyond
traditional socioeconomic factors.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES) 2025.

Methodological validation included internal consistency analysis,
exploratory factor analysis, multicollinearity diagnostics,
and HC3 robust standard errors.
""")