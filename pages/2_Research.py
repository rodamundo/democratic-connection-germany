import streamlit as st


st.title("🔎 Research")

st.subheader(
    "From the research question to the statistical comparison"
)


# ============================================================
# 1. RESEARCH QUESTION
# ============================================================

st.header("1. Research question")

st.markdown("""
Traditional explanations of democratic attitudes often focus on
people's socioeconomic and demographic position.

This project asks whether this is enough.
""")

st.info("""
# Research question

### Does Feeling Left Behind help us understand democratic attitudes
### beyond income, education, demographic characteristics and
### Subjective Social Class?
""")

st.divider()


# ============================================================
# 2. OUTCOMES
# ============================================================

st.header("2. What exactly are we trying to explain?")

st.markdown("""
Before discussing predictors or regression models, we need to define
the **three outcomes**.

An outcome is simply the thing we are trying to understand.
""")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("## 🏛️ Institutional Trust")

        st.markdown("""
### What does it mean?

How much respondents trust important institutions.

### How is it measured?

Respondents rate **eight institutions** from:

**1 = Do not trust at all**

to

**11 = Trust completely**

The eight ratings are averaged into one
**Institutional Trust score**.
""")

        st.markdown("""
### Institutions

- Federal Government
- Bundestag
- Political Parties
- Politicians
- Police
- Justice
- Science
- Public-Service Broadcasting
""")

        st.caption("Numerical outcome → OLS regression")


with c2:
    with st.container(border=True):

        st.markdown("## 🗳️ Democratic Satisfaction")

        st.markdown("""
### What does it mean?

How satisfied respondents are with the way democracy
works in Germany.

### How is it measured?

One survey response:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**

Therefore:

### Higher score = greater dissatisfaction
""")

        st.caption("Ordered numerical outcome → OLS regression")


with c3:
    with st.container(border=True):

        st.markdown("## 👥 Party Representation")

        st.markdown("""
### What does it mean?

Whether respondents believe that a political party
represents their personal political views well.

### How is it measured?

One survey question:

# Yes / No

There is no continuous representation score.
""")

        st.caption("Binary outcome → logistic regression")


st.success("""
### These are the outcomes

They answer three different questions:

**Do I trust institutions?**

**Am I satisfied with democracy?**

**Does a party represent my views?**
""")

st.divider()


# ============================================================
# 3. PREDICTORS
# ============================================================

st.header("3. What might explain differences in these outcomes?")

st.markdown("""
Now that the outcomes are clear, we can introduce the information
used to try to explain why respondents differ.
""")

st.markdown("""
### Traditional information

💰 Household Income

🎓 Education

🎂 Age

📍 East / West Germany

🌍 Migration Background

🗳️ Political Interest

### Subjective position

🪜 Subjective Social Class

### Subjective social experience

🧩 Feeling Left Behind
""")

st.divider()


# ============================================================
# 4. THREE MODELS
# ============================================================

st.header("4. Why are there three models?")

st.markdown("""
Instead of putting everything into one regression immediately,
the analysis adds information step by step.

This lets us see whether each new layer adds explanatory information.
""")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("## MODEL 1")

        st.markdown("### Traditional factors")

        st.markdown("""
💰 Household Income

🎓 Education

🎂 Age

📍 East / West Germany

🌍 Migration Background

🗳️ Political Interest
""")

        st.markdown("""
**Question:**

How much do these traditional characteristics help us
understand differences in the outcome?
""")


with c2:
    with st.container(border=True):

        st.markdown("## MODEL 2")

        st.markdown("### Model 1 + Subjective Social Class")

        st.markdown("""
Everything from Model 1 remains.

Then we add:

🪜 **Subjective Social Class**
""")

        st.markdown("""
**Question:**

Does knowing where respondents believe they stand socially
add information beyond the traditional characteristics?
""")


with c3:
    with st.container(border=True):

        st.markdown("## MODEL 3")

        st.markdown("### Model 2 + Feeling Left Behind")

        st.markdown("""
Everything from Model 2 remains.

Then we add:

🧩 **Left Behind Index**
""")

        st.markdown("""
**Question:**

Does knowing how left behind respondents feel add information
beyond everything already included?
""")


st.warning("""
### Models are not respondent scores

There is no “Model 1 score” or “Model 2 score”.

The models are simply different **sets of variables entered
into the regression**.
""")

st.divider()


# ============================================================
# 5. 3 × 3 DESIGN
# ============================================================

st.header("5. The 3 × 3 research design")

st.markdown("""
Each of the three model specifications is estimated separately
for each of the three outcomes.
""")

st.markdown("""
| Outcome ↓ / Model → | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| 🏛️ Institutional Trust | Traditional factors | + Social Class | + LBI |
| 🗳️ Democratic Satisfaction | Traditional factors | + Social Class | + LBI |
| 👥 Party Representation | Traditional factors | + Social Class | + LBI |
""")

st.success("""
# 3 outcomes × 3 models = 9 regressions
""")

st.divider()


# ============================================================
# 6. CENTRAL COMPARISON
# ============================================================

st.header("6. What comparison matters most?")

st.markdown("""
The central comparison is **Model 2 versus Model 3**.

Why?

Because Model 2 already knows:

- income;
- education;
- age;
- region;
- migration background;
- political interest;
- Subjective Social Class.

Model 3 then adds only one new construct:

# 🧩 Feeling Left Behind
""")

st.info("""
### Therefore the central question becomes:

If we already know all these characteristics about a respondent,
does knowing **how left behind they feel** help us understand
their democratic attitudes better?
""")

st.divider()


# ============================================================
# 7. EXPECTATION
# ============================================================

st.header("7. Research expectation")

st.markdown("""
The expectation is that stronger Feeling Left Behind will be associated
with greater democratic disconnection.
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
### LBI ↑

### Institutional Trust ↓
""")

with c2:
    st.markdown("""
### LBI ↑

### Democratic Dissatisfaction ↑
""")

with c3:
    st.markdown("""
### LBI ↑

### Party Representation ↓
""")

st.warning("""
These are expected **associations**, not causal claims.
""")

st.divider()


# ============================================================
# 8. LOGIC
# ============================================================

st.header("8. Research logic in one sentence")

st.success("""
### First define what democratic disconnection means,
### then measure Feeling Left Behind,
### then test whether it adds explanatory information
### beyond traditional socioeconomic factors.
""")