import streamlit as st

st.set_page_config(
    page_title="Beyond Socioeconomic Status",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Beyond Socioeconomic Status")

st.subheader(
    "How Feeling Left Behind Shapes Democratic Attitudes in Germany"
)

st.markdown("---")

st.markdown("""
### Research Question

**To what extent does feeling left behind explain democratic attitudes
beyond traditional socioeconomic characteristics?**

This project investigates whether people's perception of being left behind
helps explain democratic attitudes more strongly than objective socioeconomic
conditions such as income and education.

The analysis uses data from the
**German Longitudinal Election Study (GLES 2025)**.
""")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Initial Respondents", "7,336")

with col2:
    st.metric("Analytical Sample", "5,039")

with col3:
    st.metric("Regression Models", "9")

with col4:
    st.metric("Validated Indices", "2")

st.markdown("---")

st.success("""
### Main Finding

After accounting for household income, education, age, East/West Germany,
migration background, political interest and Subjective Social Class,
the **Left Behind Index** emerged as the strongest predictor of
**Institutional Trust** and **Democratic Satisfaction**.

Its relationship with **Political Representation** was substantially weaker.
""")

st.markdown("---")

st.markdown("""
### Explore the project

Use the navigation menu to view:

- **Research** — research design, variables and analytical sample
- **Results** — comparison of the regression models and main findings
- **Methodology** — index validation and regression diagnostics
- **Policy Implications** — practical interpretation of the findings
- **About** — project background and author
""")

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The analyses describe statistical associations and should not be interpreted
as evidence of causal relationships.
""")