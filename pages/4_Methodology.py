import streamlit as st

st.title("🔬 Methodology")

st.subheader(
    "How was the analysis built and tested?"
)

st.markdown("""
This page contains the more technical details behind the analysis.

You do **not** need to understand these statistics to interpret the
main Results page.
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
        st.markdown("**Prepare the data**")
        st.caption(
            "Clean survey responses and handle missing values."
        )

with c2:
    with st.container(border=True):
        st.markdown("### 2️⃣")
        st.markdown("**Construct indices**")
        st.caption(
            "Create Feeling Left Behind and Institutional Trust measures."
        )

with c3:
    with st.container(border=True):
        st.markdown("### 3️⃣")
        st.markdown("**Validate measures**")
        st.caption(
            "Test reliability and factor structure."
        )

with c4:
    with st.container(border=True):
        st.markdown("### 4️⃣")
        st.markdown("**Model outcomes**")
        st.caption(
            "Estimate and compare nine regression models."
        )

st.divider()

# ============================================================
# DATA
# ============================================================

st.header("Data")

c1, c2, c3 = st.columns(3)

c1.metric("Original respondents", "7,336")
c2.metric("Analytical sample", "5,039")
c3.metric("Dataset", "ZA10100")

st.markdown("""
**German Longitudinal Election Study (GLES 2025)**  
Post-Election Cross-Section
""")

st.warning("""
### A note on sampling weights

GLES provides sampling weights (e.g. `w_ipfges`) to correct for known
deviations between the sample and the general population, including
the deliberate oversampling of respondents in East Germany.

**The regression models in this project were estimated without
applying these weights.** Results should therefore be read as
associations within the analytical sample itself, not as
weighted estimates representative of the general German population.
This is particularly relevant for any comparison between East and
West Germany.
""")

st.divider()

# ============================================================
# LEFT BEHIND
# ============================================================

st.header("Left Behind Index")

st.markdown("""
The index uses:

- `q46a` — Economic attention
- `q46b` — Social recognition
- `q46c` — Infrastructure and services
- `q46d` — Freedom of expression

The original scale runs from:

**1 = Strongly agree**

to

**5 = Strongly disagree**

Because agreement represents stronger Feeling Left Behind,
the scale is reversed:
""")

st.code(
    "reversed_score = 6 - original_score",
    language="python"
)

st.markdown("""
The four reversed items are then averaged.
""")

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Cronbach's α",
        "0.753"
    )
    st.caption(
        "Acceptable internal consistency"
    )

with c2:
    st.metric(
        "Factor 1 eigenvalue",
        "2.323"
    )
    st.caption(
        "Supports a dominant common factor"
    )

st.divider()

# ============================================================
# TRUST
# ============================================================

st.header("Institutional Trust Index")

st.markdown("""
The index combines eight questions:

- `q79a` — Federal Government
- `q79b` — Bundestag
- `q79c` — Political Parties
- `q79d` — Politicians
- `q79e` — Police
- `q79f` — Justice
- `q79g` — Science
- `q79i` — Public-Service Broadcasting

The responses are averaged into one Institutional Trust score.
""")

st.info("""
`q79h` — Social Media — was excluded because it was treated as
conceptually different from the public and political institutions
used in the index.
""")

st.metric(
    "Cronbach's α",
    "0.889"
)

st.caption(
    "High internal consistency"
)

st.divider()

# ============================================================
# OUTCOMES
# ============================================================

st.header("Outcome variables")

with st.container(border=True):
    st.markdown("""
### Institutional Trust

Mean index based on eight trust questions.
""")

with st.container(border=True):
    st.markdown("""
### Democratic Satisfaction — `q119`

“How satisfied are you with the way democracy works in Germany?”

1 = Very satisfied  
2 = Fairly satisfied  
3 = Not very satisfied  
4 = Not at all satisfied
""")

with st.container(border=True):
    st.markdown("""
### Party Representation — `q141`

“Do you think that any of the parties in Germany represent your
personal political views well?”

1 = Yes  
2 = No
""")

st.divider()

# ============================================================
# REGRESSION
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
Three outcomes × three specifications = **nine regression models**.

- **Institutional Trust** and **Democratic Satisfaction** are estimated
  with **OLS regression** (continuous / near-continuous outcomes).
- **Party Representation** is a binary outcome (Yes/No), so it is
  estimated with **logistic regression** instead. Its model fit is
  reported as Pseudo R² (McFadden), which is not on the same numeric
  scale as the OLS R² used for the other two outcomes.
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
Robust standard errors were used for the OLS models because
diagnostics indicated heteroscedasticity.
""")

st.divider()

# ============================================================
# LIMITATIONS
# ============================================================

st.header("Limitations")

with st.container(border=True):

    st.markdown("""
### Cross-sectional data

All variables were measured within the same survey period.

The analysis therefore identifies associations rather than causal effects.
""")

with st.container(border=True):

    st.markdown("""
### Possible reverse causality

The direction of the relationship cannot be established from
cross-sectional data alone. It is plausible that low institutional
trust or dissatisfaction with democracy leads people to *report*
feeling left behind, rather than Feeling Left Behind causing lower
trust or satisfaction. Longitudinal or experimental data would be
needed to distinguish between these directions.
""")

with st.container(border=True):

    st.markdown("""
### Subjective perceptions

Feeling Left Behind measures respondents' perceptions.

It does not objectively establish whether society neglects a particular
person or group.
""")

with st.container(border=True):

    st.markdown("""
### Partial explanation

Even the strongest model explains only part of the differences in
democratic attitudes.

Other political, social and psychological factors also matter.
""")

with st.container(border=True):

    st.markdown("""
### Different metrics across outcomes

Because Party Representation required logistic regression, its
Pseudo R² cannot be compared numerically to the OLS R² reported for
Institutional Trust and Democratic Satisfaction. Only the relative
pattern — the size of the gain after adding Feeling Left Behind — is
comparable across outcomes.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")