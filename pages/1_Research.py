import streamlit as st

st.title("📚 Research")

st.markdown("""
## The idea behind the project

Political dissatisfaction is often explained through people's
**economic and social circumstances**.

But people with similar income or education may experience society
very differently.

This project asks whether those subjective experiences also matter.
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
# RESEARCH LOGIC VISUAL
# ============================================================

st.header("The logic of the research")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 1️⃣ Traditional factors")
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
        st.markdown("### 2️⃣ Social position")
        st.markdown("""
Everything in Model 1

**+**

Subjective Social Class
""")

with c3:
    with st.container(border=True):
        st.markdown("### 3️⃣ Feeling Left Behind")
        st.markdown("""
Everything in Models 1 and 2

**+**

Left Behind Index
""")

st.markdown("""
### The key comparison

If the third model improves substantially, Feeling Left Behind is capturing
information that traditional socioeconomic measures do not fully capture.
""")

st.divider()

# ============================================================
# DATASET
# ============================================================

st.header("Where do the data come from?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("""
### German Longitudinal Election Study

**GLES 2025**

Post-Election Cross-Section

Study: **ZA10100**
""")

with c2:
    with st.container(border=True):
        st.metric("Original respondents", "7,336")
        st.metric("Analytical sample", "5,039")

st.markdown("""
The survey was conducted after the **2025 German federal election**.

For the regression comparison, the same analytical sample is used
consistently across the models.
""")

st.divider()

# ============================================================
# CENTRAL CONCEPT
# ============================================================

st.header("The central concept")

st.markdown("""
### Feeling Left Behind

The project does not define being left behind only through material
disadvantage.

Instead, it looks at whether people feel that **people like them**
receive adequate attention, recognition, services and space to express
their views.
""")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 💶")
        st.markdown("**Economic attention**")

with c2:
    with st.container(border=True):
        st.markdown("### 👏")
        st.markdown("**Social recognition**")

with c3:
    with st.container(border=True):
        st.markdown("### 🏥")
        st.markdown("**Basic services**")

with c4:
    with st.container(border=True):
        st.markdown("### 🗣️")
        st.markdown("**Freedom of expression**")

st.info("""
The four exact GLES questions and the construction of the index are
shown in **Results → Left Behind Index**.
""")

st.divider()

# ============================================================
# OUTCOMES
# ============================================================

st.header("What are we trying to explain?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 🏛️ Institutional Trust")
        st.markdown("""
**In simple terms:**

Do people trust important public and political institutions?

**Measurement:**  
8 trust questions combined into one index.
""")

with c2:
    with st.container(border=True):
        st.markdown("### 🗳️ Democratic Satisfaction")
        st.markdown("""
**In simple terms:**

Are people satisfied with the way democracy works in Germany?

**Measurement:**  
1 direct survey question.
""")

with c3:
    with st.container(border=True):
        st.markdown("### 👥 Party Representation")
        st.markdown("""
**In simple terms:**

Does any political party represent the respondent's views well?

**Measurement:**  
1 direct Yes / No question.
""")

st.divider()

# ============================================================
# CONTROLS
# ============================================================

st.header("What else does the analysis take into account?")

st.markdown("""
To avoid confusing Feeling Left Behind with other characteristics,
the regression models also account for:

**Household Income · Education · Age · East/West Germany ·
Migration Background · Political Interest · Subjective Social Class**
""")

st.divider()

# ============================================================
# ANALYTICAL STRUCTURE
# ============================================================

st.header("How many analyses were performed?")

c1, c2, c3 = st.columns(3)

c1.metric("Outcomes", "3")
c2.metric("Models per outcome", "3")
c3.metric("Regression models", "9")

st.caption(
    "3 democratic outcomes × 3 model specifications = 9 regression models."
)

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")