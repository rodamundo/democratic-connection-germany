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
The results are presented separately for the three democratic outcomes.

For each one, we ask two different questions:

1. **Does adding Feeling Left Behind improve the model's explanatory power?**
2. **In which direction is Feeling Left Behind associated with the outcome?**
""")

st.info("""
### Two statistics — two different questions

**R² / Pseudo R²** → How much explanatory information does the model contain?

**Coefficient / Odds Ratio** → In which direction is Feeling Left Behind associated with the outcome?
""")

st.divider()


# ============================================================
# DATA — SINGLE SOURCE OF TRUTH FOR THIS PAGE
# ============================================================

comparison = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Model 1": [
        0.088,
        0.085,
        0.0337
    ],
    "Model 2": [
        0.107,
        0.096,
        0.0343
    ],
    "Model 3": [
        0.276,
        0.222,
        0.0462
    ]
})

gain_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Before LBI": [
        0.107,
        0.096,
        0.0343
    ],
    "After LBI": [
        0.276,
        0.222,
        0.0462
    ]
})


# ============================================================
# 1. REMIND THE READER WHAT WE ARE EXPLAINING
# ============================================================

st.header("1. What exactly are we trying to explain?")

st.markdown("""
Before looking at percentages, remember that these are
**three different democratic outcomes**.
""")


# ------------------------------------------------------------
# TRUST
# ------------------------------------------------------------

with st.container(border=True):

    st.markdown("## 🏛️ Institutional Trust")

    st.markdown("""
### The question

**How much does a respondent trust important institutions?**

Each respondent rated **8 institutions** from:

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


# ------------------------------------------------------------
# SATISFACTION
# ------------------------------------------------------------

with st.container(border=True):

    st.markdown("## 🗳️ Democratic Satisfaction")

    st.markdown("""
### The question

**How satisfied are respondents with the way democracy works in Germany?**

One survey response:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.warning("""
### Important direction

Higher values mean **greater dissatisfaction**.

So:

**Score ↑ → Democratic Satisfaction ↓**
""")


# ------------------------------------------------------------
# REPRESENTATION
# ------------------------------------------------------------

with st.container(border=True):

    st.markdown("## 👥 Party Representation")

    st.markdown("""
### The question

**Does any political party represent the respondent's personal
political views well?**

The answer is:

# Yes / No
""")

    st.info("""
Because this outcome is binary, it is analyzed with
**logistic regression** rather than OLS.
""")


st.divider()


# ============================================================
# 2. REMIND THE READER WHAT THE MODELS ARE
# ============================================================

st.header("2. What are Model 1, Model 2 and Model 3?")

c1, c2, c3 = st.columns(3)


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
### Model 1

# +

### 🪜 Subjective Social Class
""")


with c3:

    with st.container(border=True):

        st.markdown("## Model 3")

        st.markdown("""
### Model 2

# +

### 🧩 Feeling Left Behind Index
""")


st.info("""
The models are **nested**.

Everything in Model 1 remains in Model 2.

Everything in Model 2 remains in Model 3.

This allows us to see what additional information is gained
when each new layer is introduced.
""")

st.divider()


# ============================================================
# 3. MODEL FIT ACROSS ALL THREE OUTCOMES
# ============================================================

st.header("3. How does explanatory power change across the models?")

st.markdown("""
For Institutional Trust and Democratic Satisfaction, the values below
are **OLS R²**.

For Party Representation, they are **McFadden Pseudo R²**
from logistic regression.
""")


# ------------------------------------------------------------
# TABLE
# ------------------------------------------------------------

display_table = pd.DataFrame({
    "Outcome": [
        "🏛️ Institutional Trust",
        "🗳️ Democratic Satisfaction",
        "👥 Party Representation"
    ],
    "Model 1": [
        "8.8%",
        "8.5%",
        "3.37%"
    ],
    "Model 2": [
        "10.7%",
        "9.6%",
        "3.43%"
    ],
    "Model 3": [
        "27.6%",
        "22.2%",
        "4.62%"
    ]
})

st.dataframe(
    display_table,
    width="stretch",
    hide_index=True
)


st.caption("""
Institutional Trust and Democratic Satisfaction: OLS R².

Party Representation: McFadden Pseudo R².

Two decimal places are shown for Party Representation because
3.37% and 3.43% would both appear as 3.4% if rounded to one decimal.
""")


# ------------------------------------------------------------
# VISUAL GRAPH
# ------------------------------------------------------------

plot_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Institutional Trust",
        "Institutional Trust",
        "Democratic Satisfaction",
        "Democratic Satisfaction",
        "Democratic Satisfaction",
        "Party Representation",
        "Party Representation",
        "Party Representation"
    ],
    "Model": [
        "Model 1",
        "Model 2",
        "Model 3",
        "Model 1",
        "Model 2",
        "Model 3",
        "Model 1",
        "Model 2",
        "Model 3"
    ],
    "Model Fit": [
        0.088,
        0.107,
        0.276,
        0.085,
        0.096,
        0.222,
        0.0337,
        0.0343,
        0.0462
    ]
})

fig = px.bar(
    plot_data,
    x="Outcome",
    y="Model Fit",
    color="Model",
    barmode="group",
    text="Model Fit",
    title="How Model Fit Changes as Information Is Added"
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
        range=[0, 0.32],
        tickformat=".0%"
    )
)

st.plotly_chart(
    fig,
    width="stretch"
)


st.warning("""
### Important

The Party Representation bars use **Pseudo R²**, while Trust and
Satisfaction use ordinary **OLS R²**.

Therefore, their absolute heights should not be directly compared
as if they were the same statistic.

The meaningful comparison is primarily **within each outcome**
as Model 1 → Model 2 → Model 3.
""")

st.divider()


# ============================================================
# 4. VISUAL SUMMARY OF THE LBI
# ============================================================

st.header("4. What does Feeling Left Behind add?")

st.markdown("""
There are **two parts** to the answer.

First, we can see how much model fit increases when LBI is added.

Then, separately, we can see the **direction of the relationship**
between LBI and each democratic outcome.
""")


# ============================================================
# 4A. ADDITIONAL EXPLANATORY INFORMATION
# ============================================================

st.subheader("A. How much additional explanatory information appears after adding LBI?")

c1, c2, c3 = st.columns(3)


with c1:

    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Model 2

# 10.7%

# ↓

### + Feeling Left Behind

# ↓

Model 3

# 27.6%
""")

        st.metric(
            "Increase in explanatory power",
            "+16.9 pp"
        )

        st.caption("OLS R²")


with c2:

    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
Model 2

# 9.6%

# ↓

### + Feeling Left Behind

# ↓

Model 3

# 22.2%
""")

        st.metric(
            "Increase in explanatory power",
            "+12.6 pp"
        )

        st.caption("OLS R²")


with c3:

    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
Model 2

# 3.43%

# ↓

### + Feeling Left Behind

# ↓

Model 3

# 4.62%
""")

        st.metric(
            "Increase in model fit",
            "+1.19 pp"
        )

        st.caption("McFadden Pseudo R²")


st.success("""
### What stands out?

The increase after adding Feeling Left Behind is particularly large
for **Institutional Trust** and **Democratic Satisfaction**.

The improvement for **Party Representation** is much smaller.
""")


# ============================================================
# 4B. DIRECTION
# ============================================================

st.subheader("B. In which direction is Feeling Left Behind associated with each outcome?")

st.markdown("""
Now forget R² for a moment.

The question here is simply:

> **As Feeling Left Behind increases, what tends to happen to each outcome?**
""")


c1, c2, c3 = st.columns(3)


with c1:

    with st.container(border=True):

        st.markdown("""
## 🧩 LBI ↑

# ↓

## 🏛️ Institutional Trust ↓
""")

        st.markdown("""
People who feel more left behind tend to report
**lower trust in institutions**.
""")

        st.metric(
            "Standardized LBI coefficient",
            "−0.459"
        )

        st.caption(
            "OLS standardized β · p < .001"
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
**less satisfied with how democracy works**.
""")

        st.metric(
            "Standardized LBI coefficient",
            "+0.395"
        )

        st.caption(
            "OLS standardized β · p < .001. "
            "Positive because higher q119 values mean greater dissatisfaction."
        )


with c3:

    with st.container(border=True):

        st.markdown("""
## 🧩 LBI ↑

# ↓

## 👥 Party Representation ↓
""")

        st.markdown("""
People who feel more left behind have **lower odds**
of saying that a party represents their views well.
""")

        st.metric(
            "Odds Ratio",
            "0.706"
        )

        st.caption(
            "Logistic regression · approximately 29% lower odds "
            "per one-point increase in LBI · p < .001"
        )


st.info("""
### Why isn't there one bar chart comparing these three numbers?

Because they are **not measured on the same statistical scale**.

Trust and Satisfaction use standardized OLS coefficients.

Party Representation uses logistic regression and an Odds Ratio.

Putting −0.459, +0.395 and 0.706 into one bar chart would make
the visual comparison misleading.
""")


st.success("""
### The visual takeaway

**More Feeling Left Behind is associated with:**

🏛️ **less Institutional Trust**

🗳️ **less Democratic Satisfaction**

👥 **lower odds of Party Representation**

The relationship exists across all three outcomes, but the
increase in model explanatory power is much larger for
Trust and Democratic Satisfaction.
""")

st.divider()


# ============================================================
# 5. INSTITUTIONAL TRUST DETAIL
# ============================================================

st.header("5. 🏛️ Institutional Trust")

st.markdown("""
### What was actually measured?

Respondents rated their trust in:

- Federal Government
- Bundestag
- Political Parties
- Politicians
- Police
- Justice
- Science
- Public-Service Broadcasting

Each rating ranges from **1 to 11**.

The eight ratings are averaged into one Institutional Trust score.
""")


c1, c2, c3 = st.columns(3)

c1.metric(
    "Model 1 R²",
    "8.8%"
)

c2.metric(
    "Model 2 R²",
    "10.7%"
)

c3.metric(
    "Model 3 R²",
    "27.6%"
)


st.markdown("""
Adding Subjective Social Class increases explanatory power from
**8.8% to 10.7%**.

Adding Feeling Left Behind then increases it from
**10.7% to 27.6%**.
""")


st.success("""
### Main interpretation

Feeling Left Behind adds substantial explanatory information
for differences in Institutional Trust between respondents.
""")


st.error("""
# LBI ↑ → Institutional Trust ↓
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

    st.caption(
        "Method: multiple OLS regression."
    )


st.divider()


# ============================================================
# 6. DEMOCRATIC SATISFACTION DETAIL
# ============================================================

st.header("6. 🗳️ Democratic Satisfaction")

st.markdown("""
### What was actually measured?

Respondents were asked:

> **“How satisfied are you with the way democracy works in Germany?”**

The response scale is:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**

Higher values therefore mean **greater dissatisfaction**.
""")


c1, c2, c3 = st.columns(3)

c1.metric(
    "Model 1 R²",
    "8.5%"
)

c2.metric(
    "Model 2 R²",
    "9.6%"
)

c3.metric(
    "Model 3 R²",
    "22.2%"
)


st.markdown("""
Adding Subjective Social Class increases explanatory power from
**8.5% to 9.6%**.

Adding Feeling Left Behind then increases it from
**9.6% to 22.2%**.
""")


st.success("""
### Main interpretation

Feeling Left Behind adds substantial explanatory information
for differences in democratic satisfaction between respondents.
""")


st.error("""
# LBI ↑ → Democratic Dissatisfaction ↑

or, more intuitively:

# LBI ↑ → Democratic Satisfaction ↓
""")


with st.expander("Technical evidence"):

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final R²",
        "22.2%"
    )

    c2.metric(
        "Standardized β",
        "+0.395"
    )

    c3.metric(
        "p-value",
        "< .001"
    )

    st.caption("""
Method: multiple OLS regression.

The positive coefficient reflects the coding of q119:
higher values mean greater dissatisfaction.
""")


st.divider()


# ============================================================
# 7. PARTY REPRESENTATION DETAIL
# ============================================================

st.header("7. 👥 Party Representation")

st.markdown("""
### What was actually measured?

Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**

Responses:

# Yes / No
""")


st.info("""
Because the outcome is binary, Party Representation is modeled
using **binary logistic regression** rather than OLS.
""")


c1, c2, c3 = st.columns(3)

c1.metric(
    "Model 1 Pseudo R²",
    "3.37%"
)

c2.metric(
    "Model 2 Pseudo R²",
    "3.43%"
)

c3.metric(
    "Model 3 Pseudo R²",
    "4.62%"
)


st.markdown("""
Adding Subjective Social Class produces only a very small change:

**3.37% → 3.43%**

Adding Feeling Left Behind increases model fit to:

**4.62%**
""")


st.success("""
### Main interpretation

Feeling Left Behind is statistically associated with
Party Representation, but it adds much less model fit here than
for Institutional Trust or Democratic Satisfaction.
""")


st.error("""
# LBI ↑ → odds of Party Representation ↓
""")


with st.expander("Technical evidence"):

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final Pseudo R²",
        "4.62%"
    )

    c2.metric(
        "Odds Ratio",
        "0.706"
    )

    c3.metric(
        "p-value",
        "< .001"
    )

    st.markdown("""
Holding the other variables constant, each one-point increase in the
Left Behind Index is associated with approximately **29% lower odds**
of saying that a political party represents the respondent's views well.
""")

    st.caption("""
Calculation: 1 − 0.706 = 0.294, approximately 29%.

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
    "Before LBI": [
        "10.7%",
        "9.6%",
        "3.43%"
    ],
    "After LBI": [
        "27.6%",
        "22.2%",
        "4.62%"
    ],
    "Gain after LBI": [
        "+16.9 pp",
        "+12.6 pp",
        "+1.19 pp"
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
Party Representation uses McFadden Pseudo R², so its gain should
not be treated as numerically equivalent to the OLS R² gains
for the other two outcomes.
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
# 9. PLAIN LANGUAGE
# ============================================================

st.header("9. The result in plain language")

st.info("""
Imagine two respondents who are similar in income, education, age,
region, migration background, political interest and perceived
social class.

Knowing **how left behind they feel** still gives us substantial
additional information about how much they trust institutions and
how satisfied they are with democracy.

For Party Representation, Feeling Left Behind is also related to
the outcome, but it adds considerably less explanatory information.
""")


st.divider()


# ============================================================
# LIMITATION
# ============================================================

st.header("Important limitation")

st.warning("""
### Association ≠ causation

The results identify statistical relationships.

Because the GLES data used here are cross-sectional, the analysis
cannot establish that Feeling Left Behind **causes** lower
Institutional Trust, lower Democratic Satisfaction or lower
Party Representation.
""")


st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Analytical sample: 5,039 respondents.
""")