import streamlit as st
import pandas as pd


st.title("🔬 Methodology")

st.subheader(
    "How survey answers become variables, models and statistical results"
)

st.info("""
### Methodological sequence

**Respondent answers → outcomes and predictors → two regression models →
coefficients → model fit → interpretation**
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
    "Outcome-specific samples",
    "5,096–5,676"
)

st.info("""
The final regressions use **complete-case samples**.

The two models for a given outcome are estimated on exactly the
same respondents so that changes in model fit can be compared fairly.

- Institutional Trust: **N = 5,653**
- Democratic Satisfaction: **N = 5,676**
- Party Representation: **N = 5,096**
""")

st.divider()


# ============================================================
# 2. OUTCOMES
# ============================================================

st.header("2. How are the three outcomes measured?")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Respondents rate trust in **eight institutions** from
**1 to 11**.

The ratings are combined using their **mean**.

### 8 answers → mean → Trust score
""")

        st.caption(
            "Analyzed using multiple OLS regression."
        )


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
One survey response measures satisfaction with democracy.

**1 = Very satisfied**

to

**4 = Not at all satisfied**

Higher values indicate greater dissatisfaction.
""")

        st.caption(
            "Analyzed using multiple OLS regression."
        )


with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
One survey question asks whether any political party
represents the respondent's views well.

### Yes / No
""")

        st.caption(
            "Analyzed using binary logistic regression."
        )


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
        "Feeling Left Behind"
    ],
    "Role": [
        "Traditional factor",
        "Traditional factor",
        "Traditional factor",
        "Traditional factor",
        "Traditional factor",
        "Traditional factor",
        "New predictor tested in Model 2"
    ],
    "How it is represented": [
        "Reported household-income category",
        "Education level/category",
        "Respondent's age",
        "Geographical category",
        "Migration-background category",
        "Survey measure of political interest",
        "Mean of four Feeling Left Behind items"
    ]
})

st.dataframe(
    variable_table,
    width="stretch",
    hide_index=True
)


st.info("""
The traditional variables remain **separate predictors**.

They are not averaged into one socioeconomic score.
""")

st.caption("""
Subjective Social Class is explored descriptively in the Feeling Left Behind
section, but it is not included as a separate stage in the final regression design.
""")

st.divider()


# ============================================================
# 4. REGRESSION
# ============================================================

st.header("4. What does multiple regression do?")

st.markdown("""
Multiple regression examines how several predictors are associated
with an outcome **at the same time**.
""")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("### 🔢 Numerical / ordered information")

        st.markdown("""
For variables such as age, the model asks:

> **When this value changes, does the outcome also tend to change?**
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🗂️ Categories")

        st.markdown("""
For categorical variables, the model compares groups.

For example:

**East Germany versus West Germany**
""")


st.success("""
### The important idea

The relationship for each predictor is estimated while the other
variables in the model are also taken into account.
""")

st.divider()


# ============================================================
# 5. LBI
# ============================================================

st.header("5. How is the Left Behind Index calculated?")

st.markdown("""
Feeling Left Behind is a **composite index constructed in this project**.

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

### Mean of the four reversed responses

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
# 6. TWO MODELS
# ============================================================

st.header("6. How are the two models constructed?")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("## Model 1")

        st.markdown("""
### Traditional factors

Household Income

+ Education

+ Age

+ East / West Germany

+ Migration Background

+ Political Interest
""")


with c2:
    with st.container(border=True):

        st.markdown("## Model 2")

        st.markdown("""
### Everything in Model 1

# +

### 🧩 Left Behind Index
""")


st.success("""
### Why two models?

The project's central question is whether **Feeling Left Behind adds
explanatory information beyond traditional factors**.

Model 1 provides the baseline.

Model 2 adds the LBI.
""")

st.divider()


# ============================================================
# 7. SIX REGRESSIONS
# ============================================================

st.header("7. How many regressions are estimated?")

st.markdown("""
Both model specifications are applied separately to each outcome.
""")

st.markdown("""
| Outcome | Model 1 | Model 2 |
|---|---|---|
| Institutional Trust | OLS | OLS |
| Democratic Satisfaction | OLS | OLS |
| Party Representation | Logistic | Logistic |
""")

st.success("""
# 3 outcomes × 2 models = 6 regressions
""")

st.divider()


# ============================================================
# 8. SAME SAMPLE
# ============================================================

st.header("8. Why use the same sample within each comparison?")

st.markdown("""
Adding LBI means that some respondents with missing LBI information
could otherwise disappear only from Model 2.

That would make Model 1 and Model 2 use different groups of people.
""")

st.info("""
### To avoid this:

For each outcome, the data are restricted first to respondents with
valid information for **all variables needed in Model 2**.

Then both models are estimated on this same sample.
""")

st.success("""
This means that the change from Model 1 to Model 2 reflects
the change in predictors — **not a change in who is being analyzed**.
""")

st.divider()


# ============================================================
# 9. OLS
# ============================================================

st.header("9. Institutional Trust and Democratic Satisfaction")

st.markdown("""
These two outcomes are modeled using
**multiple Ordinary Least Squares (OLS) regression**.
""")

st.info("""
OLS estimates how each predictor is associated with the outcome
while accounting for the other predictors included in the model.
""")

st.divider()


# ============================================================
# 10. COEFFICIENT
# ============================================================

st.header("10. What does the coefficient tell us?")

st.markdown("""
The coefficient tells us the **direction and estimated size
of an association**, holding the other variables constant.
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
For Institutional Trust:

### LBI coefficient = −0.994

So:

# LBI ↑ → Trust ↓
""")

st.divider()


# ============================================================
# 11. R2
# ============================================================

st.header("11. What does R² mean?")

st.info("""
# R² = proportion of observed outcome variation accounted for by the model
""")

st.markdown("""
Respondents have different outcome scores.

R² asks:

> **How much of those observed differences can the variables in
> the model statistically account for?**
""")


st.markdown("""
### Institutional Trust

**Model 1**

Traditional factors

→ **R² = 8.46%**

# ↓

**Model 2**

+ Feeling Left Behind

→ **R² = 26.29%**
""")


st.success("""
### Correct interpretation

The complete Model 2 accounts for **26.29% of the observed
variation in Institutional Trust**.

The increase after LBI is added is:

### 26.29% − 8.46% = +17.83 percentage points
""")


st.warning("""
### Do not say:

“Feeling Left Behind alone explains 26.29%.”

That percentage belongs to the **complete Model 2**.
""")

st.divider()


# ============================================================
# 12. R2 CAUTION
# ============================================================

st.header("12. Why must R² be used carefully?")

st.markdown("""
Ordinary R² will not decrease when an additional predictor is added.

Therefore, simply observing that Model 2 has a higher R² than Model 1
is **not enough by itself** to establish that LBI is important.
""")

st.info("""
### We therefore look at several pieces of evidence together:

**R² change**

+

**Adjusted R²**

+

**LBI coefficient**

+

**p-value**
""")


c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
R²:

**8.46% → 26.29%**

Adjusted R²:

**8.37% → 26.20%**
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
R²:

**7.97% → 21.20%**

Adjusted R²:

**7.87% → 21.10%**
""")


st.success("""
Because Adjusted R² penalizes unnecessary predictors, the fact that
the improvement remains almost unchanged provides additional evidence
that the gain is not merely a mechanical consequence of adding
one variable.
""")

st.divider()


# ============================================================
# 13. COEFFICIENT VS R2
# ============================================================

st.header("13. Coefficient and R² answer different questions")


comparison_table = pd.DataFrame({
    "Statistic": [
        "Coefficient",
        "R²",
        "Adjusted R²"
    ],
    "Question": [
        "How is a predictor associated with the outcome?",
        "How much observed variation does the complete model account for?",
        "How much variation does the model account for after penalizing added predictors?"
    ],
    "Trust example": [
        "LBI coefficient = −0.994",
        "Model 2 R² = 26.29%",
        "Model 2 Adjusted R² = 26.20%"
    ]
})

st.dataframe(
    comparison_table,
    width="stretch",
    hide_index=True
)

st.divider()


# ============================================================
# 14. P-VALUE
# ============================================================

st.header("14. What does the p-value tell us?")

st.markdown("""
The p-value helps evaluate the statistical evidence for an
estimated association.

In this project:

### p < .05

is used as the threshold for statistical significance.
""")

st.warning("""
Statistical significance does not tell us that an effect is
causal, large or important.

It answers a different question from model fit and effect size.
""")

st.divider()


# ============================================================
# 15. LOGISTIC REGRESSION
# ============================================================

st.header("15. Why is Party Representation different?")

st.markdown("""
Party Representation has only two possible outcomes:

# Yes / No

Therefore OLS is not used.

Instead, the analysis uses **binary logistic regression**.
""")

st.markdown("""
The logistic regression estimates how predictors are associated
with the **odds of answering Yes**.
""")

st.divider()


# ============================================================
# 16. ODDS RATIO
# ============================================================

st.header("16. How do we interpret Party Representation?")

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

**Odds Ratio = 0.705**

Holding the other variables constant, a one-point increase
in the Left Behind Index is associated with approximately
**29.5% lower odds** of saying that a political party
represents the respondent's views well.
""")

st.caption(
    "Calculation: 1 − 0.7052 = 0.2948, approximately 29.5%."
)

st.divider()


# ============================================================
# 17. PSEUDO R2
# ============================================================

st.header("17. Why does Party Representation use Pseudo R²?")

st.markdown("""
Standard OLS R² is not used for logistic regression.

For Party Representation, the analysis reports
**McFadden's Pseudo R²**.
""")

st.warning("""
Pseudo R² is **not the same statistic** as OLS R².

Therefore, the Party Representation values should not be directly
compared numerically with Trust or Satisfaction.
""")

st.divider()


# ============================================================
# 18. COMPLETE METHOD
# ============================================================

st.header("18. The complete method")

st.markdown("""
### Survey respondents

# ↓

### Measure three outcomes

🏛️ Institutional Trust

🗳️ Democratic Satisfaction

👥 Party Representation

# ↓

### Model 1

Income · Education · Age · Region · Migration · Political Interest

# ↓

### Construct Left Behind Index

4 questions → reversed scale → mean → 1–5 score

# ↓

### Model 2

Model 1 + Feeling Left Behind

# ↓

### Estimate both models for each outcome

# ↓

### 6 regressions

# ↓

### Read the evidence together

**Coefficient → direction / estimated association**

**p-value → statistical evidence**

**R² → OLS model fit**

**Adjusted R² → penalized OLS model fit**

**Odds Ratio → logistic association**

**Pseudo R² → logistic model fit**
""")

st.divider()


# ============================================================
# 19. 30 SECOND ANSWER
# ============================================================

st.header("19. How to explain the methodology in 30 seconds")

st.info("""
“I study three democratic outcomes: Institutional Trust,
Democratic Satisfaction and Party Representation.

For each outcome, I compare two models.

Model 1 contains traditional socioeconomic, demographic and
political factors.

Model 2 adds the Feeling Left Behind Index, constructed as the
mean of four survey items.

Trust and Satisfaction use multiple OLS regression.
Party Representation is Yes/No, so it uses logistic regression.

I compare model fit, but I do not rely on R² alone. For the OLS
models I also look at Adjusted R², and for all outcomes I examine
the LBI association and its statistical significance.”
""")

st.divider()


# ============================================================
# 20. ADDITIONAL METHODOLOGICAL LIMITATIONS
# ============================================================

st.header("20. Additional methodological limitations")


with st.container(border=True):

    st.markdown("### ⚖️ Survey weights")

    st.markdown("""
The GLES dataset provides survey weights, including `w_ipfges`.

These weights were **not applied to the regression models used
in this project**.

The results should therefore be interpreted as statistical
associations within the analytical sample rather than as
weighted population estimates for the German electorate.
""")


with st.container(border=True):

    st.markdown("### 🔄 Reverse causality")

    st.markdown("""
Because the data are cross-sectional, the causal direction
of the relationships cannot be established.

The results are consistent with:

**Feeling Left Behind → lower trust / lower democratic satisfaction**

but the reverse process is also possible:

**existing distrust or dissatisfaction → stronger perceptions
of Feeling Left Behind**

Both may also be influenced by other factors that are not
included in the models.
""")


st.divider()


# ============================================================
# 21. IMPORTANT LIMITATION
# ============================================================

st.header("21. What can — and cannot — be concluded?")


c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("### ✅ What the analysis shows")

        st.markdown("""
The analysis identifies **statistical associations** between
Feeling Left Behind and the three democratic outcomes.

It also shows how model fit changes when LBI is added to the
traditional predictors.
""")


with c2:
    with st.container(border=True):

        st.markdown("### ❌ What the analysis does not show")

        st.markdown("""
The analysis does not establish that Feeling Left Behind
**causes** lower trust, greater democratic dissatisfaction
or lower Party Representation.

It also does not establish the direction of causality.
""")


st.warning("""
### Association ≠ causation

Because the data are cross-sectional, we cannot determine whether
Feeling Left Behind contributes to democratic disconnection,
whether existing democratic disconnection contributes to stronger
perceptions of being left behind, or whether both are influenced
by other factors.
""")


st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Regression models are unweighted (`w_ipfges` was not applied).
""")