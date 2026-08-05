import streamlit as st

st.set_page_config(
    page_title="Beyond Socioeconomic Status",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Beyond Socioeconomic Status")

st.subheader(
    "Why Social Disconnection Matters for Democratic Connection in Germany"
)

st.markdown("---")

st.markdown("""
### Research Question

How do subjective experiences of social disconnection shape democratic attitudes in Germany?

This project investigates whether feeling left behind explains democratic
attitudes more strongly than objective socioeconomic conditions.

The analysis uses data from the **German Longitudinal Election Study (GLES 2025)**.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Respondents", "7,336")

with col2:
    st.metric("Regression Models", "9")

with col3:
    st.metric("Validated Indices", "2")

st.markdown("---")

st.success(
    "Main finding: Social Disconnection is substantially more strongly associated "
    "with Institutional Trust and Democratic Satisfaction than objective socioeconomic characteristics."
)