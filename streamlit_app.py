import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Feeling Left Behind and Democracy in Germany",
    page_icon="🏛️",
    layout="wide"
)


# ============================================================
# HOME
# ============================================================

def home():

    st.title("🏛️ Feeling Left Behind and Democracy in Germany")

    st.subheader(
        "Does feeling socially left behind help us understand "
        "people's relationship with democracy?"
    )

    st.markdown("""
This project uses the **German Longitudinal Election Study (GLES 2025)**
to investigate whether Feeling Left Behind adds information beyond
traditional socioeconomic, demographic and political characteristics.

The analysis builds the argument **step by step**.
""")

    st.info("""
### The logic of the project

**First:** define what we want to explain.

**Then:** test what traditional characteristics already tell us.

**Finally:** add Feeling Left Behind and ask whether it helps us
understand democratic attitudes better.
""")

    st.divider()


    # ========================================================
    # STEP 1 — OUTCOMES
    # ========================================================

    st.header("Step 1 — What are we trying to explain?")

    st.markdown("""
The project studies **three different aspects of people's
relationship with democracy**.

These are the **outcomes** — the things the statistical models
try to explain.
""")


    # --------------------------------------------------------
    # INSTITUTIONAL TRUST
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🏛️ Institutional Trust")

        st.markdown("""
### What does this mean?

**How much does a person trust important institutions?**

Each respondent rated their trust in **8 institutions** from:

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
### How do we get one Trust score?

**8 trust ratings**

# ↓

**Calculate the mean**

# ↓

### Institutional Trust score: 1–11

**Higher score = higher overall institutional trust**
""")


    # --------------------------------------------------------
    # DEMOCRATIC SATISFACTION
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🗳️ Democratic Satisfaction")

        st.markdown("""
### What does this mean?

**How satisfied is a person with how democracy works in Germany?**

This comes from **one survey question**:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

        st.warning("""
### Important

This scale runs in the opposite direction from Trust.

**Higher score = greater dissatisfaction**

So:

### Score ↑ → Satisfaction ↓
""")


    # --------------------------------------------------------
    # PARTY REPRESENTATION
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 👥 Party Representation")

        st.markdown("""
### What does this mean?

**Does a political party represent the respondent's
political views well?**

The answer is:

# YES / NO

There is no average Party Representation score.
""")


    st.success("""
### These are the three things we want to understand:

🏛️ **Do people trust institutions?**

🗳️ **Are people satisfied with how democracy works?**

👥 **Do people feel represented by a political party?**
""")

    st.divider()


    # ========================================================
    # STEP 2 — MODEL 1
    # ========================================================

    st.header("Step 2 — Start with what we already know")

    st.markdown("""
Why do respondents differ in Trust, Satisfaction and Representation?

We begin with characteristics commonly used to understand
differences between people.
""")

    st.markdown("## Model 1 — Traditional factors")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("""
### 💰 Economic

**Household Income**

How much income does the respondent's household have?
""")

    with c2:
        with st.container(border=True):

            st.markdown("""
### 🎓 Demographic / social

**Education**

**Age**

**East / West Germany**

**Migration Background**
""")

    with c3:
        with st.container(border=True):

            st.markdown("""
### 🗳️ Political

**Political Interest**

How interested is the respondent in politics?
""")


    st.info("""
### Model 1 asks:

**How much can these traditional characteristics help us understand
why respondents differ in Trust, Satisfaction and Representation?**
""")

    st.markdown("""
The variables are entered **together in a multiple regression**.

They are not averaged into one score.
""")

    st.divider()


    # ========================================================
    # STEP 3 — THE GAP
    # ========================================================

    st.header("Step 3 — What might traditional factors be missing?")

    st.markdown("""
At this point, we already know quite a lot about the respondent:

**income · education · age · region · migration background ·
political interest**

But two people with similar characteristics may still feel
very differently about how society treats **people like them**.
""")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### Person A")

            st.markdown("""
Feels that people like them are:

✅ economically considered

✅ recognized

✅ adequately served

✅ able to express their views
""")

    with c2:
        with st.container(border=True):

            st.markdown("### Person B")

            st.markdown("""
Feels that people like them are:

❌ economically overlooked

❌ insufficiently recognized

❌ poorly served

❌ not heard
""")


    st.success("""
# This is the additional dimension the Feeling Left Behind Index tries to capture.
""")

    st.divider()


    # ========================================================
    # STEP 4 — LBI
    # ========================================================

    st.header("Step 4 — Measure Feeling Left Behind")

    st.markdown("""
The GLES survey contains four questions that allow us to capture
this subjective social experience.
""")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):

            st.markdown("### 💶 Economic attention")

            st.markdown("""
Are the economic concerns of people like me receiving
sufficient attention?
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 👏 Recognition")

            st.markdown("""
Do people like me receive sufficient recognition
for what they contribute?
""")

    with c3:
        with st.container(border=True):

            st.markdown("### 🏥 Services")

            st.markdown("""
Do people like me have adequate access to
basic services and infrastructure?
""")

    with c4:
        with st.container(border=True):

            st.markdown("### 🗣️ Voice")

            st.markdown("""
Do people like me feel able to express
their opinions?
""")


    st.markdown("## How do four answers become one measure?")

    with st.container(border=True):

        st.markdown("""
### Economic attention

+

### Recognition

+

### Services

+

### Voice

# ↓

### Mean of the four responses

# ↓

# 🧩 Left Behind Index

### 1 ───── 2 ───── 3 ───── 4 ───── 5

**Lower Feeling Left Behind　　　　　　　　　Higher Feeling Left Behind**
""")


    st.info("""
There is no “Left Behind / Not Left Behind” cut-off.

Every respondent receives a score between **1 and 5**.

The higher the score, the stronger the respondent's
Feeling Left Behind.
""")

    st.divider()


    # ========================================================
    # STEP 5 — MODEL 2
    # ========================================================

    st.header("Step 5 — Add Feeling Left Behind")

    st.markdown("""
Now we perform the central test of the project.
""")

    with st.container(border=True):

        st.markdown("""
# Model 1

Traditional socioeconomic, demographic and political factors

# +

# 🧩 Feeling Left Behind Index

# =

# Model 2
""")


    st.success("""
### Model 2 asks:

**If we already know people's traditional socioeconomic,
demographic and political characteristics, does knowing how
left behind they feel help us understand their democratic
attitudes better?**
""")

    st.divider()


    # ========================================================
    # STEP 6 — DESIGN
    # ========================================================

    st.header("Step 6 — Run both models for each outcome")

    st.markdown("""
The same two model specifications are estimated separately
for each democratic outcome.
""")

    st.markdown("""
| What we want to explain ↓ | Model 1 | Model 2 |
|---|---|---|
| 🏛️ **Institutional Trust** | Traditional factors | + Feeling Left Behind |
| 🗳️ **Democratic Satisfaction** | Traditional factors | + Feeling Left Behind |
| 👥 **Party Representation** | Traditional factors | + Feeling Left Behind |
""")

    st.success("""
# 3 outcomes × 2 model specifications = 6 regressions
""")

    st.warning("""
### Remember

**Outcomes = what we want to explain**

Trust · Satisfaction · Representation

**Models = the information used to explain them**

Model 1 · Model 2
""")

    st.divider()


    # ========================================================
    # STEP 7 — R2
    # ========================================================

    st.header("Step 7 — How do we know whether the model improves?")

    st.markdown("""
For Institutional Trust and Democratic Satisfaction, the analysis
uses **multiple OLS regression**.

One measure of model fit is **R²**.
""")

    st.info("""
### R² asks:

**How much of the observed differences between respondents
can the variables included in the model account for?**
""")

    st.warning("""
### R² must be interpreted carefully

Ordinary R² will not decrease when a new predictor is added.

For that reason, the analysis does **not rely on R² alone**.

For the OLS models we also examine **Adjusted R²**, which penalizes
the addition of predictors that contribute little, together with
the LBI coefficient and its statistical significance.
""")

    st.markdown("""
### Direction is a different question

R² tells us about **model fit**.

The coefficient tells us the **direction of the association**.

For example:

**Feeling Left Behind ↑ → Institutional Trust ↓**

comes from the negative LBI coefficient — not from R².
""")

    st.divider()


    # ========================================================
    # STEP 8 — RESULTS
    # ========================================================

    st.header("Step 8 — What changes when Feeling Left Behind is added?")


    # --------------------------------------------------------
    # TRUST
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🏛️ Institutional Trust")

        st.markdown("""
### What are we explaining?

The respondent's **average trust across 8 institutions**:

Federal Government · Bundestag · Political Parties · Politicians ·
Police · Justice · Science · Public-Service Broadcasting

**Scale: 1–11**

Higher score = higher Institutional Trust.
""")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Model 1",
                "8.46%"
            )

            st.caption(
                "Traditional factors · OLS R²"
            )

        with c2:
            st.metric(
                "Model 2",
                "26.29%",
                "+17.83 pp"
            )

            st.caption(
                "+ Feeling Left Behind · OLS R²"
            )

        st.success("""
### What changed?

Model 1 accounts for **8.46%** of the observed variation in Trust.

After Feeling Left Behind is added, Model 2 accounts for **26.29%**.

### Increase in R² = +17.83 percentage points
""")

        st.info("""
**Adjusted R²:** 8.37% → 26.20%

The increase remains essentially the same after penalizing
the additional predictor.
""")

        st.error("""
### Direction

# Feeling Left Behind ↑ → Institutional Trust ↓
""")


    # --------------------------------------------------------
    # SATISFACTION
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🗳️ Democratic Satisfaction")

        st.markdown("""
### What are we explaining?

How satisfied respondents are with how democracy works in Germany.

**1 = Very satisfied**

to

**4 = Not at all satisfied**

Therefore:

**Higher score = greater democratic dissatisfaction.**
""")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Model 1",
                "7.97%"
            )

            st.caption(
                "Traditional factors · OLS R²"
            )

        with c2:
            st.metric(
                "Model 2",
                "21.20%",
                "+13.23 pp"
            )

            st.caption(
                "+ Feeling Left Behind · OLS R²"
            )

        st.success("""
### What changed?

Model 1 accounts for **7.97%** of the observed variation.

After Feeling Left Behind is added, Model 2 accounts for **21.20%**.

### Increase in R² = +13.23 percentage points
""")

        st.info("""
**Adjusted R²:** 7.87% → 21.10%

Again, the improvement remains essentially unchanged after adjustment.
""")

        st.error("""
### Direction

# Feeling Left Behind ↑ → Democratic Dissatisfaction ↑

Or, stated more intuitively:

# Feeling Left Behind ↑ → Democratic Satisfaction ↓
""")


    # --------------------------------------------------------
    # PARTY REPRESENTATION
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 👥 Party Representation")

        st.markdown("""
### What are we explaining?

Whether respondents say that a political party represents
their personal political views well.

# Yes / No

Because this outcome is binary, it uses **logistic regression**
rather than OLS.
""")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Model 1",
                "3.33%"
            )

            st.caption(
                "Traditional factors · McFadden Pseudo R²"
            )

        with c2:
            st.metric(
                "Model 2",
                "4.65%",
                "+1.32 pp"
            )

            st.caption(
                "+ Feeling Left Behind · McFadden Pseudo R²"
            )

        st.error("""
### Direction

# Feeling Left Behind ↑ → odds of Party Representation ↓

The Odds Ratio is **0.705**.

A one-point increase in the LBI is associated with approximately
**29.5% lower odds** of saying that a political party represents
the respondent's views well, holding the other variables constant.
""")

        st.warning("""
### Important

Party Representation uses **McFadden Pseudo R²**.

It is not the same statistic as ordinary OLS R².

Therefore, **4.65% cannot be directly compared numerically
with 26.29% or 21.20%.**
""")

    st.divider()


    # ========================================================
    # STEP 9 — MAIN RESULT
    # ========================================================

    st.header("Step 9 — What is the main result?")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Traditional factors:

# 8.46%

# ↓

Add LBI

# ↓

# 26.29%

### +17.83 percentage points
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Traditional factors:

# 7.97%

# ↓

Add LBI

# ↓

# 21.20%

### +13.23 percentage points
""")


    st.success("""
### Main interpretation

Knowing how left behind respondents feel adds substantial
explanatory information for **Institutional Trust** and
**Democratic Satisfaction**, beyond income, education, age,
region, migration background and political interest.
""")

    st.markdown("""
For **Party Representation**, Feeling Left Behind is also strongly
associated with the outcome, but the improvement in model fit
is much smaller.
""")

    st.divider()


    # ========================================================
    # FINAL STORY
    # ========================================================

    st.header("The whole story")

    st.markdown("""
### 1️⃣ Define what we want to explain

🏛️ Institutional Trust

🗳️ Democratic Satisfaction

👥 Party Representation

# ↓

### 2️⃣ Start with traditional information

Income · Education · Age · Region · Migration · Political Interest

**= Model 1**

# ↓

### 3️⃣ Ask what might still be missing

How does the person feel society treats **people like them**?

# ↓

### 4️⃣ Measure Feeling Left Behind

Economic attention · Recognition · Services · Voice

**4 answers → mean → LBI 1–5**

# ↓

### 5️⃣ Add LBI

**= Model 2**

# ↓

### 6️⃣ Compare model fit

Institutional Trust:

**8.46% → 26.29%**

Democratic Satisfaction:

**7.97% → 21.20%**

Party Representation:

**3.33% → 4.65% Pseudo R²**

# ↓

### Main conclusion

**Feeling Left Behind adds information that traditional
characteristics alone do not capture, particularly for Trust
and Democratic Satisfaction.**
""")


    st.warning("""
### Association ≠ causation

The analysis identifies statistical associations.

Because the data are cross-sectional, it cannot demonstrate that
Feeling Left Behind causes lower trust, democratic dissatisfaction
or lower Party Representation.
""")


    st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Outcome-specific complete-case samples:
Institutional Trust N = 5,653;
Democratic Satisfaction N = 5,676;
Party Representation N = 5,096.
""")


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

home_page = st.Page(
    home,
    title="Home",
    icon="🏠",
    default=True
)

left_behind_page = st.Page(
    "pages/1_Feeling_Left_Behind.py",
    title="Feeling Left Behind",
    icon="🧩"
)

research_page = st.Page(
    "pages/2_Research.py",
    title="Research",
    icon="📚"
)

results_page = st.Page(
    "pages/3_Results.py",
    title="Results",
    icon="📊"
)

methodology_page = st.Page(
    "pages/4_Methodology.py",
    title="Methodology",
    icon="🔬"
)

policy_page = st.Page(
    "pages/5_Policy_Implications.py",
    title="Policy Implications",
    icon="💡"
)

about_page = st.Page(
    "pages/6_About.py",
    title="About",
    icon="👤"
)


# ============================================================
# RUN NAVIGATION
# ============================================================

pg = st.navigation([
    home_page,
    left_behind_page,
    research_page,
    results_page,
    methodology_page,
    policy_page,
    about_page
])

pg.run()