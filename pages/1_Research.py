import streamlit as st

st.title("📚 Research")

st.markdown("""
## What is this project trying to understand?

Many explanations of political dissatisfaction focus on people's
**economic and social position**:

- income;
- education;
- age;
- region;
- social class.

This project asks whether another dimension also matters:

> **Do people who feel overlooked, unrecognized or left behind relate
> differently to democratic institutions?**
""")

st.divider()

# ============================================================
# RESEARCH QUESTION
# ============================================================

st.header("Research Question")

st.info("""
### To what extent does feeling left behind explain democratic attitudes
### beyond traditional socioeconomic characteristics?
""")

st.markdown("""
The purpose is not to argue that income or education do not matter.

Instead, the analysis asks whether people's **subjective experience of
their place in society adds information beyond these traditional factors**.
""")

st.divider()

# ============================================================
# DATASET
# ============================================================

st.header("Where do the data come from?")

st.markdown("""
The analysis uses the:

### German Longitudinal Election Study — GLES 2025

**Post-Election Cross-Section — ZA10100**

The survey was conducted following the 2025 German federal election.

The original dataset contains:

## **7,336 respondents**

After selecting the variables required for the regression analysis and
using complete observations consistently across the models, the final
analytical sample contains:

## **5,039 respondents**
""")

st.divider()

# ============================================================
# CENTRAL CONCEPT
# ============================================================

st.header("The central concept: Feeling Left Behind")

st.markdown("""
The project focuses on a subjective experience that is different from
simply measuring someone's income.

The GLES asks whether respondents feel that **people like them**:

1. receive too little attention to their economic situation;
2. receive too little recognition for their work;
3. receive insufficient attention regarding access to basic services;
4. are less free to express their opinions publicly.

These four questions are combined into the **Left Behind Index**.
""")

st.info("""
The Results page contains a dedicated **Left Behind Index** tab explaining
each survey question, the original response scale, the reversal of the
scale and the construction of the final index.
""")

st.divider()

# ============================================================
# OUTCOMES
# ============================================================

st.header("What democratic outcomes are studied?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### 🏛️ Institutional Trust

**Question in simple terms:**

Do people trust important public and political institutions?

The analysis combines trust ratings for **eight institutions or groups**
into one index.
""")

with col2:
    st.markdown("""
### 🗳️ Democratic Satisfaction

**Question in simple terms:**

Are people satisfied with how democracy works in Germany?

This outcome comes from **one direct survey question**.
""")

with col3:
    st.markdown("""
### 👥 Party Representation

**Question in simple terms:**

Do people feel that any political party represents their views well?

This also comes from **one direct survey question**.
""")

st.divider()

# ============================================================
# EXPLANATORY VARIABLES
# ============================================================

st.header("What factors are compared?")

st.markdown("""
The analysis compares Feeling Left Behind with several more traditional
characteristics:

- **Household Income**
- **Education**
- **Age**
- **East/West Germany**
- **Migration Background**
- **Political Interest**
- **Subjective Social Class**
""")

st.divider()

# ============================================================
# LOGIC
# ============================================================

st.header("How is the research question tested?")

st.markdown("""
Three versions of the statistical model are estimated for each democratic
outcome.

### Model 1 — Traditional characteristics

Income, education, age, East/West Germany, migration background and
political interest.

### Model 2 — Adds Subjective Social Class

This tests whether people's perceived position in society provides
additional information.

### Model 3 — Adds Feeling Left Behind

The Left Behind Index is added last.

This allows us to ask:

> **Does Feeling Left Behind explain something that income, education
> and social class do not?**
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")