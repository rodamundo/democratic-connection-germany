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
to investigate what helps us understand differences in people's
relationship with democracy.

The analysis builds the explanation **step by step**.
""")

    st.info("""
### The logic of the project

**First:** define what we want to explain.

**Then:** start with traditional socioeconomic, demographic and
political characteristics.

**Next:** add how people perceive their own social position.

**Finally:** ask whether Feeling Left Behind adds something that
those factors were still missing.
""")

    st.divider()


    # ========================================================
    # STEP 1 — OUTCOMES
    # ========================================================

    st.header("Step 1 — What are we trying to explain?")

    st.markdown("""
The project studies **three different aspects of people's
relationship with democracy**.

These are our **outcomes** — the things the statistical models
will try to explain.
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
### So these are the three things we want to understand:

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
We now need to ask:

> **Why do some respondents have higher or lower Trust,
> Satisfaction or Representation than others?**

We start with characteristics commonly used to understand
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
    # STEP 3 — MODEL 2
    # ========================================================

    st.header(
        "Step 3 — But objective characteristics may not tell the whole story"
    )

    st.markdown("""
Two people can have similar income, education and age but
**perceive their position in society differently**.

So we add another piece of information:
""")

    with st.container(border=True):

        st.markdown("## 🪜 Subjective Social Class")

        st.markdown("""
Instead of asking only:

> **“What income or education does this person have?”**

we also ask:

> **“Where does this person believe they stand in society?”**
""")


    st.markdown("## Model 2")

    st.markdown("""
# Model 1

Traditional factors

# +

# 🪜 Subjective Social Class

# =

# Model 2
""")


    st.info("""
### Model 2 asks:

**Does knowing how people perceive their own social position
help us understand democratic attitudes better than traditional
characteristics alone?**
""")

    st.divider()


    # ========================================================
    # STEP 4 — THE GAP
    # ========================================================

    st.header("Step 4 — What might still be missing?")

    st.markdown("""
At this point, we already know:

**income · education · age · region · migration background ·
political interest · perceived social class**

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
# This is the additional dimension the Feeling Left Behind Index
# tries to capture.
""")

    st.divider()


    # ========================================================
    # STEP 5 — LBI
    # ========================================================

    st.header("Step 5 — Measure Feeling Left Behind")

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
### There is no “Left Behind / Not Left Behind” cut-off.

Every respondent receives a score somewhere between **1 and 5**.

The higher the score, the stronger the respondent's
Feeling Left Behind.
""")

    st.divider()


    # ========================================================
    # STEP 6 — MODEL 3
    # ========================================================

    st.header("Step 6 — Add Feeling Left Behind")

    st.markdown("""
Now we can perform the central test of the project.
""")

    with st.container(border=True):

        st.markdown("""
# Model 2

Traditional factors

+

Subjective Social Class

# +

# 🧩 Feeling Left Behind Index

# =

# Model 3
""")


    st.success("""
### Model 3 asks:

**If we already know people's socioeconomic and demographic
characteristics, political interest and perceived social class,
does knowing how left behind they feel help us understand their
democratic attitudes better?**
""")

    st.divider()


    # ========================================================
    # STEP 7 — DESIGN
    # ========================================================

    st.header("Step 7 — Run the three models for each outcome")

    st.markdown("""
The same three model specifications are estimated separately
for each democratic outcome.
""")

    st.markdown("""
| What we want to explain ↓ | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| 🏛️ **Institutional Trust** | Traditional factors | + Social Class | + LBI |
| 🗳️ **Democratic Satisfaction** | Traditional factors | + Social Class | + LBI |
| 👥 **Party Representation** | Traditional factors | + Social Class | + LBI |
""")

    st.success("""
# 3 outcomes × 3 model specifications = 9 regressions
""")

    st.warning("""
### Remember

**Outcomes = what we want to explain**

Trust · Satisfaction · Representation

**Models = the information used to explain them**

Model 1 · Model 2 · Model 3
""")

    st.divider()


    # ========================================================
    # STEP 8 — R2
    # ========================================================

    st.header("Step 8 — How do we know whether explanatory power improves?")

    st.markdown("""
For Institutional Trust and Democratic Satisfaction, the analysis
uses **multiple OLS regression**.

We use **R²** as a measure of the complete model's
**explanatory power**.
""")

    st.info("""
### R² asks:

**How much of the observed differences between respondents
can the variables included in the complete model account for?**
""")

    st.warning("""
### R² does NOT tell us the direction of the relationship.

For direction, we look at the **coefficient**.

For example:

**Feeling Left Behind ↑ → Institutional Trust ↓**

comes from the negative LBI coefficient — not from R².
""")

    st.divider()


    # ========================================================
    # STEP 9 — RESULTS
    # ========================================================

    st.header("Step 9 — What happens across the three models?")


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

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Model 1",
                "8.8%"
            )

            st.caption(
                "Traditional factors"
            )

        with c2:
            st.metric(
                "Model 2",
                "10.7%",
                "+1.9 pp"
            )

            st.caption(
                "+ Subjective Social Class"
            )

        with c3:
            st.metric(
                "Model 3",
                "27.6%",
                "+16.9 pp"
            )

            st.caption(
                "+ Feeling Left Behind"
            )


        st.success("""
### What changed?

Model 1 explains **8.8%** of the observed variation in Trust.

Adding Subjective Social Class raises this to **10.7%**.

Adding Feeling Left Behind raises the explanatory power of the
complete model to **27.6%**.

### The increase associated with adding LBI is +16.9 percentage points.
""")


        st.error("""
### Direction

# Feeling Left Behind ↑ → Institutional Trust ↓
""")


        st.warning("""
**27.6% is the explanatory power of the complete Model 3.**

It does not mean that LBI alone explains 27.6% of Trust.
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

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Model 1",
                "8.5%"
            )

            st.caption(
                "Traditional factors"
            )

        with c2:
            st.metric(
                "Model 2",
                "9.6%",
                "+1.1 pp"
            )

            st.caption(
                "+ Subjective Social Class"
            )

        with c3:
            st.metric(
                "Model 3",
                "22.2%",
                "+12.6 pp"
            )

            st.caption(
                "+ Feeling Left Behind"
            )


        st.success("""
### What changed?

Model 1 explains **8.5%** of the observed variation.

Adding Subjective Social Class raises this to **9.6%**.

Adding Feeling Left Behind raises the explanatory power of the
complete model to **22.2%**.

### The increase associated with adding LBI is +12.6 percentage points.
""")


        st.error("""
### Direction

# Feeling Left Behind ↑ → Democratic Dissatisfaction ↑

Or, stated in the more intuitive direction:

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

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Model 1",
                "3.37%"
            )

            st.caption(
                "McFadden Pseudo R² · Traditional factors"
            )

        with c2:
            st.metric(
                "Model 2",
                "3.43%",
                "+0.06 pp"
            )

            st.caption(
                "+ Subjective Social Class"
            )

        with c3:
            st.metric(
                "Model 3",
                "4.62%",
                "+1.19 pp"
            )

            st.caption(
                "+ Feeling Left Behind"
            )


        st.info("""
### Why show two decimal places here?

Model 1 is **3.37%** and Model 2 is **3.43%**.

If both were rounded to one decimal place, they would appear as
**3.4% → 3.4%**, hiding the very small improvement after adding
Subjective Social Class.
""")


        st.error("""
### Direction

# Feeling Left Behind ↑ → odds of Party Representation ↓

The estimated odds ratio is **0.706**.

Holding the other included variables constant, a one-point increase
in the LBI is associated with approximately **29% lower odds**
of saying that a political party represents the respondent's views well.
""")


        st.warning("""
### Important

These values are **McFadden Pseudo R²**.

They are not the same statistic as the ordinary R² used for
Institutional Trust and Democratic Satisfaction.

Therefore, **4.62% cannot be directly compared with 27.6% or 22.2%.**
""")

    st.divider()


    # ========================================================
    # STEP 10 — MAIN RESULT
    # ========================================================

    st.header("Step 10 — What is the main result?")

    st.markdown("""
The largest increase in explanatory power occurs when
Feeling Left Behind is added.
""")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Model 2:

# 10.7%

# ↓

Add LBI

# ↓

Model 3:

# 27.6%

### +16.9 percentage points
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Model 2:

# 9.6%

# ↓

Add LBI

# ↓

Model 3:

# 22.2%

### +12.6 percentage points
""")


    st.success("""
### Main interpretation

Knowing how left behind respondents feel adds substantial
explanatory information for **Institutional Trust** and
**Democratic Satisfaction**, beyond income, education, age,
region, migration background, political interest and
Subjective Social Class.
""")


    st.markdown("""
For **Party Representation**, LBI is also statistically associated
with the outcome, but the improvement in model fit is much smaller.
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

### 3️⃣ Add perceived social position

Subjective Social Class

**= Model 2**

# ↓

### 4️⃣ Ask what may still be missing

How does the person feel society treats **people like them**?

# ↓

### 5️⃣ Measure Feeling Left Behind

Economic attention · Recognition · Services · Voice

**4 answers → mean → LBI 1–5**

# ↓

### 6️⃣ Add LBI

**= Model 3**

# ↓

### 7️⃣ Compare explanatory power

Institutional Trust:

**8.8% → 10.7% → 27.6%**

Democratic Satisfaction:

**8.5% → 9.6% → 22.2%**

Party Representation:

**3.37% → 3.43% → 4.62% Pseudo R²**

# ↓

### Main conclusion

**Feeling Left Behind adds information that the previous
models did not capture, particularly for Trust and
Democratic Satisfaction.**
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

Analytical sample: 5,039 respondents.
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