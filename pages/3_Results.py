import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 Results")


# ============================================================
# HELPER: PUZZLE VISUAL
# ============================================================

def puzzle_visual(explained, label, value):

    explained_round = round(explained)
    unexplained_round = 100 - explained_round

    with st.container(border=True):

        st.markdown(f"### {label}")

        st.progress(explained / 100)

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "🧩 Accounted for by the model",
                f"≈ {explained_round} / 100"
            )

        with c2:
            st.metric(
                "Not accounted for by the model",
                f"≈ {unexplained_round} / 100"
            )

        st.caption(f"Statistical value: {value}")


# ============================================================
# DATA
# ============================================================

ols_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction"
    ],
    "Traditional Factors": [
        0.088,
        0.085
    ],
    "+ Social Class": [
        0.107,
        0.096
    ],
    "+ Feeling Left Behind": [
        0.276,
        0.222
    ]
})


party_data = pd.DataFrame({
    "Model": [
        "Traditional Factors",
        "+ Social Class",
        "+ Feeling Left Behind"
    ],
    "Pseudo R²": [
        0.0337,
        0.0343,
        0.0462
    ]
})


# ============================================================
# INTRO
# ============================================================

st.header("What are we trying to explain?")

st.markdown("""
The analysis starts with a simple question:

> ### Why do people give different answers about democracy?
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Every respondent receives a trust score.

Some people have low scores.

Some people have high scores.

The model tries to understand:

> **Why are their scores different?**
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
People give different answers about how satisfied they are
with democracy.

The model tries to understand:

> **Why are their answers different?**
""")


with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
Here the question is different.

People answer:

# **Yes / No**

Does a political party represent their views?
""")


st.info("""
### Important

For Institutional Trust and Democratic Satisfaction, we are **not**
dividing respondents into people who trust / do not trust.

We use the full range of responses.

Party Representation is the only Yes/No outcome.
""")

st.divider()


# ============================================================
# PUZZLE INTRODUCTION
# ============================================================

st.header("Think of the differences as a puzzle")

st.markdown("""
Let's start with **Institutional Trust**.

The 5,039 respondents have different trust scores.

Imagine all those differences as a puzzle made of **100 pieces**.

# 🧩 100 pieces = all the observed differences in trust scores

The models try to account for as much of that puzzle as possible
using the information we know about each respondent.
""")

st.divider()


# ============================================================
# MODEL 1
# ============================================================

puzzle_visual(
    8.8,
    "Model 1 — Traditional Factors",
    "R² = 8.8%"
)

st.markdown("""
We start with:

**Income + Education + Age + Region + Migration Background + Political Interest**

Together, these variables help the model account for roughly:

### 🧩 9 of every 100 pieces
""")

st.divider()


# ============================================================
# MODEL 2
# ============================================================

puzzle_visual(
    10.7,
    "Model 2 — + Subjective Social Class",
    "R² = 10.7%"
)

st.markdown("""
Now we add **Subjective Social Class**.

The model moves from roughly:

### 9 → 11 pieces

So Social Class adds some information, but the change is relatively small.
""")

st.divider()


# ============================================================
# MODEL 3
# ============================================================

puzzle_visual(
    27.6,
    "Model 3 — + Feeling Left Behind",
    "R² = 27.6%"
)

st.success("""
### This is the important jump

After Feeling Left Behind is added, the complete model can account for:

# 🧩 ≈ 28 of every 100 pieces

of the observed differences in Institutional Trust scores.

Approximately **72 of 100 pieces remain unaccounted for**
by the variables included in the model.
""")

st.caption("""
The puzzle is a teaching analogy.

Statistically, R² measures the share of observed variation in the outcome
that the model can account for.

The pieces do not represent 100 individual causes.
""")

st.divider()


# ============================================================
# WHAT 27.6% MEANS
# ============================================================

st.header("What does 27.6% actually mean?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### ❌ It does NOT mean")

        st.markdown("""
**27.6% of respondents trust institutions**

or

**trust increased by 27.6%**

or

**Feeling Left Behind alone explains 27.6%**

or

**we discovered 27.6% of the causes of distrust**
""")


with c2:
    with st.container(border=True):

        st.markdown("### ✅ It DOES mean")

        st.markdown("""
The **complete Model 3** can statistically account for:

# 27.6%

of the observed differences in Institutional Trust scores
between respondents.
""")


st.markdown("""
Another way to say it:

> **People have different trust scores. With all the information included
> in Model 3, we can account for about 28 out of every 100 units of
> observed variation between those scores.**
""")

st.divider()


# ============================================================
# OLS COMPARISON
# ============================================================

st.header("Does the same pattern appear for Democratic Satisfaction?")

st.markdown("""
Now that we know what R² means, we can compare the two outcomes
that use the same type of model.
""")

chart_data = ols_data.melt(
    id_vars="Outcome",
    var_name="Model",
    value_name="Share"
)

fig = px.bar(
    chart_data,
    x="Outcome",
    y="Share",
    color="Model",
    barmode="group",
    text="Share",
    title="How Much of the Observed Differences Can Each Model Account For?"
)

fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside",
    hovertemplate=(
        "<b>%{x}</b><br>"
        "%{fullData.name}<br>"
        "%{y:.1%}"
        "<extra></extra>"
    )
)

fig.update_layout(
    height=520,
    xaxis_title="",
    yaxis_title="Share of observed differences accounted for",
    legend_title="",
    yaxis=dict(
        range=[0, 0.35],
        tickformat=".0%"
    )
)

st.plotly_chart(
    fig,
    width="stretch"
)

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Traditional Factors  
**8.8%**

↓

+ Social Class  
**10.7%**

↓

+ Feeling Left Behind  
# **27.6%**
""")

        st.metric(
            "Gain after Feeling Left Behind",
            "+16.9 pp"
        )


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
Traditional Factors  
**8.5%**

↓

+ Social Class  
**9.6%**

↓

+ Feeling Left Behind  
# **22.2%**
""")

        st.metric(
            "Gain after Feeling Left Behind",
            "+12.6 pp"
        )


st.success("""
### The same pattern appears twice

For both outcomes:

**Subjective Social Class adds relatively little.**

**Feeling Left Behind adds substantially more information.**
""")

st.divider()


# ============================================================
# WHY THE JUMP MATTERS
# ============================================================

st.header("What exactly does Feeling Left Behind add?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.metric(
            "Before Feeling Left Behind",
            "10.7%"
        )

        st.markdown("### ↓")

        st.metric(
            "After Feeling Left Behind",
            "27.6%"
        )

        st.metric(
            "Increase in R²",
            "+16.9 percentage points"
        )


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.metric(
            "Before Feeling Left Behind",
            "9.6%"
        )

        st.markdown("### ↓")

        st.metric(
            "After Feeling Left Behind",
            "22.2%"
        )

        st.metric(
            "Increase in R²",
            "+12.6 percentage points"
        )


st.info("""
### Important distinction

The **16.9 and 12.6 percentage-point increases** tell us how much
the model improves when Feeling Left Behind is added.

They do not mean that Feeling Left Behind acting alone explains
exactly 16.9% or 12.6% of the outcome.
""")

st.divider()


# ============================================================
# PARTY REPRESENTATION
# ============================================================

st.header("Party Representation is different")

st.markdown("""
For Party Representation, respondents answer:

# **Yes / No**

Because the outcome is binary, the analysis uses **logistic regression**.

Its model-fit statistic is **McFadden Pseudo R²**, not the same R²
used for Institutional Trust and Democratic Satisfaction.
""")

party_fig = px.bar(
    party_data,
    x="Model",
    y="Pseudo R²",
    text="Pseudo R²",
    title="Party Representation — Model Fit"
)

party_fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside"
)

party_fig.update_layout(
    height=430,
    xaxis_title="",
    yaxis_title="McFadden Pseudo R²",
    yaxis=dict(
        range=[0, 0.06],
        tickformat=".0%"
    )
)

st.plotly_chart(
    party_fig,
    width="stretch"
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Traditional Factors",
    "3.4%"
)

c2.metric(
    "+ Social Class",
    "3.4%"
)

c3.metric(
    "+ Feeling Left Behind",
    "4.6%",
    delta="+1.2 pp"
)

st.warning("""
### Do not interpret 4.6% as “4.6 pieces of the same puzzle”

Pseudo R² does not have the same interpretation as OLS R².

It should also not be numerically compared with the 27.6% and 22.2%
values above.

The useful conclusion here is simpler:

**Feeling Left Behind improves the Party Representation model,
but much less.**
""")

st.divider()


# ============================================================
# DETAILED RESULTS
# ============================================================

st.header("Detailed results")

tab1, tab2, tab3 = st.tabs([
    "Institutional Trust",
    "Democratic Satisfaction",
    "Party Representation"
])


# ============================================================
# TRUST
# ============================================================

with tab1:

    st.subheader("🏛️ Institutional Trust")

    st.markdown("""
Respondents rated eight institutions from:

**1 = Do not trust at all**

to

**11 = Trust completely**
""")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
- Federal Government
- Bundestag
- Political Parties
- Politicians
""")

    with c2:
        st.markdown("""
- Police
- Justice
- Science
- Public-Service Broadcasting
""")

    st.info("""
The eight ratings are averaged into one Institutional Trust score.

There is **no threshold** separating people who “trust” from people
who “do not trust”.
""")

    st.success("""
### Finding

As Feeling Left Behind scores increase,
Institutional Trust tends to decrease.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final R²",
            "27.6%"
        )

        c2.metric(
            "Standardized β",
            "−0.459"
        )

        c3.metric(
            "p-value",
            "< .001"
        )

        st.caption("""
Method: OLS regression with HC3 robust standard errors.

Higher Feeling Left Behind scores are associated with lower
Institutional Trust.
""")


# ============================================================
# SATISFACTION
# ============================================================

with tab2:

    st.subheader("🗳️ Democratic Satisfaction")

    st.markdown("""
Respondents answered:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.info("""
The full 1–4 scale is used.

There is no binary division between satisfied and dissatisfied.

Higher values mean greater dissatisfaction.
""")

    st.success("""
### Finding

As Feeling Left Behind scores increase,
democratic dissatisfaction tends to increase.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final R²",
            "22.2%"
        )

        c2.metric(
            "Standardized β",
            "0.395"
        )

        c3.metric(
            "p-value",
            "< .001"
        )

        st.caption("""
Method: OLS regression with HC3 robust standard errors.

The coefficient is positive because higher values on the outcome
mean greater dissatisfaction.
""")


# ============================================================
# PARTY
# ============================================================

with tab3:

    st.subheader("👥 Party Representation")

    st.markdown("""
Respondents were asked:

> **Does any political party represent your political views well?**

**Yes / No**
""")

    st.info("""
This outcome is genuinely binary.

That is why logistic regression is used.
""")

    st.success("""
### Finding

Higher Feeling Left Behind scores are associated with lower odds
of saying that a political party represents the respondent's views well.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final Pseudo R²",
            "4.6%"
        )

        c2.metric(
            "Logit coefficient",
            "−0.348"
        )

        c3.metric(
            "p-value",
            "< .001"
        )

        st.markdown("""
**Odds ratio: 0.706**

Holding the other variables constant, each one-point increase
in the Left Behind Index is associated with approximately
**29% lower odds** of saying that a political party represents
the respondent's views well.
""")


# ============================================================
# FINAL MESSAGE
# ============================================================

st.divider()

st.header("The main message")

st.success("""
### Feeling Left Behind does not complete the puzzle.

But for Institutional Trust and Democratic Satisfaction,
it adds substantially more information than Subjective Social Class alone.
""")

st.markdown("""
> ## What people have matters.
>
> ## How people feel seen, recognized, served and heard may matter too.
""")

st.warning("""
The analysis shows **associations, not causation**.

The data cannot establish whether Feeling Left Behind causes lower
trust or dissatisfaction, or whether the relationship runs in the
opposite direction.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")