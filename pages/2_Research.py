import streamlit as st


st.title("🔎 Research")

st.subheader(
    "What are we trying to explain — and what might explain it?"
)

st.divider()


# ============================================================
# 1. RESEARCH QUESTION
# ============================================================

st.header("1. Research question")

st.markdown("""
Traditional explanations of democratic attitudes often focus on
socioeconomic, demographic and political characteristics.

This project asks whether this is enough.
""")

st.info("""
# Research question

### Does Feeling Left Behind help us understand people's relationship
### with democracy beyond traditional socioeconomic, demographic
### and political characteristics?
""")

st.divider()


# ============================================================
# 2. OUTCOMES
# ============================================================

st.header("2. What does “relationship with democracy” mean here?")

st.markdown("""
In this project, it does **not** mean one single thing.

We study three different outcomes.
""")


with st.container(border=True):

    st.markdown("## 🏛️ Outcome 1 — Institutional Trust")

    st.markdown("""
### What are we measuring?

How much respondents trust **eight important institutions**.

Each institution is rated from:

**1 = Do not trust at all**

to

**11 = Trust completely**
""")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
#### Political institutions

- Federal Government
- Bundestag
- Political Parties
- Politicians
""")

    with c2:
        st.markdown("""
#### Other public institutions

- Police
- Justice
- Science
- Public-Service Broadcasting
""")

    st.markdown("""
### How does this become one outcome?

**8 trust ratings**

# ↓

**Calculate the mean**

# ↓

### Institutional Trust score

**1 = very low overall trust**

**11 = very high overall trust**
""")


with st.container(border=True):

    st.markdown("## 🗳️ Outcome 2 — Democratic Satisfaction")

    st.markdown("""
### What are we measuring?

How satisfied respondents are with **how democracy works in Germany**.

This is based on **one survey response**:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.warning("""
### Important

Unlike Institutional Trust, this outcome is **not an average
of several questions**.

The direction is also reversed:

### Higher score = greater dissatisfaction
""")


with st.container(border=True):

    st.markdown("## 👥 Outcome 3 — Party Representation")

    st.markdown("""
### What are we measuring?

Whether respondents feel that **any political party represents
their personal political views well**.

The response is:

# YES / NO
""")

    st.info("""
Because Party Representation is binary, it is analyzed using
**logistic regression** rather than OLS.
""")


st.success("""
### In simple language

🏛️ **Trust:**  
“Do I trust important institutions?”

🗳️ **Satisfaction:**  
“Am I satisfied with how democracy works?”

👥 **Representation:**  
“Is there a party that represents my political views?”
""")

st.divider()


# ============================================================
# 3. WHAT MIGHT EXPLAIN THEM?
# ============================================================

st.header("3. What might explain differences between respondents?")

st.markdown("""
The final analysis compares **two layers of information**.
""")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("### 1️⃣ Traditional characteristics")

        st.markdown("""
💰 Household Income

🎓 Education

🎂 Age

📍 East / West Germany

🌍 Migration Background

🗳️ Political Interest
""")


with c2:
    with st.container(border=True):

        st.markdown("### 2️⃣ Subjective social experience")

        st.markdown("""
🧩 **Feeling Left Behind**

Whether respondents feel that people like them are:

- economically considered;
- recognized;
- adequately served;
- able to express their views.
""")


st.info("""
Subjective Social Class is still explored descriptively in the
Feeling Left Behind section, but it is **not a separate stage in
the final regression design**.
""")

st.divider()


# ============================================================
# 4. MODELS
# ============================================================

st.header("4. How are these explanations tested?")

st.markdown("""
The analysis uses **two nested models**.
""")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("## MODEL 1")

        st.markdown("### Traditional factors")

        st.markdown("""
Income

+ Education

+ Age

+ Region

+ Migration Background

+ Political Interest
""")


with c2:
    with st.container(border=True):

        st.markdown("## MODEL 2")

        st.markdown("""
### Model 1

# +

### 🧩 Feeling Left Behind
""")


st.success("""
### Why compare these two models?

Because the central research question is whether
**Feeling Left Behind adds information beyond traditional factors**.
""")

st.divider()


# ============================================================
# 5. MODEL VS OUTCOME
# ============================================================

st.header("5. Outcomes and models are different things")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("## OUTCOMES")

        st.markdown("""
### What we want to explain

🏛️ Institutional Trust

🗳️ Democratic Satisfaction

👥 Party Representation
""")


with c2:
    with st.container(border=True):

        st.markdown("## MODELS")

        st.markdown("""
### Information used to explain them

**Model 1** → Traditional factors

**Model 2** → Traditional factors + Feeling Left Behind
""")


st.divider()


# ============================================================
# 6. DESIGN
# ============================================================

st.header("6. The complete research design")

st.markdown("""
Each model is estimated separately for each outcome.
""")

st.markdown("""
| Outcome ↓ | Model 1 | Model 2 |
|---|---|---|
| 🏛️ Institutional Trust | Traditional factors | + LBI |
| 🗳️ Democratic Satisfaction | Traditional factors | + LBI |
| 👥 Party Representation | Traditional factors | + LBI |
""")

st.success("""
# 3 outcomes × 2 models = 6 regressions
""")

st.divider()


# ============================================================
# 7. CENTRAL TEST
# ============================================================

st.header("7. What is the central test?")

st.markdown("""
Model 1 already contains:

- Household Income
- Education
- Age
- Region
- Migration Background
- Political Interest

Then Model 2 adds one new construct:

# 🧩 Feeling Left Behind
""")

st.info("""
### Central question

If we already know these traditional characteristics about a respondent,
does knowing **how left behind they feel** help us understand their
democratic attitudes better?
""")

st.divider()


# ============================================================
# 8. EXPECTATIONS
# ============================================================

st.header("8. What relationships do we expect?")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Trust")

        st.markdown("""
Feeling Left Behind ↑

# ↓

Institutional Trust ↓
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Satisfaction")

        st.markdown("""
Feeling Left Behind ↑

# ↓

Democratic Dissatisfaction ↑
""")


with c3:
    with st.container(border=True):

        st.markdown("### 👥 Representation")

        st.markdown("""
Feeling Left Behind ↑

# ↓

Party Representation ↓
""")


st.warning("""
These are hypotheses about **statistical associations**.

The research design does not establish causality.
""")