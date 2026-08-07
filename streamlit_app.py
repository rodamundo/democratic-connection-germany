import streamlit as st

st.set_page_config(
    page_title="Beyond Socioeconomic Status",
    page_icon="🏛️",
    layout="wide"
)

# ============================================================
# HOME PAGE
# ============================================================

def home():
    st.title("🏛️ Beyond Socioeconomic Status")

    st.subheader(
        "How Feeling Left Behind Shapes Democratic Attitudes in Germany"
    )

    st.divider()

    st.markdown("""
## Research Question

**To what extent does feeling left behind explain democratic attitudes
beyond traditional socioeconomic characteristics?**

This project investigates whether people's perception of being left behind
helps explain democratic attitudes more strongly than objective socioeconomic
characteristics such as household income and education.

The analysis uses data from the
**German Longitudinal Election Study (GLES 2025)**.
""")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Respondents", "7,336")

    with col2:
        st.metric("Analytical Sample", "5,039")

    with col3:
        st.metric("Regression Models", "9")

    with col4:
        st.metric("Composite Indices", "2")

    st.divider()

    st.success("""
## Key Finding

The **Left Behind Index** remained the strongest standardized predictor of
**Institutional Trust** and **Democratic Satisfaction**, even after
controlling for household income, education, age, East/West Germany,
migration background, political interest and Subjective Social Class.

Its association with **Political Representation** was substantially weaker.
""")

    st.divider()

    st.markdown("""
## Explore the Project

Use the navigation menu to explore:

- 📚 **Research** — research design, variables and analytical sample
- 📊 **Results** — regression models and key findings
- 🔬 **Methodology** — index validation and regression diagnostics
- 💡 **Policy Implications** — practical interpretation of the findings
- 👤 **About** — project background and author
""")

    st.divider()

    st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section (ZA10100).

Results describe **statistical associations rather than causal relationships**.
""")


# ============================================================
# NAVIGATION
# ============================================================

home_page = st.Page(
    home,
    title="Home",
    icon="🏠",
    default=True
)

research_page = st.Page(
    "pages/1_Research.py",
    title="Research",
    icon="📚"
)

results_page = st.Page(
    "pages/2_Results.py",
    title="Results",
    icon="📊"
)

methodology_page = st.Page(
    "pages/3_Methodology.py",
    title="Methodology",
    icon="🔬"
)

policy_page = st.Page(
    "pages/4_Policy_Implications.py",
    title="Policy Implications",
    icon="💡"
)

about_page = st.Page(
    "pages/5_About.py",
    title="About",
    icon="👤"
)

pg = st.navigation([
    home_page,
    research_page,
    results_page,
    methodology_page,
    policy_page,
    about_page
])

pg.run()