import streamlit as st

st.title("📚 Research")

st.subheader(
    "What are we trying to understand?"
)

st.markdown("""
Political dissatisfaction is often explained through people's
**economic and social circumstances**.

Income, education and social class clearly matter.

But this project asks whether another dimension may also provide
important information:

> **How people experience their place in society.**
""")

st.divider()

# ============================================================
# QUESTION
# ============================================================

st.header("The research question")

st.info("""
### To what extent does Feeling Left Behind explain democratic attitudes
### beyond traditional socioeconomic characteristics?
""")

st.markdown("""
In simpler terms:

> **If two people have similar income, education and social backgrounds,
> could differences in whether they feel recognized and included help
> explain why they relate differently to democracy?**
""")

st.divider()

# ============================================================
# DATA
# ============================================================

st.header("Where do the data come from?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("""
### German Longitudinal Election Study

**GLES 2025**

Post-Election Cross-Section

Study number: **ZA10100**
""")

with c2:
    with st.container(border=True):
        st.metric(
            "Original respondents",
            "7,336"
        )

        st.metric(
            "Analytical sample",
            "5,039"
        )

st.markdown("""
The survey was conducted after the **2025 German federal election**.

The same analytical sample is used consistently across the regression
models so that comparisons between models remain meaningful.
""")

st.divider()

# ============================================================
# WHAT ARE DEMOCRATIC ATTITUDES?
# ============================================================

st.header("What do we mean by 'democratic attitudes'?")

st.markdown("""
The project does not treat democracy as one single attitude.

Instead, it examines **three different dimensions**.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
**Simple question:**

> Do people trust important public and political institutions?

The analysis combines trust ratings for **eight institutions or groups**
into one index.
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
**Simple question:**

> Are people satisfied with how democracy works in Germany?

This outcome comes from **one direct survey question**.
""")

with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
**Simple question:**

> Does any political party represent the person's political views well?

This outcome also comes from **one direct survey question**.
""")

st.divider()

# ============================================================
# WHAT ELSE IS INCLUDED?
# ============================================================

st.header("What else does the analysis take into account?")

st.markdown("""
To distinguish Feeling Left Behind from other characteristics,
the analysis also includes:

- **Household Income**
- **Education**
- **Age**
- **East / West Germany**
- **Migration Background**
- **Political Interest**
- **Subjective Social Class**
""")

st.divider()

# ============================================================
# MODELS
# ============================================================

st.header("How is the question tested?")

st.markdown("""
The analysis adds information in three stages.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 1️⃣ Traditional Factors")

        st.markdown("""
Income  
Education  
Age  
East / West Germany  
Migration background  
Political interest
""")

with c2:
    with st.container(border=True):

        st.markdown("### 2️⃣ + Social Class")

        st.markdown("""
Everything in the first model

**+**

Subjective Social Class
""")

with c3:
    with st.container(border=True):

        st.markdown("### 3️⃣ + Feeling Left Behind")

        st.markdown("""
Everything above

**+**

Left Behind Index
""")

st.info("""
### Why do this in stages?

If the model improves substantially only after Feeling Left Behind
is added, this suggests that the index captures information not already
represented by income, education and social class.
""")

st.divider()

# ============================================================
# MODELS NUMBER
# ============================================================

st.header("How many regression analyses were performed?")

c1, c2, c3 = st.columns(3)

c1.metric("Democratic outcomes", "3")
c2.metric("Models per outcome", "3")
c3.metric("Total regression models", "9")

st.caption("""
3 democratic outcomes × 3 model specifications = 9 regression models.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")