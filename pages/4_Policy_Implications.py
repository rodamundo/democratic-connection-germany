import streamlit as st

st.set_page_config(
    page_title="Policy Implications",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Policy Implications")

st.markdown("""
The findings suggest that democratic disconnection cannot be understood
through income or education alone.

The results indicate that **feeling left behind in society** is a stronger
predictor of democratic attitudes than several traditional socioeconomic
characteristics.
""")

st.divider()

st.info("""
### Why focus on the Left Behind Index?

The Left Behind Index demonstrated good psychometric properties:

- **Cronbach's α = 0.753**
- **One-factor structure (Eigenvalue = 2.323)**
- **Low multicollinearity (all VIF values < 2)**

These results support its use as a reliable measure of perceived social exclusion.
""")

st.divider()

st.header("What this may mean for democratic organizations")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### 1. Participation is not enough

Creating opportunities for participation may have limited impact if
citizens still feel ignored, excluded or disconnected from society.
""")

    st.markdown("""
### 2. Recognition matters

Democratic initiatives should consider whether people feel their
experiences, identities and opinions are genuinely recognized.
""")

with col2:

    st.markdown("""
### 3. Different outcomes require different strategies

The **Left Behind Index** is strongly associated with
Institutional Trust and Democratic Satisfaction, while showing
a substantially weaker relationship with Political Representation.

Different democratic outcomes may therefore require different policy approaches.
""")

    st.markdown("""
### 4. Go beyond socioeconomic targeting

Income and education remain important indicators,
but they do not fully identify people who feel left behind.
""")

st.divider()

st.warning("""
These findings represent **statistical associations**, not causal relationships.

Although the Left Behind Index is strongly associated with democratic attitudes,
this study does not demonstrate that improving the index would automatically
increase democratic trust or democratic satisfaction.
""")

st.divider()

st.header("Questions for policymakers")

st.markdown("""
- How can democratic institutions identify people who feel left behind?

- Which public policies strengthen citizens' sense of recognition and belonging?

- How can participation processes become more inclusive?

- Which interventions improve democratic trust without increasing political polarization?
""")

st.divider()

st.caption("""
The policy implications presented here are derived from the statistical analyses
conducted in this project and should be interpreted as evidence-informed
recommendations rather than causal conclusions.
""")