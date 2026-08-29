import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE
# ============================================================

st.title("📊 Results")

st.subheader(
    "What changes when Feeling Left Behind is added?"
)

st.markdown("""
The analysis compares two models for each democratic outcome:

**Model 1 — Traditional factors**

versus

**Model 2 — Traditional factors + Feeling Left Behind**
""")


st.info("""
### Two simple questions

**1. Does Feeling Left Behind add useful information?**

We compare the model **before and after adding LBI**.

**2. What happens as Feeling Left Behind increases?**

We examine whether **trust, satisfaction and representation
tend to increase or decrease**.

*The technical measures behind these comparisons are R² / Pseudo R²
and regression coefficients / Odds Ratios.*
""")

st.divider()


# ============================================================
# DATA
# ============================================================

comparison = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Model 1": [
        0.0846,
        0.0797,
        0.0333
    ],
    "Model 2": [
        0.2629,
        0.2120,
        0.0465
    ]
})


# ============================================================
# 1. OUTCOMES
# ============================================================

st.header("1. What exactly are we trying to explain?")


with st.container(border=True):

    st.markdown("## 🏛️ Institutional Trust")

    st.markdown("""
Respondents rated **8 institutions** from:

**1 = Do not trust at all**

to

**11 = Trust completely**
""")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
**Political institutions**

- Federal Government
- Bundestag
- Political Parties
- Politicians
""")

    with c2:
        st.markdown("""
**Other public institutions**

- Police
- Justice
- Science
- Public-Service Broadcasting
""")

    st.markdown("""
### 8 ratings → mean → Institutional Trust score

**Higher score = greater Institutional Trust**
""")


with st.container(border=True):

    st.markdown("## 🗳️ Democratic Satisfaction")

    st.markdown("""
Respondents were asked how satisfied they are with
the way democracy works in Germany.

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.warning("""
Higher values mean **greater dissatisfaction**.

So:

**Score ↑ → Democratic Satisfaction ↓**
""")


with st.container(border=True):

    st.markdown("## 👥 Party Representation")

    st.markdown("""
Respondents were asked whether any political party represents
their personal political views well.

# Yes / No
""")

    st.info("""
Because this outcome is binary, it is analyzed using
**binary logistic regression** rather than OLS.
""")


st.divider()


# ============================================================
# 2. MODELS
# ============================================================

st.header("2. What are the two models?")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("## Model 1")

        st.markdown("### Traditional factors")

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

        st.markdown("## Model 2")

        st.markdown("""
### Everything in Model 1

# +

### 🧩 Feeling Left Behind Index
""")


st.success("""
### The comparison is simple

**What do traditional factors tell us?**

# ↓

**What changes when Feeling Left Behind is added?**
""")

st.divider()


# ============================================================
# 3. MODEL FIT
# ============================================================

st.header("3. What changes when Feeling Left Behind is added?")


display_table = pd.DataFrame({
    "Outcome": [
        "🏛️ Institutional Trust",
        "🗳️ Democratic Satisfaction",
        "👥 Party Representation"
    ],
    "Model 1": [
        "8.46%",
        "7.97%",
        "3.33%"
    ],
    "Model 2 (+ LBI)": [
        "26.29%",
        "21.20%",
        "4.65%"
    ],
    "Change": [
        "+17.83 pp",
        "+13.23 pp",
        "+1.32 pp"
    ]
})

st.dataframe(
    display_table,
    width="stretch",
    hide_index=True
)


st.caption("""
Institutional Trust and Democratic Satisfaction use OLS R².

Party Representation uses McFadden Pseudo R² and should not be
directly compared numerically with the other two outcomes.
""")


# ============================================================
# GRAPH
# ============================================================

plot_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Institutional Trust",
        "Democratic Satisfaction",
        "Democratic Satisfaction",
        "Party Representation",
        "Party Representation"
    ],
    "Model": [
        "Traditional Factors",
        "+ Feeling Left Behind",
        "Traditional Factors",
        "+ Feeling Left Behind",
        "Traditional Factors",
        "+ Feeling Left Behind"
    ],
    "Model Fit": [
        0.0846,
        0.2629,
        0.0797,
        0.2120,
        0.0333,
        0.0465
    ]
})


fig = px.bar(
    plot_data,
    x="Outcome",
    y="Model Fit",
    color="Model",
    barmode="group",
    text="Model Fit",
    title="What Changes When Feeling Left Behind Is Added?"
)

fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside",
    hovertemplate=(
        "<b>%{x}</b><br>"
        "%{fullData.name}<br>"
        "Model fit: %{y:.2%}"
        "<extra></extra>"
    )
)

fig.update_layout(
    height=520,
    xaxis_title="",
    yaxis_title="Model fit",
    legend_title="",
    yaxis=dict(
        range=[0, 0.31],
        tickformat=".0%"
    )
)

st.plotly_chart(
    fig,
    width="stretch"
)


st.warning("""
### Important

Party Representation uses **McFadden Pseudo R²**.

Trust and Satisfaction use ordinary **OLS R²**.

The meaningful comparison is therefore primarily **within each outcome**:
before and after Feeling Left Behind is added.
""")

st.divider()


# ============================================================
# 4. LBI VISUAL SUMMARY
# ============================================================

st.header("4. What does Feeling Left Behind add?")


st.subheader("A. Change in model fit")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Traditional factors

# 8.46%

# ↓

### + Feeling Left Behind

# ↓

# 26.29%
""")

        st.metric(
            "Increase in R²",
            "+17.83 pp"
        )


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
Traditional factors

# 7.97%

# ↓

### + Feeling Left Behind

# ↓

# 21.20%
""")

        st.metric(
            "Increase in R²",
            "+13.23 pp"
        )


with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
Traditional factors

# 3.33%

# ↓

### + Feeling Left Behind

# ↓

# 4.65%
""")

        st.metric(
            "Increase in Pseudo R²",
            "+1.32 pp"
        )


st.success("""
The increase is particularly large for **Institutional Trust**
and **Democratic Satisfaction**.

The improvement for **Party Representation** is much smaller.
""")


# ============================================================
# DIRECTION
# ============================================================

st.subheader("B. In which direction is LBI associated with each outcome?")

st.markdown("""
Now we ask a different question:

> **As Feeling Left Behind increases, what tends to happen?**
""")


c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("""
## 🧩 LBI ↑

# ↓

## 🏛️ Trust ↓
""")

        st.markdown("""
People who feel more left behind tend to report
**lower Institutional Trust**.
""")

        st.metric(
            "LBI coefficient",
            "−0.994"
        )

        st.caption(
            "OLS coefficient · p < .001"
        )


with c2:
    with st.container(border=True):

        st.markdown("""
## 🧩 LBI ↑

# ↓

## 🗳️ Satisfaction ↓
""")

        st.markdown("""
People who feel more left behind tend to be
**less satisfied with democracy**.
""")

        st.metric(
            "LBI coefficient",
            "+0.353"
        )

        st.caption(
            "OLS coefficient · p < .001. Positive because higher "
            "q119 values mean greater dissatisfaction."
        )


with c3:
    with st.container(border=True):

        st.markdown("""
## 🧩 LBI ↑

# ↓

## 👥 Representation ↓
""")

        st.markdown("""
People who feel more left behind have **lower odds**
of saying that a party represents their views well.
""")

        st.metric(
            "Odds Ratio",
            "0.705"
        )

        st.caption(
            "Approximately 29.5% lower odds per one-point "
            "increase in LBI · p < .001"
        )


st.info("""
### A technical detail

The numbers shown above are not all measured on the same scale.

Trust and Satisfaction use OLS coefficients.

Party Representation uses an Odds Ratio from logistic regression.

That is why the three effect numbers should not be compared
directly with one another.
""")

st.divider()


# ============================================================
# 5. INSTITUTIONAL TRUST
# ============================================================

st.header("5. 🏛️ Institutional Trust")

st.markdown("""
### What was actually measured?

Average trust across:

- Federal Government
- Bundestag
- Political Parties
- Politicians
- Police
- Justice
- Science
- Public-Service Broadcasting

Each rating ranges from **1 to 11**.
""")


c1, c2 = st.columns(2)

c1.metric(
    "Model 1 R²",
    "8.46%"
)

c2.metric(
    "Model 2 R²",
    "26.29%",
    "+17.83 pp"
)


st.success("""
### Main interpretation

Feeling Left Behind adds substantial explanatory information
for differences in Institutional Trust.
""")


st.error("""
# LBI ↑ → Institutional Trust ↓
""")


with st.expander("Technical evidence"):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Model 2 R²",
        "26.29%"
    )

    c2.metric(
        "Adjusted R²",
        "26.20%"
    )

    c3.metric(
        "LBI coefficient",
        "−0.994"
    )

    c4.metric(
        "p-value",
        "< .001"
    )

    st.caption("""
N = 5,653.

Method: multiple OLS regression.

Model 1 Adjusted R² = 8.37%.
""")


st.divider()


# ============================================================
# 6. SATISFACTION
# ============================================================

st.header("6. 🗳️ Democratic Satisfaction")

st.markdown("""
Respondents were asked:

> **“How satisfied are you with the way democracy works in Germany?”**

**1 = Very satisfied**

to

**4 = Not at all satisfied**

Higher values therefore mean **greater dissatisfaction**.
""")


c1, c2 = st.columns(2)

c1.metric(
    "Model 1 R²",
    "7.97%"
)

c2.metric(
    "Model 2 R²",
    "21.20%",
    "+13.23 pp"
)


st.success("""
### Main interpretation

Feeling Left Behind adds substantial explanatory information
for differences in Democratic Satisfaction.
""")


st.error("""
# LBI ↑ → Democratic Dissatisfaction ↑

or:

# LBI ↑ → Democratic Satisfaction ↓
""")


with st.expander("Technical evidence"):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Model 2 R²",
        "21.20%"
    )

    c2.metric(
        "Adjusted R²",
        "21.10%"
    )

    c3.metric(
        "LBI coefficient",
        "+0.353"
    )

    c4.metric(
        "p-value",
        "< .001"
    )

    st.caption("""
N = 5,676.

Method: multiple OLS regression.

Model 1 Adjusted R² = 7.87%.

The positive LBI coefficient reflects the coding of q119:
higher values mean greater dissatisfaction.
""")


st.divider()


# ============================================================
# 7. PARTY REPRESENTATION
# ============================================================

st.header("7. 👥 Party Representation")

st.markdown("""
Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**

# Yes / No
""")


st.info("""
Because the outcome is binary, Party Representation is modeled
using **binary logistic regression**.
""")


c1, c2 = st.columns(2)

c1.metric(
    "Model 1 Pseudo R²",
    "3.33%"
)

c2.metric(
    "Model 2 Pseudo R²",
    "4.65%",
    "+1.32 pp"
)


st.success("""
### Main interpretation

Feeling Left Behind is statistically associated with
Party Representation, but it adds much less model fit here
than for Trust or Satisfaction.
""")


st.error("""
# LBI ↑ → odds of Party Representation ↓
""")


with st.expander("Technical evidence"):

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Model 2 Pseudo R²",
        "4.65%"
    )

    c2.metric(
        "Odds Ratio",
        "0.705"
    )

    c3.metric(
        "p-value",
        "< .001"
    )

    st.markdown("""
Holding the other variables constant, each one-point increase
in the Left Behind Index is associated with approximately
**29.5% lower odds** of saying that a political party represents
the respondent's views well.
""")

    st.caption("""
N = 5,096.

Logit coefficient = −0.349.

Calculation: 1 − 0.7052 = 0.2948, approximately 29.5%.

Method: binary logistic regression.
""")


st.divider()


# ============================================================
# 8. FINAL COMPARISON
# ============================================================

st.header("8. What is the overall result?")


summary = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Traditional factors": [
        "8.46%",
        "7.97%",
        "3.33%"
    ],
    "+ LBI": [
        "26.29%",
        "21.20%",
        "4.65%"
    ],
    "Gain": [
        "+17.83 pp",
        "+13.23 pp",
        "+1.32 pp"
    ],
    "Direction": [
        "LBI ↑ → Trust ↓",
        "LBI ↑ → Satisfaction ↓",
        "LBI ↑ → Representation ↓"
    ]
})

st.dataframe(
    summary,
    width="stretch",
    hide_index=True
)


st.warning("""
Party Representation uses McFadden Pseudo R².

Its gain should not be treated as numerically equivalent to the
OLS R² gains for Trust and Satisfaction.
""")


st.success("""
# Main finding

Feeling Left Behind adds substantial explanatory information
for **Institutional Trust** and **Democratic Satisfaction**.

Higher Feeling Left Behind is associated with:

### 🏛️ lower Institutional Trust

### 🗳️ lower Democratic Satisfaction

### 👥 lower odds of Party Representation
""")

st.divider()


# ============================================================
# 9. R2 CAUTION
# ============================================================

st.header("9. Why not rely on R² alone?")

st.markdown("""
Ordinary R² naturally cannot decrease when a predictor is added.

Therefore, an increase in R² by itself is not enough to establish
that Feeling Left Behind is substantively important.
""")

st.info("""
### We therefore look at several pieces of evidence together:

**1. Does model fit change?**

**2. Does Adjusted R² also improve?**

**3. In which direction is LBI associated with the outcome?**

**4. Is that association statistically significant?**
""")


c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Trust")

        st.markdown("""
R²:

**8.46% → 26.29%**

Adjusted R²:

**8.37% → 26.20%**
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Satisfaction")

        st.markdown("""
R²:

**7.97% → 21.20%**

Adjusted R²:

**7.87% → 21.10%**
""")


st.success("""
The improvement remains almost unchanged after adjusting for
the additional predictor.
""")

st.divider()


# ============================================================
# 10. PLAIN LANGUAGE
# ============================================================

st.header("10. The result in plain language")

st.info("""
Imagine two respondents who are similar in income, education, age,
region, migration background and political interest.

Knowing **how left behind they feel** still gives us substantial
additional information about how much they trust institutions and
how satisfied they are with democracy.

For Party Representation, Feeling Left Behind is also related to
the outcome, but the improvement in model fit is considerably smaller.
""")

st.divider()


# ============================================================
# 11. METHODOLOGICAL NOTES
# ============================================================

st.header("11. Important methodological notes")


with st.container(border=True):

    st.markdown("### ⚖️ Survey weights")

    st.markdown("""
The GLES dataset provides survey weights, including `w_ipfges`.

These weights were **not applied to the regression models in this project**.

The results should therefore be interpreted as statistical associations
within the analytical sample rather than as weighted population estimates
for the German electorate.
""")


with st.container(border=True):

    st.markdown("### 🔄 Reverse causality")

    st.markdown("""
Because the data are cross-sectional, the direction of the relationship
cannot be established.

The results are consistent with:

**Feeling Left Behind → lower trust / lower democratic satisfaction**

but the reverse mechanism is also possible:

**existing distrust or dissatisfaction → stronger perceptions of
Feeling Left Behind**

Both may also be influenced by other factors not included in the models.
""")


st.warning("""
### Association ≠ causation

The analysis identifies statistical relationships.

It cannot establish that Feeling Left Behind causes lower Institutional
Trust, lower Democratic Satisfaction or lower Party Representation.
""")


st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Complete-case samples are outcome-specific:

Institutional Trust: N = 5,653

Democratic Satisfaction: N = 5,676

Party Representation: N = 5,096
""")
