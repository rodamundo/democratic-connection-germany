import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 Results")

st.subheader(
    "From Feeling Left Behind scores to democratic attitudes"
)


# ============================================================
# 1. REMIND THE USER WHAT IS BEING COMPARED
# ============================================================

st.header("1. What are we comparing?")

st.markdown("""
Before looking at statistical models, remember what exists
for each respondent.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("""
### 🧩 Feeling Left Behind Index

Four survey answers

↓

Average

↓

# Score from 1 to 5

**Higher score = higher Feeling Left Behind**
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### Democratic outcomes

🏛️ **Institutional Trust**

🗳️ **Democratic Satisfaction**

👥 **Party Representation**
""")


st.success("""
# First question:

As someone's Feeling Left Behind score increases,
what tends to happen to their democratic attitudes?
""")

st.divider()


# ============================================================
# 2. DIRECTION
# ============================================================

st.header("2. What direction do we find?")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("""
### Institutional Trust

🧩 Feeling Left Behind

# ↑

# ↓

🏛️ Institutional Trust

**Higher Feeling Left Behind is associated with lower trust.**
""")

        st.caption(
            "Standardized β = −0.459 · p < .001"
        )


with c2:

    with st.container(border=True):

        st.markdown("""
### Democratic Satisfaction

🧩 Feeling Left Behind

# ↑

# ↓

🗳️ Satisfaction

**Higher Feeling Left Behind is associated with greater
democratic dissatisfaction.**
""")

        st.caption(
            "Standardized β = 0.395 · p < .001"
        )


with c3:

    with st.container(border=True):

        st.markdown("""
### Party Representation

🧩 Feeling Left Behind

# ↑

# ↓

👥 Party Representation

**Higher Feeling Left Behind is associated with lower odds
of feeling represented.**
""")

        st.caption(
            "Odds ratio = 0.706 · p < .001"
        )


st.info("""
### This answers the direction question.

The coefficients tell us whether higher Feeling Left Behind
is associated with **more or less** of each democratic outcome.

But we still have another question:

**Does Feeling Left Behind tell us something that income,
education, social class and other factors do not already tell us?**
""")

st.divider()


# ============================================================
# 3. WHY THREE MODELS?
# ============================================================

st.header("3. Why do we need three models?")

st.markdown("""
We add information step by step.
""")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("""
### Model 1

## What do we already know?

💰 Income

🎓 Education

🎂 Age

📍 Region

🌍 Migration background

🗳️ Political interest
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### Model 2

## Add:

🪜 **Subjective Social Class**

Does knowing where people believe they belong in society
help us understand their democratic attitudes better?
""")


with c3:

    with st.container(border=True):

        st.markdown("""
### Model 3

## Add:

🧩 **Feeling Left Behind**

Does knowing how left behind people feel add information
beyond everything already included?
""")


st.success("""
# This comparison is the central test.

If Model 3 performs substantially better than Model 2,
Feeling Left Behind is capturing information that the previous
variables did not capture.
""")

st.divider()


# ============================================================
# 4. R2
# ============================================================

st.header("4. What does R² tell us?")

st.markdown("""
People have different Institutional Trust scores.

Some trust institutions more.

Others trust them less.

The model tries to understand **why these scores differ**.
""")

st.info("""
# R² = how much of the differences between people's scores
# the variables in the model can explain.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("""
### A higher R² means:

The information included in the model helps us understand
**more of the differences between respondents**.
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### R² does NOT tell us:

Whether a particular variable is associated with
**higher or lower trust**.

For that, we look at its coefficient.
""")


st.markdown("""
So these are **two different questions**:

**Coefficient → In which direction is the relationship?**

**R² → How much of the differences does the complete model explain?**
""")

st.divider()


# ============================================================
# 5. INSTITUTIONAL TRUST
# ============================================================

st.header("5. Institutional Trust")

st.markdown("""
Let's add information step by step.
""")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("### Model 1")

        st.metric(
            "Differences explained",
            "8.8%"
        )

        st.markdown("""
Income, education, age, region, migration background
and political interest.
""")


with c2:

    with st.container(border=True):

        st.markdown("### Model 2")

        st.metric(
            "Differences explained",
            "10.7%",
            "+1.9 pp"
        )

        st.markdown("""
Everything in Model 1

**+ Subjective Social Class**
""")


with c3:

    with st.container(border=True):

        st.markdown("### Model 3")

        st.metric(
            "Differences explained",
            "27.6%",
            "+16.9 pp"
        )

        st.markdown("""
Everything in Model 2

**+ Feeling Left Behind**
""")


st.success("""
# What happened?

Adding Subjective Social Class:

**8.8% → 10.7%**

Small improvement.

Adding Feeling Left Behind:

**10.7% → 27.6%**

Much larger improvement.
""")


st.markdown("""
### And what direction does Feeling Left Behind have?

# Feeling Left Behind ↑ → Institutional Trust ↓

So the result has **two parts**:

**Direction:** people who feel more left behind tend to trust institutions less.

**Additional information:** including Feeling Left Behind substantially
improves how much of the differences in trust the model can explain.
""")


st.warning("""
### Do not interpret 27.6% as:

❌ 27.6% of respondents trust institutions

❌ Feeling Left Behind reduces trust by 27.6%

❌ Feeling Left Behind alone explains 27.6%

### Correct interpretation:

✅ Model 3 — containing all variables together — explains
27.6% of the variation in Institutional Trust scores.
""")

st.divider()


# ============================================================
# 6. DEMOCRATIC SATISFACTION
# ============================================================

st.header("6. Democratic Satisfaction")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("### Model 1")

        st.metric(
            "Differences explained",
            "8.5%"
        )

        st.caption(
            "Traditional factors"
        )


with c2:

    with st.container(border=True):

        st.markdown("### Model 2")

        st.metric(
            "Differences explained",
            "9.6%",
            "+1.1 pp"
        )

        st.caption(
            "+ Subjective Social Class"
        )


with c3:

    with st.container(border=True):

        st.markdown("### Model 3")

        st.metric(
            "Differences explained",
            "22.2%",
            "+12.6 pp"
        )

        st.caption(
            "+ Feeling Left Behind"
        )


st.success("""
Again, the largest improvement appears when Feeling Left Behind
is added:

# 9.6% → 22.2%
""")


st.markdown("""
### Direction

# Feeling Left Behind ↑ → Democratic Dissatisfaction ↑

So people who feel more left behind tend to report
greater dissatisfaction with democracy.
""")

st.divider()


# ============================================================
# 7. VISUAL COMPARISON
# ============================================================

st.header("7. Compare the two models visually")

model_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Institutional Trust",
        "Institutional Trust",
        "Democratic Satisfaction",
        "Democratic Satisfaction",
        "Democratic Satisfaction"
    ],
    "Model": [
        "Model 1 — Traditional",
        "Model 2 — + Social Class",
        "Model 3 — + Feeling Left Behind",
        "Model 1 — Traditional",
        "Model 2 — + Social Class",
        "Model 3 — + Feeling Left Behind"
    ],
    "R²": [
        0.088,
        0.107,
        0.276,
        0.085,
        0.096,
        0.222
    ]
})


fig = px.bar(
    model_data,
    x="Outcome",
    y="R²",
    color="Model",
    barmode="group",
    text="R²",
    title="How Much of the Differences Between Respondents Does Each Model Explain?"
)

fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside"
)

fig.update_layout(
    height=500,
    xaxis_title="",
    yaxis_title="Variation explained",
    legend_title="",
    yaxis=dict(
        range=[0, 0.32],
        tickformat=".0%"
    )
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.info("""
The important comparison is **Model 2 → Model 3**.

That is where Feeling Left Behind enters the analysis.
""")

st.divider()


# ============================================================
# 8. PARTY REPRESENTATION
# ============================================================

st.header("8. Party Representation")

st.markdown("""
Party Representation is different because respondents answer:

# Yes / No

Therefore, this outcome uses **logistic regression** rather than
the OLS models used for Trust and Satisfaction.
""")


c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Model 1",
        "3.4%"
    )

with c2:
    st.metric(
        "Model 2",
        "3.4%"
    )

with c3:
    st.metric(
        "Model 3",
        "4.6%",
        "+1.2 pp"
    )


st.caption("""
These are McFadden Pseudo R² values and should not be directly
compared with the OLS R² values for Institutional Trust and
Democratic Satisfaction.
""")


with st.container(border=True):

    st.markdown("""
### The easier result to interpret

# Feeling Left Behind ↑

# ↓

# Odds of feeling represented by a party

The odds ratio is **0.706**.

Holding the other variables constant, each one-point increase
in the Left Behind Index is associated with approximately
**29% lower odds** of saying that a political party represents
the respondent's views well.
""")


st.info("""
Feeling Left Behind is therefore also associated with Party
Representation, but the improvement in model fit is much smaller
than for Institutional Trust and Democratic Satisfaction.
""")

st.divider()


# ============================================================
# 9. FINAL SUMMARY
# ============================================================

st.header("9. What did the project find?")

with st.container(border=True):

    st.markdown("""
### 🏛️ Institutional Trust

**More Feeling Left Behind → Lower Institutional Trust**

Adding Feeling Left Behind:

**R² 10.7% → 27.6%**
""")


with st.container(border=True):

    st.markdown("""
### 🗳️ Democratic Satisfaction

**More Feeling Left Behind → Greater Democratic Dissatisfaction**

Adding Feeling Left Behind:

**R² 9.6% → 22.2%**
""")


with st.container(border=True):

    st.markdown("""
### 👥 Party Representation

**More Feeling Left Behind → Lower odds of feeling represented**

The relationship exists, but the improvement in model fit is
much smaller.
""")


st.success("""
# Main takeaway

Feeling Left Behind is associated with greater democratic
disconnection.

And for Institutional Trust and Democratic Satisfaction,
it adds substantial information beyond income, education,
social class and other traditional characteristics.
""")


st.warning("""
These results show **statistical associations, not causation**.
""")


st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")