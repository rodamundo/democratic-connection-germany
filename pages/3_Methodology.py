import streamlit as st

st.title("🔬 Methodology")

st.markdown("""
This page documents the statistical decisions behind the analysis.

The main Results page is designed to be understandable without technical
knowledge. This page provides the additional methodological detail needed
to evaluate the robustness of the analysis.
""")

st.divider()

# ============================================================
# DATA
# ============================================================

st.header("Data")

st.markdown("""
**Dataset:** German Longitudinal Election Study (GLES 2025)  
**Study:** Post-Election Cross-Section  
**Study number:** ZA10100

**Initial sample:** 7,336 respondents  
**Analytical sample:** 5,039 respondents

The same analytical sample is used across the regression models to make
model comparisons consistent.
""")

st.divider()

# ============================================================
# LEFT BEHIND INDEX
# ============================================================

st.header("Left Behind Index")

st.markdown("""
The index contains four GLES variables:

- `q46a` — economic attention;
- `q46b` — social recognition;
- `q46c` — infrastructure and basic services;
- `q46d` — freedom of expression.

The original scale runs from:

**1 = Strongly agree**  
to  
**5 = Strongly disagree**

Because agreement represents greater social disconnection, each item was
reversed using:

`6 - original response`

The four reversed items were then averaged.
""")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Cronbach's α",
        "0.753"
    )

with col2:
    st.metric(
        "Factor 1 eigenvalue",
        "2.323"
    )

st.markdown("""
Cronbach's alpha indicates acceptable internal consistency.

Exploratory Factor Analysis also supports a dominant one-factor structure,
providing evidence that the four items can reasonably be summarized as
one underlying construct.
""")

st.divider()

# ============================================================
# TRUST INDEX
# ============================================================

st.header("Institutional Trust Index")

st.markdown("""
The Institutional Trust Index uses:

- `q79a` — Federal Government
- `q79b` — Bundestag
- `q79c` — Political Parties
- `q79d` — Politicians
- `q79e` — Police
- `q79f` — Justice
- `q79g` — Science
- `q79i` — Public-Service Broadcasting

Each item uses an 11-point trust scale.

`q79h` — Social Media — was excluded because it was treated as
conceptually different from the formal public and political institutions
included in the index.

The remaining eight variables were averaged.
""")

st.metric(
    "Cronbach's α",
    "0.889"
)

st.markdown("""
The resulting value indicates high internal consistency.
""")

st.divider()

# ============================================================
# OUTCOMES
# ============================================================

st.header("Outcome variables")

st.markdown("""
### Institutional Trust

Composite mean index based on eight trust items.

### Democratic Satisfaction

`q119`

“How satisfied are you with the way democracy works in Germany?”

Scale:

1 = Very satisfied  
2 = Fairly satisfied  
3 = Not very satisfied  
4 = Not at all satisfied

### Party Representation

`q141`

“Do you think that any of the parties in Germany represent your personal
political views well?”

1 = Yes  
2 = No
""")

st.divider()

# ============================================================
# REGRESSION DESIGN
# ============================================================

st.header("Regression design")

st.markdown("""
Nine OLS regression models were estimated:

**3 outcomes × 3 model specifications**

### Model 1

Traditional socioeconomic and demographic characteristics:

- Household Income
- Education
- Age
- East/West Germany
- Migration Background
- Political Interest

### Model 2

Model 1 +

- Subjective Social Class

### Model 3

Model 2 +

- Left Behind Index

This nested design makes it possible to examine how much additional
explanatory power each new layer contributes.
""")

st.divider()

# ============================================================
# DIAGNOSTICS
# ============================================================

st.header("Regression diagnostics")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Predictor VIF",
        "< 2"
    )

with col2:
    st.metric(
        "Robust standard errors",
        "HC3"
    )

st.markdown("""
### Multicollinearity

Variance Inflation Factors below 2 indicate no meaningful
multicollinearity among the predictors.

### Heteroscedasticity

Regression diagnostics indicated heteroscedasticity.

For this reason, statistical significance and confidence intervals are
based on **HC3 robust standard errors**.
""")

st.divider()

# ============================================================
# LIMITATIONS
# ============================================================

st.header("Limitations")

st.markdown("""
### Cross-sectional data

All variables were measured within the same survey period.

The analysis therefore identifies statistical associations, not causal
effects.

### Subjective measures

Feeling Left Behind captures respondents' perceptions.

It does not objectively determine whether respondents actually receive
insufficient recognition, services or political voice.

### Model explanatory power

Even the strongest model explains only part of the variation in democratic
attitudes.

Many other social, political and psychological factors are likely to
contribute.
""")

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")