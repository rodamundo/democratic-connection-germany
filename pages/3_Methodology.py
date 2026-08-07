import streamlit as st

st.title("🔬 Methodology")

st.markdown("""
## How was the analysis tested?

This page contains the technical evidence behind the findings.

You do **not** need to understand these statistics to follow the Results
page. They are provided here for transparency and reproducibility.
""")

st.divider()

# ============================================================
# WORKFLOW
# ============================================================

st.header("Analysis workflow")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 1️⃣")
        st.markdown("**Clean data**")
        st.caption("Handle survey missing values and prepare variables.")

with c2:
    with st.container(border=True):
        st.markdown("### 2️⃣")
        st.markdown("**Build indices**")
        st.caption("Left Behind and Institutional Trust.")

with c3:
    with st.container(border=True):
        st.markdown("### 3️⃣")
        st.markdown("**Validate**")
        st.caption("Reliability, factor structure and diagnostics.")

with c4:
    with st.container(border=True):
        st.markdown("### 4️⃣")
        st.markdown("**Model outcomes**")
        st.caption("Nine OLS regression models.")

st.divider()

# ============================================================
# SAMPLE
# ============================================================

st.header("Data")

c1, c2, c3 = st.columns(3)

c1.metric("Original sample", "7,336")
c2.metric("Analytical sample", "5,039")
c3.metric("Study", "ZA10100")

st.markdown("""
**Dataset:** German Longitudinal Election Study (GLES 2025)  
**Design:** Post-Election Cross-Section
""")

st.divider()

# ============================================================
# LEFT BEHIND
# ============================================================

st.header("Left Behind Index")

st.markdown("""
The index uses four questions:

`q46a` — Economic attention  
`q46b` — Social recognition  
`q46c` — Infrastructure and basic services  
`q46d` — Freedom of expression
""")

st.markdown("""
The original scale is:

**1 = Strongly agree → 5 = Strongly disagree**

Because agreement corresponds to greater Feeling Left Behind,
the items are reversed:
""")

st.code(
    "reversed_score = 6 - original_score",
    language="python"
)

st.markdown("""
The final index is the **mean of the four reversed items**.
""")

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Cronbach's α",
        "0.753"
    )
    st.caption("Acceptable internal consistency")

with c2:
    st.metric(
        "Factor 1 eigenvalue",
        "2.323"
    )
    st.caption("Supports a dominant common factor")

with st.expander("What does this mean in plain language?"):

    st.markdown("""
The four questions are not identical, but they are related strongly enough
to support treating them as different aspects of one broader concept:
**Feeling Left Behind**.
""")

st.divider()

# ============================================================
# TRUST
# ============================================================

st.header("Institutional Trust Index")

st.markdown("""
Eight GLES variables are averaged:

`q79a` Federal Government  
`q79b` Bundestag  
`q79c` Political Parties  
`q79d` Politicians  
`q79e` Police  
`q79f` Justice  
`q79g` Science  
`q79i` Public-Service Broadcasting
""")

st.info("""
`q79h` — Social Media — is excluded because it was treated as conceptually
different from the public and political institutions included in the index.
""")

st.metric(
    "Cronbach's α",
    "0.889"
)

st.caption("High internal consistency")

st.divider()

# ============================================================
# MODEL STRUCTURE
# ============================================================

st.header("Regression design")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### Model 1")
        st.markdown("""
Income  
Education  
Age  
East / West  
Migration background  
Political interest
""")

with c2:
    with st.container(border=True):
        st.markdown("### Model 2")
        st.markdown("""
Model 1

**+**

Subjective Social Class
""")

with c3:
    with st.container(border=True):
        st.markdown("### Model 3")
        st.markdown("""
Model 2

**+**

Left Behind Index
""")

st.info("""
Three outcomes × three specifications = **nine OLS regression models**.
""")

st.divider()

# ============================================================
# DIAGNOSTICS
# ============================================================

st.header("Regression diagnostics")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric(
            "Predictor VIF",
            "< 2"
        )
        st.markdown("""
No meaningful multicollinearity was detected among the predictors.
""")

with c2:
    with st.container(border=True):
        st.metric(
            "Standard errors",
            "HC3"
        )
        st.markdown("""
Robust standard errors were used because diagnostics indicated
heteroscedasticity.
""")

st.divider()

# ============================================================
# LIMITATIONS
# ============================================================

st.header("What are the limitations?")

with st.container(border=True):
    st.markdown("""
### Cross-sectional data

All variables were measured within the same survey period.

The analysis therefore cannot establish which variable causes another.
""")

with st.container(border=True):
    st.markdown("""
### Subjective perceptions

The Left Behind Index measures what respondents **feel or perceive**.

It does not objectively determine whether society neglects a particular
person or group.
""")

with st.container(border=True):
    st.markdown("""
### Partial explanation

Even the strongest model explains only part of the differences between
respondents.

Other political, social and psychological factors also matter.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")