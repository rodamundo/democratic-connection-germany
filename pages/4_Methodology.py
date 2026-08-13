import streamlit as st
import pandas as pd


# ============================================================
# PAGE
# ============================================================

st.title("🔬 Methodology")

st.subheader(
    "From survey answers to statistical models"
)

st.markdown("""
This page explains exactly how the survey responses were transformed
into variables and how those variables were used to test the relationship
between **Feeling Left Behind** and democratic attitudes.
""")

st.info("""
### The analysis in one line

**Survey answers → variables → three regression models → coefficients
and model fit → interpretation**
""")

st.divider()


# ============================================================
# 1. DATA
# ============================================================

st.header("1. Data")

st.markdown("""
The analysis uses the **German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section**.

The original dataset contains **7,336 respondents**.

After applying the cleaning and complete-case requirements used for
the regression analysis, the final analytical sample contains
**5,039 respondents**.
""")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Initial respondents",
    "7,336"
)

c2.metric(
    "Analytical sample",
    "5,039"
)

c3.metric(
    "Democratic outcomes",
    "3"
)

st.divider()


# ============================================================
# 2. WHAT EXISTS FOR EACH PERSON?
# ============================================================

st.header("2. What information do we have for each respondent?")

st.markdown("""
The regression does not give every respondent one general
“socioeconomic score”.

Instead, each characteristic remains a **separate variable**.

For example, one respondent has their own income, age, education,
region, political interest and other characteristics.
""")

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
    "How it enters the analysis": [
        "Respondent's reported household-income information",
        "Respondent's education level/category",
        "Respondent's age",
        "Geographical category",
        "Migration-background category",
        "Respondent's level of political interest",
        "Respondent's perceived social position",
        "Index calculated from four survey questions"
    ],
    "Type of information": [
        "Ordered / numerical information",
        "Categorical / ordered information",
        "Numerical",
        "Categorical",
        "Categorical",
        "Survey scale",
        "Survey scale / category",
        "Composite score"
    ]
})

st.dataframe(
    variable_table,
    width="stretch",
    hide_index=True
)

st.success("""
### Important

Model 1 and Model 2 are **not indices**.

Income, education, age, region and the other characteristics are
not averaged together.

They remain separate variables and are entered together into
the regression.
""")

st.divider()


# ============================================================
# 3. INTUITIVE EXPLANATION
# ============================================================

st.header("3. What does the regression actually compare?")

st.markdown("""
The basic idea is simple:

> **Do people with different values or categories on these variables
> also tend to have different democratic attitudes?**

The exact comparison depends on the type of variable.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("""
### 🔢 Numerical or ordered variables

For variables such as **age** or ordered measures, the model asks:

> As this value changes, does the democratic outcome also tend
> to change?

For example:

**Different ages → systematically different trust scores?**

The regression estimates the direction and size of that relationship.
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### 🗂️ Categorical variables

For variables such as **East / West Germany**, the model compares
categories.

Conceptually:

**East → pattern of trust**

versus

**West → pattern of trust**

The regression estimates whether there is a systematic difference
between the categories.
""")


st.warning("""
The examples above explain **how the statistical comparison works**.

They do not imply that one particular group necessarily has higher
or lower trust. The actual direction must be read from the estimated
coefficient.
""")

st.divider()


# ============================================================
# 4. LEFT BEHIND INDEX
# ============================================================

st.header("4. How is the Feeling Left Behind Index created?")

st.markdown("""
Feeling Left Behind is different from the variables above because
it is a **composite index created from four survey questions**.

The questions capture four dimensions of how respondents perceive
the position of **people like them** in society.
""")

c1, c2, c3, c4 = st.columns(4)

with c1:

    with st.container(border=True):

        st.markdown("""
### 💶 Economic attention

Whether society pays sufficient attention to the economic
situation of people like the respondent.
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### 👏 Recognition

Whether people like the respondent receive sufficient
recognition for what they contribute.
""")


with c3:

    with st.container(border=True):

        st.markdown("""
### 🏥 Services

Whether people like the respondent have adequate access
to basic services.
""")


with c4:

    with st.container(border=True):

        st.markdown("""
### 🗣️ Voice

Whether people like the respondent feel able to express
their opinions.
""")


st.markdown("### From four answers to one score")

st.markdown("""
For each respondent, the four items are oriented in the same
direction and then combined using their **mean**.
""")

with st.container(border=True):

    st.markdown("""
<div style="text-align:center;">

<h3>Question 1 &nbsp;&nbsp; + &nbsp;&nbsp;
Question 2 &nbsp;&nbsp; + &nbsp;&nbsp;
Question 3 &nbsp;&nbsp; + &nbsp;&nbsp;
Question 4</h3>

<h2>↓</h2>

<h3>Mean of the four responses</h3>

<h2>↓</h2>

<h2>Feeling Left Behind Index</h2>

<br>

<h3>1 ───────── 2 ───────── 3 ───────── 4 ───────── 5</h3>

<p>
Lower Feeling Left Behind
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Higher Feeling Left Behind
</p>

</div>
""", unsafe_allow_html=True)


st.info("""
### There is no cut-off

Respondents are **not** divided into:

❌ “Left Behind”

and

❌ “Not Left Behind”

Instead, every respondent receives a position on a **continuous
1–5 scale**.

A higher score represents a higher level of Feeling Left Behind.
""")

st.divider()


# ============================================================
# 5. OUTCOMES
# ============================================================

st.header("5. What are we trying to explain?")

st.markdown("""
The Feeling Left Behind Index and the other variables are used to
study **three democratic outcomes**.
""")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("""
### 🏛️ Institutional Trust

Trust ratings for **eight institutions** are combined into an
Institutional Trust measure.

The analysis asks:

> Why do Institutional Trust scores differ between respondents?
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### 🗳️ Democratic Satisfaction

Respondents report their level of satisfaction with democracy.

The analysis asks:

> Why do Democratic Satisfaction responses differ between respondents?
""")


with c3:

    with st.container(border=True):

        st.markdown("""
### 👥 Party Representation

Respondents indicate whether a political party represents
their views well.

This outcome is:

# Yes / No

Therefore it requires a different type of regression.
""")

st.divider()


# ============================================================
# 6. THREE MODELS
# ============================================================

st.header("6. Why are there three models?")

st.markdown("""
The models are **nested**.

This means that we start with a basic set of variables and then
add new information step by step.

This allows us to ask whether each new piece of information helps
us understand democratic attitudes better.
""")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("""
### MODEL 1

## Traditional factors

💰 Household Income

🎓 Education

🎂 Age

📍 East / West Germany

🌍 Migration Background

🗳️ Political Interest

---

**Question:**

How much can these characteristics help us understand
differences in democratic attitudes?
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### MODEL 2

## Model 1 +

🪜 **Subjective Social Class**

Everything from Model 1 remains in the regression.

We then add how respondents perceive their own social position.

---

**Question:**

Does perceived social position add information beyond the
traditional variables?
""")


with c3:

    with st.container(border=True):

        st.markdown("""
### MODEL 3

## Model 2 +

🧩 **Feeling Left Behind Index**

Everything from Models 1 and 2 remains in the regression.

We then add the Feeling Left Behind score.

---

**Question:**

Does Feeling Left Behind add information that socioeconomic
characteristics and subjective class did not already capture?
""")


st.success("""
### This is the central comparison of the project

**Model 1**

Traditional characteristics

↓

**Model 2**

+ Subjective Social Class

↓

**Model 3**

+ Feeling Left Behind

The question is whether the model becomes substantially more
informative when Feeling Left Behind is added.
""")

st.divider()


# ============================================================
# 7. STATISTICAL METHOD
# ============================================================

st.header("7. How are these relationships estimated statistically?")

st.markdown("""
The analysis uses **multiple regression**.

“Multiple” means that several variables are included in the model
at the same time.

This is important because it allows us to estimate the relationship
between one variable and the outcome **while holding the other
variables in the model constant**.
""")

st.markdown("### Example")

with st.container(border=True):

    st.markdown("""
Suppose the model contains:

**Income + Education + Age + Region + Migration Background +
Political Interest + Social Class + Feeling Left Behind**

When estimating the relationship between **Feeling Left Behind**
and **Institutional Trust**, the model also takes the other
variables into account.

So the question becomes:

> **Among respondents who are otherwise comparable on the variables
> included in the model, is a higher Feeling Left Behind score
> associated with a different level of Institutional Trust?**
""")

st.warning("""
This is statistical adjustment, not an experiment.

It helps separate associations between variables, but it does
**not establish causality**.
""")

st.divider()


# ============================================================
# 8. OLS
# ============================================================

st.header("8. Institutional Trust and Democratic Satisfaction: OLS")

st.markdown("""
For **Institutional Trust** and **Democratic Satisfaction**, the
analysis uses **multiple Ordinary Least Squares (OLS) regression**.

OLS estimates how changes or differences in the predictor variables
are associated with differences in the outcome.
""")

with st.container(border=True):

    st.markdown("""
### Conceptually

**Income**

**+ Education**

**+ Age**

**+ Region**

**+ Migration Background**

**+ Political Interest**

**+ Subjective Social Class**

**+ Feeling Left Behind**

# ↓

### OLS regression

# ↓

**Institutional Trust**

or

**Democratic Satisfaction**
""")

st.divider()


# ============================================================
# 9. COEFFICIENT
# ============================================================

st.header("9. What does the coefficient tell us?")

st.markdown("""
The **coefficient** tells us the **direction** of the statistical
relationship, holding the other variables in the model constant.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("""
### Positive coefficient

Predictor ↑

# ↓

Outcome ↑

A higher value of the predictor is associated with a
**higher value of the outcome**.
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### Negative coefficient

Predictor ↑

# ↓

Outcome ↓

A higher value of the predictor is associated with a
**lower value of the outcome**.
""")


st.success("""
### Example from this project

For **Institutional Trust**, the Feeling Left Behind coefficient
is negative.

Therefore:

# Feeling Left Behind ↑ → Institutional Trust ↓
""")

st.info("""
The coefficient answers:

### “Which direction does the relationship go?”

It does **not** tell us how much of all differences between
respondents the complete model explains.

For that, we use R².
""")

st.divider()


# ============================================================
# 10. R-SQUARED
# ============================================================

st.header("10. What does R² tell us?")

st.markdown("""
Respondents have different levels of Institutional Trust.

Some report high trust.

Others report low trust.

The regression model tries to understand these differences using
the information we have about the respondents.
""")

st.info("""
# R² asks:

### How much of the observed variation in respondents' outcome
### scores can the complete model account for?
""")

st.markdown("### Institutional Trust example")

r2_table = pd.DataFrame({
    "Model": [
        "Model 1",
        "Model 2",
        "Model 3"
    ],
    "Information included": [
        "Traditional factors",
        "+ Subjective Social Class",
        "+ Feeling Left Behind"
    ],
    "R²": [
        "8.8%",
        "10.7%",
        "27.6%"
    ]
})

st.dataframe(
    r2_table,
    width="stretch",
    hide_index=True
)

st.markdown("""
This means:

**Model 1 → 8.8%**

The variables in Model 1 together account for **8.8% of the
observed differences in Institutional Trust scores**.

↓

**Model 2 → 10.7%**

Adding Subjective Social Class increases the proportion to
**10.7%**.

↓

**Model 3 → 27.6%**

After Feeling Left Behind is added, the complete model accounts
for **27.6% of the observed differences in Institutional Trust**.
""")


st.warning("""
### 27.6% does NOT mean:

❌ 27.6% of respondents trust institutions

❌ Feeling Left Behind decreases trust by 27.6%

❌ Feeling Left Behind alone explains 27.6%

### It means:

✅ All variables in Model 3 **together** account for 27.6% of the
observed variation in Institutional Trust scores.
""")


st.success("""
### Why compare the R² values?

Because the increase tells us whether the newly added information
helps the model account for more of the differences between respondents.

For Institutional Trust:

**10.7% → 27.6%**

when Feeling Left Behind is added.

This is a much larger improvement than the change:

**8.8% → 10.7%**

when Subjective Social Class is added.
""")

st.divider()


# ============================================================
# 11. COEFFICIENT VS R2
# ============================================================

st.header("11. Coefficient vs R²")

st.markdown("""
These statistics answer **different questions** and should not
be confused.
""")

comparison = pd.DataFrame({
    "Statistic": [
        "Coefficient",
        "R²"
    ],
    "Question it answers": [
        "In which direction, and by how much, is a predictor associated with the outcome?",
        "How much of the variation in the outcome does the complete model account for?"
    ],
    "Example": [
        "Higher Feeling Left Behind → lower Institutional Trust",
        "Model 3 accounts for 27.6% of variation in Institutional Trust"
    ]
})

st.dataframe(
    comparison,
    width="stretch",
    hide_index=True
)

st.success("""
### Easy way to remember

**Coefficient = direction and estimated relationship**

**R² = explanatory power of the complete model**
""")

st.divider()


# ============================================================
# 12. P-VALUE
# ============================================================

st.header("12. What does the p-value tell us?")

st.markdown("""
The **p-value** helps evaluate the statistical evidence for an
estimated relationship.

In this project, results with:

# p < .05

are treated as statistically significant.
""")

st.markdown("""
A small p-value provides evidence against the idea that the observed
relationship is simply compatible with a zero association under the
model assumptions.

It does **not** tell us:

- how large the relationship is;
- whether it is socially important;
- whether one variable causes another.
""")

st.divider()


# ============================================================
# 13. LOGISTIC REGRESSION
# ============================================================

st.header("13. Why is Party Representation different?")

st.markdown("""
Institutional Trust and Democratic Satisfaction are modeled with OLS.

Party Representation cannot be treated in exactly the same way because
the outcome is **binary**:
""")

st.markdown("""
# Does a party represent the respondent's views?

### YES / NO
""")

st.markdown("""
Therefore, the analysis uses **binary logistic regression**.
""")

with st.container(border=True):

    st.markdown("""
### Logistic model

Traditional variables

**+ Subjective Social Class**

**+ Feeling Left Behind**

# ↓

### Logistic regression

# ↓

### Probability / odds of answering YES to Party Representation
""")

st.divider()


# ============================================================
# 14. ODDS RATIO
# ============================================================

st.header("14. What does the Odds Ratio tell us?")

st.markdown("""
For logistic regression, an intuitive way to interpret the
relationship is the **Odds Ratio (OR)**.
""")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("""
### OR = 1

No change in the odds associated with a one-unit increase
in the predictor.
""")


with c2:

    with st.container(border=True):

        st.markdown("""
### OR > 1

Higher predictor values are associated with
**higher odds** of the outcome.
""")


with c3:

    with st.container(border=True):

        st.markdown("""
### OR < 1

Higher predictor values are associated with
**lower odds** of the outcome.
""")


st.success("""
### Result for Feeling Left Behind

**Odds Ratio = 0.706**

Holding the other variables constant, each one-point increase in
the Feeling Left Behind Index is associated with approximately:

# 29% lower odds

of saying that a political party represents the respondent's
views well.
""")

st.caption("""
Calculation: 1 − 0.706 = 0.294, or approximately 29%.
""")

st.divider()


# ============================================================
# 15. PSEUDO R2
# ============================================================

st.header("15. What about R² for Party Representation?")

st.markdown("""
Logistic regression does not use the standard OLS R².

For Party Representation, the analysis reports
**McFadden's Pseudo R²**.
""")

st.warning("""
### Important

McFadden's Pseudo R² is **not the same statistic** as OLS R².

Therefore:

**4.6% Pseudo R² for Party Representation**

should **not** be directly compared with:

**27.6% OLS R² for Institutional Trust.**

The useful comparison is between the logistic models themselves,
for example Model 2 versus Model 3.
""")

st.divider()


# ============================================================
# 16. COMPLETE WORKFLOW
# ============================================================

st.header("16. Complete analytical workflow")

st.markdown("""
Here is the entire analysis from beginning to end.
""")

with st.container(border=True):

    st.markdown("""
### STEP 1 — Survey responses

Each respondent answers the GLES questionnaire.

# ↓

### STEP 2 — Create variables

Income, education, age, region, migration background,
political interest and subjective social class remain separate
respondent characteristics.

The four Feeling Left Behind items are combined into a
**1–5 index using their mean**.

# ↓

### STEP 3 — Measure democratic outcomes

🏛️ Institutional Trust

🗳️ Democratic Satisfaction

👥 Party Representation

# ↓

### STEP 4 — Build Model 1

Traditional socioeconomic, demographic and political variables.

# ↓

### STEP 5 — Build Model 2

Model 1

**+ Subjective Social Class**

# ↓

### STEP 6 — Build Model 3

Model 2

**+ Feeling Left Behind Index**

# ↓

### STEP 7 — Estimate the relationships

**Institutional Trust → Multiple OLS regression**

**Democratic Satisfaction → Multiple OLS regression**

**Party Representation → Binary logistic regression**

# ↓

### STEP 8 — Interpret the statistics

**Coefficient → direction / estimated relationship**

**p-value → statistical evidence**

**R² → model fit for OLS**

**Odds Ratio → relationship in logistic regression**

**Pseudo R² → model fit for logistic regression**

# ↓

### STEP 9 — Compare the models

Does adding Subjective Social Class improve the model?

Does adding Feeling Left Behind improve it further?

# ↓

### STEP 10 — Interpret the substantive result

Does Feeling Left Behind provide information about democratic
attitudes beyond the socioeconomic characteristics already included?
""")

st.divider()


# ============================================================
# 17. HOW TO EXPLAIN IT
# ============================================================

st.header("17. How to explain the method in 30 seconds")

st.info("""
**“I used three nested regression models. Model 1 contains traditional
socioeconomic, demographic and political characteristics. Model 2 adds
Subjective Social Class, and Model 3 adds the Feeling Left Behind Index,
which I constructed as the mean of four survey items. For Institutional
Trust and Democratic Satisfaction I use multiple OLS regression, while
Party Representation is binary, so I use logistic regression. The
coefficients show the direction of the associations, while R² tells me
how much of the variation between respondents the complete OLS model
accounts for.”**
""")

st.divider()


# ============================================================
# 18. LIMITATIONS
# ============================================================

st.header("18. What this methodology cannot tell us")

st.warning("""
### Association is not causation

The analysis uses cross-sectional survey data.

Therefore, the regressions can identify **statistical associations**,
but they cannot demonstrate that Feeling Left Behind **causes**
lower trust, democratic dissatisfaction or lower party representation.
""")

st.markdown("""
Other factors that are not included in the models may also contribute
to differences in democratic attitudes.

The results should therefore be interpreted as evidence about
**relationships and additional explanatory information**, not as
causal effects.
""")

st.divider()


# ============================================================
# SOURCE
# ============================================================

st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")