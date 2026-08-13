import streamlit as st
import pandas as pd


st.title("🔬 Methodology")

st.subheader(
    "How survey answers become variables, models and statistical results"
)

st.info("""
### Methodological sequence

**Respondent answers → outcomes and predictors → regression →
coefficients → R² / Pseudo R² → interpretation**
""")

st.divider()


# ============================================================
# 1. DATA
# ============================================================

st.header("1. Data")

st.markdown("""
The analysis uses the **German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section**.
""")

c1, c2 = st.columns(2)

c1.metric(
    "Original respondents",
    "7,336"
)

c2.metric(
    "Analytical sample",
    "5,039"
)

st.divider()


# ============================================================
# 2. OUTCOMES
# ============================================================

st.header("2. First: how are the three outcomes measured?")

st.markdown("""
These are the variables that the regression tries to explain.
""")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Respondents rate trust in **eight institutions** on a
**1–11 scale**.

The ratings are combined using their **mean**.

### 8 answers → mean → Trust score
""")

        st.caption("Analyzed using multiple OLS regression.")


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
One survey response measures satisfaction with democracy.

**1 = Very satisfied**

to

**4 = Not at all satisfied**

### 1 answer → Satisfaction measure

Higher values therefore indicate greater dissatisfaction.
""")

        st.caption("Analyzed using multiple OLS regression.")


with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
One survey question asks whether any political party
represents the respondent's views well.

### 1 answer → Yes / No

There is no average or continuous representation score.
""")

        st.caption("Analyzed using binary logistic regression.")


st.divider()


# ============================================================
# 3. PREDICTORS
# ============================================================

st.header("3. What information is used to explain the outcomes?")

variable_table = pd.DataFrame({
    "Variable": [
        "Household Income",
        "Education",
        "Age",
        "East / West Germany",
        "Migration Background",
        "Political Interest",
        "Subjective Social Class",
        "Feeling Left Behind"
    ],
    "How it is represented": [
        "Respondent's reported household-income information",
        "Education level/category",
        "Respondent's age",
        "Geographical category",
        "Migration-background category",
        "Survey measure of political interest",
        "Respondent's perceived social position",
        "Mean of four Feeling Left Behind questions"
    ]
})

st.dataframe(
    variable_table,
    width="stretch",
    hide_index=True
)

st.info("""
The regression does **not** average income, education, age and the
other traditional variables into one socioeconomic index.

They remain **separate variables**.
""")

st.divider()


# ============================================================
# 4. HOW REGRESSION USES DIFFERENT VARIABLES
# ============================================================

st.header("4. How does the regression use these values?")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("### 🔢 Numerical / ordered information")

        st.markdown("""
For variables such as age or ordered measures, the model asks:

> **When this value changes, does the outcome also tend to change?**

Example:

Different ages

# ↓

Different patterns of Institutional Trust?
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🗂️ Categories")

        st.markdown("""
For categorical variables, the model compares groups.

Example:

East Germany

**versus**

West Germany

# ↓

Is there a systematic difference in Institutional Trust?
""")


st.markdown("""
The regression evaluates these relationships **simultaneously**.

This means that the estimated relationship for one variable is
calculated while the other variables in the model are also taken
into account.
""")

st.divider()


# ============================================================
# 5. LEFT BEHIND INDEX
# ============================================================

st.header("5. How is the Left Behind Index calculated?")

st.markdown("""
Unlike the traditional variables, Feeling Left Behind is a
**composite index constructed in this project**.

It combines four GLES survey items.
""")

c1, c2, c3, c4 = st.columns(4)

c1.markdown("### 💶 Economic attention")
c2.markdown("### 👏 Recognition")
c3.markdown("### 🏥 Services")
c4.markdown("### 🗣️ Voice")

st.markdown("""
### For each respondent:

**Question 1 + Question 2 + Question 3 + Question 4**

# ↓

### Mean of the four responses

# ↓

# Left Behind Index: 1–5
""")

c1, c2 = st.columns(2)

c1.metric(
    "1",
    "Lower Feeling Left Behind"
)

c2.metric(
    "5",
    "Higher Feeling Left Behind"
)

st.info("""
There is **no threshold** separating “left behind” and
“not left behind”.

The index represents degrees of Feeling Left Behind.
""")

st.divider()


# ============================================================
# 6. THREE MODELS
# ============================================================

st.header("6. How are the three models constructed?")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("## Model 1")

        st.markdown("""
### Traditional factors

Household Income

+ Education

+ Age

+ East / West

+ Migration Background

+ Political Interest
""")


with c2:
    with st.container(border=True):

        st.markdown("## Model 2")

        st.markdown("""
### Model 1

# +

### Subjective Social Class
""")


with c3:
    with st.container(border=True):

        st.markdown("## Model 3")

        st.markdown("""
### Model 2

# +

### Left Behind Index
""")


st.success("""
### Why build the models this way?

Because each model contains everything from the previous model.

We can therefore observe how much **additional information**
is gained when a new variable is added.
""")

st.divider()


# ============================================================
# 7. NINE REGRESSIONS
# ============================================================

st.header("7. How many regressions are estimated?")

st.markdown("""
The three model specifications are applied separately to
each outcome.
""")

st.markdown("""
| Outcome | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| Institutional Trust | OLS | OLS | OLS |
| Democratic Satisfaction | OLS | OLS | OLS |
| Party Representation | Logistic | Logistic | Logistic |
""")

st.success("""
# 3 outcomes × 3 models = 9 regressions
""")

st.divider()


# ============================================================
# 8. OLS
# ============================================================

st.header("8. Institutional Trust and Democratic Satisfaction")

st.markdown("""
Because these outcomes are modeled as numerical measures,
the analysis uses **multiple Ordinary Least Squares (OLS) regression**.
""")

st.info("""
### What does multiple regression do?

It estimates how each predictor is statistically associated with
the outcome while accounting for the other predictors in the model.
""")

st.divider()


# ============================================================
# 9. COEFFICIENT
# ============================================================

st.header("9. What does the coefficient tell us?")

st.markdown("""
The coefficient tells us the **direction and estimated size of the
relationship** between a predictor and the outcome, holding the
other included variables constant.
""")

c1, c2 = st.columns(2)

with c1:
    st.success("""
### Positive coefficient

Predictor ↑

↓

Outcome ↑
""")

with c2:
    st.error("""
### Negative coefficient

Predictor ↑

↓

Outcome ↓
""")

st.markdown("""
For example, in the Institutional Trust model:

# LBI ↑ → Trust ↓

because the estimated LBI coefficient is negative.
""")

st.divider()


# ============================================================
# 10. R-SQUARED
# ============================================================

st.header("10. What does R² mean?")

st.info("""
# R² = explanatory power of the complete OLS model
""")

st.markdown("""
Respondents have different outcome scores.

For example, some respondents have high Institutional Trust
and others have low Institutional Trust.

R² asks:

> **How much of these observed differences between respondents
> can the variables in the complete model account for?**
""")

st.markdown("""
### Institutional Trust

**Model 1**

Traditional factors

→ **R² = 8.8%**

↓

**Model 2**

+ Subjective Social Class

→ **R² = 10.7%**

↓

**Model 3**

+ Feeling Left Behind

→ **R² = 27.6%**
""")

st.success("""
### Correct interpretation

After Feeling Left Behind is added, the **complete Model 3**
accounts for **27.6% of the observed variation in Institutional Trust**.
""")

st.warning("""
### Do not say:

“Feeling Left Behind explains 27.6%.”

The 27.6% belongs to the **entire Model 3**.

What we can attribute to adding Feeling Left Behind is the increase:

### 27.6% − 10.7% = +16.9 percentage points
""")

st.divider()


# ============================================================
# 11. COEFFICIENT VS R2
# ============================================================

st.header("11. Coefficient and R² answer different questions")

comparison = pd.DataFrame({
    "Statistic": [
        "Coefficient",
        "R²"
    ],
    "Question": [
        "How is this predictor associated with the outcome?",
        "How much variation does the complete model account for?"
    ],
    "Institutional Trust example": [
        "Higher LBI → lower trust",
        "Model 3 explanatory power = 27.6%"
    ]
})

st.dataframe(
    comparison,
    width="stretch",
    hide_index=True
)

st.success("""
### Easy rule

**Coefficient = direction and strength of an association**

**R² = explanatory power of the complete model**
""")

st.divider()


# ============================================================
# 12. P-VALUE
# ============================================================

st.header("12. What does the p-value tell us?")

st.markdown("""
The p-value helps evaluate the statistical evidence for an
estimated relationship.

In this project:

### p < .05

is used as the threshold for statistical significance.
""")

st.warning("""
Statistical significance does not tell us that an effect is large,
important or causal.

It addresses a different question from effect size and R².
""")

st.divider()


# ============================================================
# 13. LOGISTIC REGRESSION
# ============================================================

st.header("13. Why is Party Representation different?")

st.markdown("""
Party Representation has only two possible outcomes:

# Yes / No

Therefore OLS is not used.

Instead, the analysis uses **binary logistic regression**.
""")

st.markdown("""
The logistic regression estimates how the predictors are associated
with the **odds of answering Yes** to Party Representation.
""")

st.divider()


# ============================================================
# 14. ODDS RATIO
# ============================================================

st.header("14. How do we interpret Party Representation?")

st.markdown("""
An intuitive statistic from logistic regression is the
**Odds Ratio (OR)**.
""")

c1, c2, c3 = st.columns(3)

c1.metric(
    "OR = 1",
    "No change in odds"
)

c2.metric(
    "OR > 1",
    "Higher odds"
)

c3.metric(
    "OR < 1",
    "Lower odds"
)

st.success("""
### Feeling Left Behind result

**Odds Ratio = 0.706**

Holding the other included variables constant, a one-point increase
in the Left Behind Index is associated with approximately
**29% lower odds** of saying that a political party represents
the respondent's views well.
""")

st.caption(
    "Calculation: 1 − 0.706 = 0.294, approximately 29%."
)

st.divider()


# ============================================================
# 15. PSEUDO R2
# ============================================================

st.header("15. Why does Party Representation use Pseudo R²?")

st.markdown("""
Standard OLS R² is not used for logistic regression.

For Party Representation, the analysis reports
**McFadden's Pseudo R²**.
""")

st.warning("""
Pseudo R² is **not the same statistic** as OLS R².

Therefore, the Party Representation value should not be directly
compared numerically with the R² values for Institutional Trust
and Democratic Satisfaction.
""")

st.divider()


# ============================================================
# 16. COMPLETE METHOD
# ============================================================

st.header("16. The complete method")

st.markdown("""
### Survey respondents

# ↓

### Measure three outcomes

🏛️ Institutional Trust

🗳️ Democratic Satisfaction

👥 Party Representation

# ↓

### Measure traditional characteristics

Income · Education · Age · Region · Migration · Political Interest

# ↓

### Add Subjective Social Class

🪜

# ↓

### Construct Left Behind Index

4 questions → mean → 1–5 score

# ↓

### Estimate Model 1, Model 2 and Model 3

for each of the three outcomes

# ↓

### 9 regressions

# ↓

### Read the results

**Coefficient → direction / strength**

**p-value → statistical evidence**

**R² → explanatory power of OLS model**

**Odds Ratio → logistic association**

**Pseudo R² → logistic model fit**
""")

st.divider()


# ============================================================
# 17. 30 SECOND ANSWER
# ============================================================

st.header("17. How to explain the methodology in 30 seconds")

st.info("""
“I study three democratic outcomes: Institutional Trust,
Democratic Satisfaction and Party Representation.

I then estimate three nested models for each outcome.
Model 1 contains traditional socioeconomic, demographic and
political factors. Model 2 adds Subjective Social Class.
Model 3 adds the Left Behind Index, which is the mean of four
survey items.

Trust and Satisfaction are analyzed with multiple OLS regression,
while Party Representation is Yes/No and therefore uses logistic
regression.

I compare the models to see how much additional explanatory
information Feeling Left Behind provides.”
""")

st.divider()


# ============================================================
# LIMITATION
# ============================================================

st.header("18. Important limitation")

st.warning("""
### Association ≠ causation

The GLES data used here are cross-sectional.

The regression can identify statistical associations, but it
cannot demonstrate that Feeling Left Behind causes lower trust,
greater dissatisfaction or lower political representation.
""")

st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")