import streamlit as st
import pandas as pd


st.title("📊 Results")

st.subheader(
    "Does Feeling Left Behind add explanatory information?"
)

st.markdown("""
The results are presented separately for the three democratic outcomes.

For each outcome, we first remind the reader **what was measured**,
then compare Model 1, Model 2 and Model 3.
""")

st.divider()


# ============================================================
# QUICK GUIDE
# ============================================================

st.header("Before reading the results")

st.markdown("""
### What do Model 1, Model 2 and Model 3 contain?
""")

model_table = pd.DataFrame({
    "Model": [
        "Model 1",
        "Model 2",
        "Model 3"
    ],
    "Variables": [
        "Income + Education + Age + Region + Migration Background + Political Interest",
        "Everything in Model 1 + Subjective Social Class",
        "Everything in Model 2 + Feeling Left Behind Index"
    ]
})

st.dataframe(
    model_table,
    width="stretch",
    hide_index=True
)

st.info("""
### What are we looking for?

If model fit increases substantially after LBI is added,
Feeling Left Behind is providing explanatory information that
the previous variables did not capture.
""")

st.divider()


# ============================================================
# 1. INSTITUTIONAL TRUST
# ============================================================

st.header("1. 🏛️ Institutional Trust")

with st.container(border=True):

    st.markdown("### What exactly are we explaining?")

    st.markdown("""
Institutional Trust is the respondent's **average trust across
eight institutions**.

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
### For each respondent:

8 trust ratings

# ↓

Mean

# ↓

### Institutional Trust score: 1–11

**Higher score = higher overall institutional trust**
""")

st.markdown("## What happens across the models?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### Model 1")

        st.metric(
            "Explanatory Power (R²)",
            "8.8%"
        )

        st.caption(
            "Traditional socioeconomic, demographic and political factors."
        )

with c2:
    with st.container(border=True):

        st.markdown("### Model 2")

        st.metric(
            "Explanatory Power (R²)",
            "10.7%",
            "+1.9 pp"
        )

        st.caption(
            "Model 1 + Subjective Social Class."
        )

with c3:
    with st.container(border=True):

        st.markdown("### Model 3")

        st.metric(
            "Explanatory Power (R²)",
            "27.6%",
            "+16.9 pp"
        )

        st.caption(
            "Model 2 + Feeling Left Behind."
        )

st.success("""
### What does 27.6% mean?

The **complete Model 3** accounts for **27.6% of the observed
differences in Institutional Trust scores between respondents**.

It does **not** mean that LBI alone explains 27.6%.
""")

st.markdown("### What did adding LBI change?")

st.markdown("""
Before LBI:

# 10.7%

After LBI:

# 27.6%

### Increase = +16.9 percentage points
""")

st.info("""
This means that adding Feeling Left Behind substantially increases
the model's explanatory power for Institutional Trust.
""")

st.markdown("### In which direction is LBI associated with trust?")

st.error("""
# Feeling Left Behind ↑ → Institutional Trust ↓

Respondents with higher Feeling Left Behind scores tend to report
lower Institutional Trust, holding the other variables in the model
constant.
""")

st.caption(
    "The LBI association is statistically significant (p < .001)."
)

st.divider()


# ============================================================
# 2. DEMOCRATIC SATISFACTION
# ============================================================

st.header("2. 🗳️ Democratic Satisfaction")

with st.container(border=True):

    st.markdown("### What exactly are we explaining?")

    st.markdown("""
This outcome measures how satisfied respondents are with
**how democracy works in Germany**.

It comes from **one survey response**:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.warning("""
### Important direction

Higher scores mean **greater dissatisfaction**.

Therefore:

**Outcome score ↑ = Democratic Satisfaction ↓**
""")

st.markdown("## What happens across the models?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### Model 1")

        st.metric(
            "Explanatory Power (R²)",
            "8.2%"
        )

        st.caption(
            "Traditional socioeconomic, demographic and political factors."
        )

with c2:
    with st.container(border=True):

        st.markdown("### Model 2")

        st.metric(
            "Explanatory Power (R²)",
            "9.6%",
            "+1.4 pp"
        )

        st.caption(
            "Model 1 + Subjective Social Class."
        )

with c3:
    with st.container(border=True):

        st.markdown("### Model 3")

        st.metric(
            "Explanatory Power (R²)",
            "22.2%",
            "+12.6 pp"
        )

        st.caption(
            "Model 2 + Feeling Left Behind."
        )

st.success("""
### What does 22.2% mean?

The **complete Model 3** accounts for **22.2% of the observed
variation in Democratic Satisfaction responses**.
""")

st.markdown("""
Before LBI:

# 9.6%

After LBI:

# 22.2%

### Increase = +12.6 percentage points
""")

st.info("""
Again, Feeling Left Behind adds substantial explanatory information
beyond the variables already included in Model 2.
""")

st.markdown("### In which direction is the relationship?")

st.error("""
# Feeling Left Behind ↑ → Democratic Dissatisfaction ↑

Because higher outcome values mean greater dissatisfaction,
respondents with higher LBI scores tend to be **less satisfied
with how democracy works**.
""")

st.caption(
    "The LBI association is statistically significant (p < .001)."
)

st.divider()


# ============================================================
# 3. PARTY REPRESENTATION
# ============================================================

st.header("3. 👥 Party Representation")

with st.container(border=True):

    st.markdown("### What exactly are we explaining?")

    st.markdown("""
Respondents are asked whether **any political party in Germany
represents their personal political views well**.

The outcome has only two possible responses:

# YES / NO
""")

    st.info("""
There is no continuous Party Representation score.

Because the outcome is binary, this analysis uses
**logistic regression** rather than OLS.
""")

st.markdown("## What happens across the models?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### Model 1")

        st.metric(
            "McFadden Pseudo R²",
            "2.9%"
        )

        st.caption(
            "Traditional socioeconomic, demographic and political factors."
        )

with c2:
    with st.container(border=True):

        st.markdown("### Model 2")

        st.metric(
            "McFadden Pseudo R²",
            "3.4%",
            "+0.5 pp"
        )

        st.caption(
            "Model 1 + Subjective Social Class."
        )

with c3:
    with st.container(border=True):

        st.markdown("### Model 3")

        st.metric(
            "McFadden Pseudo R²",
            "4.6%",
            "+1.2 pp"
        )

        st.caption(
            "Model 2 + Feeling Left Behind."
        )

st.warning("""
### Do not compare 4.6% directly with 27.6% or 22.2%

Party Representation uses **McFadden's Pseudo R²** from logistic
regression.

Institutional Trust and Democratic Satisfaction use ordinary
OLS R².

They are different statistics.
""")

st.markdown("### What does the LBI result mean?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.metric(
            "LBI Odds Ratio",
            "0.706"
        )

with c2:
    with st.container(border=True):

        st.metric(
            "Approximate change in odds",
            "−29%"
        )

st.error("""
# Feeling Left Behind ↑ → odds of Party Representation ↓

Holding the other variables constant, each one-point increase
in the Left Behind Index is associated with approximately
**29% lower odds** of saying that a political party represents
the respondent's views well.
""")

st.caption(
    "Calculation: 1 − 0.706 = 0.294, approximately 29%."
)

st.divider()


# ============================================================
# 4. SIDE-BY-SIDE
# ============================================================

st.header("4. What is the overall pattern?")

summary_table = pd.DataFrame({
    "Outcome": [
        "🏛️ Institutional Trust",
        "🗳️ Democratic Satisfaction",
        "👥 Party Representation"
    ],
    "What it measures": [
        "Average trust in 8 institutions",
        "Satisfaction with how democracy works",
        "Whether a party represents the respondent's views"
    ],
    "Before LBI": [
        "10.7% R²",
        "9.6% R²",
        "3.4% Pseudo R²"
    ],
    "After LBI": [
        "27.6% R²",
        "22.2% R²",
        "4.6% Pseudo R²"
    ],
    "Change": [
        "+16.9 pp",
        "+12.6 pp",
        "+1.2 pp"
    ]
})

st.dataframe(
    summary_table,
    width="stretch",
    hide_index=True
)

st.warning("""
The Party Representation change uses McFadden Pseudo R² and
should not be compared numerically as if it were the same
statistic as OLS R².
""")

st.divider()


# ============================================================
# 5. MAIN FINDING
# ============================================================

st.header("5. Main finding")

st.success("""
### Feeling Left Behind adds substantial explanatory information
### for Institutional Trust and Democratic Satisfaction.

For Institutional Trust:

**10.7% → 27.6%**

For Democratic Satisfaction:

**9.6% → 22.2%**

For Party Representation, LBI is also associated with lower
representation, but the improvement in model fit is considerably
smaller.
""")

st.divider()


# ============================================================
# 6. HOW TO SAY IT
# ============================================================

st.header("6. How to explain the result in plain language")

st.info("""
**“People who feel more left behind tend to trust institutions less,
be less satisfied with how democracy works, and have lower odds of
feeling represented by a political party.

The strongest improvement in explanatory power appears for
Institutional Trust and Democratic Satisfaction.

This does not mean that Feeling Left Behind causes these attitudes,
but it provides substantial additional information beyond the
socioeconomic and demographic variables already included.”**
""")

st.divider()


# ============================================================
# LIMITATION
# ============================================================

st.header("Important limitation")

st.warning("""
### Association ≠ causation

These regressions identify statistical relationships.

Because the analysis uses cross-sectional survey data, the results
cannot establish that Feeling Left Behind **causes** lower trust,
greater democratic dissatisfaction or lower Party Representation.
""")

st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Analytical sample: 5,039 respondents.
""")