import streamlit as st

st.set_page_config(
    page_title="Beyond Socioeconomic Status",
    page_icon="🏛️",
    layout="wide"
)

# -----------------------------
# HERO
# -----------------------------

st.title("🏛️ Beyond Socioeconomic Status")

st.subheader(
    "Why Social Disconnection Matters for Democratic Connection in Germany"
)

st.markdown(
"""
This interactive research project investigates whether citizens'
**subjective experiences of social disconnection** explain democratic
attitudes better than objective socioeconomic characteristics.

The analyses are based on the **German Longitudinal Election Study (GLES 2025)**.
"""
)

st.divider()

# -----------------------------
# KEY NUMBERS
# -----------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Respondents",
    "7,336"
)

col2.metric(
    "Regression Models",
    "9"
)

col3.metric(
    "Validated Indices",
    "2"
)

st.divider()

# -----------------------------
# WHY THIS MATTERS
# -----------------------------

st.header("Why this matters")

st.write(
"""
Democratic backsliding is often explained by unemployment,
income inequality or education.

This project explores another possibility:

People may lose confidence in democracy not only because of
their objective socioeconomic conditions, but because they
feel **left behind**, **socially excluded** or **insufficiently
recognized**.
"""
)

st.divider()

# -----------------------------
# MAIN FINDING
# -----------------------------

st.header("Main finding")

st.success(
"""
Across multiple regression models, **Social Disconnection**
emerged as a substantially stronger predictor of
Institutional Trust and Democratic Satisfaction than
objective socioeconomic characteristics such as
income or education.
"""
)

st.divider()

# -----------------------------
# PROJECT STRUCTURE
# -----------------------------

st.header("Explore the project")

st.markdown("""
The research is organized into four sections:

- 📖 Research
- 📊 Results
- 💡 Policy Implications
- 👤 About
""")