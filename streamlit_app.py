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

    st.header("Step 3 — But objective characteristics may not tell the whole story")

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
At this point, we know quite a lot about each respondent.

We know their:

**income · education · age · region · migration background ·
political interest · perceived social class**

But there is another possible dimension.

Two people can have similar characteristics **and even perceive
themselves as belonging to a similar social class**, while having
very different experiences of how society treats people like them.
""")

    st.markdown("### For example:")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### Person A")

            st.markdown("""
Feels that people like them are:

✅ recognized

✅ economically considered

✅ adequately served

✅ able to express their views
""")

    with c2:
        with st.container(border=True):

            st.markdown("### Person B")

            st.markdown("""
Feels that people like them are:

❌ overlooked

❌ insufficiently recognized

❌ poorly served

❌ not heard
""")


    st.success("""
# This is the gap the Feeling Left Behind Index tries to capture.
""")

    st.divider()


    # ========================================================
    # STEP 5 — LBI
    # ========================================================

    st.header("Step 5 — Measure Feeling Left Behind")

    st.markdown("""
The GLES survey contains four questions that allow us to measure
this subjective experience.
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

    st.header("Step 6 — Now add Feeling Left Behind")

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
    # STEP 7 — 3 x 3
    # ========================================================

    st.header("Step 7 — Run the three models for each outcome")

    st.markdown("""
The same sequence is tested separately for each of the
three democratic outcomes.
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

**Outcomes** are what we want to explain:

Trust · Satisfaction · Representation

**Models** are the information we use to try to explain them:

Model 1 · Model 2 · Model 3
""")

    st.divider()


    # ========================================================
    # STEP 8 — RESULTS
    # ========================================================

    st.header("Step 8 — What changes when LBI is added?")

    st.markdown("""
Now we compare the models.

For Institutional Trust and Democratic Satisfaction, **R²**
shows the explanatory power of the complete model.
""")


    # --------------------------------------------------------
    # TRUST RESULT
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🏛️ Institutional Trust")

        st.markdown("""
**What are we explaining?**

Average trust across:

Federal Government · Bundestag · Political Parties · Politicians ·
Police · Justice · Science · Public-Service Broadcasting

**Scale: 1–11**
""")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Model 1",
            "8.8%"
        )

        c2.metric(
            "Model 2",
            "10.7%"
        )

        c3.metric(
            "Model 3",
            "27.6%",
            "+16.9 pp"
        )

        st.markdown("""
### What happened?

Traditional factors alone:

**8.8% explanatory power**

↓

Add Subjective Social Class:

**10.7%**

↓

Add Feeling Left Behind:

# **27.6%**
""")

        st.success("""
Adding LBI increases explanatory power by **16.9 percentage points**
compared with Model 2.
""")

        st.error("""
### Direction of the relationship

**Feeling Left Behind ↑ → Institutional Trust ↓**
""")


    # --------------------------------------------------------
    # SATISFACTION RESULT
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🗳️ Democratic Satisfaction")

        st.markdown("""
**What are we explaining?**

How satisfied respondents are with how democracy works.

**1 = Very satisfied**

to

**4 = Not at all satisfied**

So higher scores mean **greater dissatisfaction**.
""")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Model 1",
            "8.2%"
        )

        c2.metric(
            "Model 2",
            "9.6%"
        )

        c3.metric(
            "Model 3",
            "22.2%",
            "+12.6 pp"
        )

        st.success("""
Adding LBI increases explanatory power by **12.6 percentage points**
compared with Model 2.
""")

        st.error("""
### Direction of the relationship

**Feeling Left Behind ↑ → Democratic Dissatisfaction ↑**

In other words:

**Feeling Left Behind ↑ → Satisfaction ↓**
""")


    # --------------------------------------------------------
    # REPRESENTATION RESULT
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 👥 Party Representation")

        st.markdown("""
**What are we explaining?**

Whether respondents say that a political party represents
their political views well.

# Yes / No
""")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Model 1",
            "2.9%"
        )

        c2.metric(
            "Model 2",
            "3.4%"
        )

        c3.metric(
            "Model 3",
            "4.6%",
            "+1.2 pp"
        )

        st.markdown("""
Because this outcome is **Yes / No**, it uses logistic regression
and **McFadden's Pseudo R²** rather than ordinary R².
""")

        st.error("""
### Direction of the relationship

**Feeling Left Behind ↑ → odds of Party Representation ↓**
""")


    st.warning("""
### Important comparison rule

The Party Representation percentages are **Pseudo R²**.

They should not be directly compared numerically with the ordinary
OLS R² values for Institutional Trust and Democratic Satisfaction.
""")

    st.divider()


    # ========================================================
    # STEP 9 — WHAT DOES THIS MEAN?
    # ========================================================

    st.header("Step 9 — What is the main finding?")

    st.markdown("""
The strongest change appears when Feeling Left Behind is added
to the models for **Institutional Trust** and
**Democratic Satisfaction**.
""")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Before LBI:

# 10.7%

After LBI:

# 27.6%

### +16.9 percentage points
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Before LBI:

# 9.6%

After LBI:

# 22.2%

### +12.6 percentage points
""")


    st.success("""
### Main interpretation

Feeling Left Behind adds substantial explanatory information
for **Institutional Trust** and **Democratic Satisfaction**
beyond the characteristics already included in Model 2.
""")

    st.warning("""
This does **not** mean that LBI alone explains 27.6% of
Institutional Trust.

**27.6% is the explanatory power of the complete Model 3.**

The additional explanatory power after LBI is added is
**16.9 percentage points**.
""")

    st.divider()


    # ========================================================
    # FINAL STORY
    # ========================================================

    st.header("The whole story")

    st.markdown("""
### 1️⃣ What do we want to understand?

Trust · Satisfaction · Representation

# ↓

### 2️⃣ Start with traditional characteristics

Income · Education · Age · Region · Migration · Political Interest

**= Model 1**

# ↓

### 3️⃣ Add where people think they stand socially

Subjective Social Class

**= Model 2**

# ↓

### 4️⃣ Ask what might still be missing

How do people feel society treats **people like them**?

# ↓

### 5️⃣ Measure that experience

Economic attention · Recognition · Services · Voice

**= Feeling Left Behind Index**

# ↓

### 6️⃣ Add LBI

**= Model 3**

# ↓

### 7️⃣ Compare explanatory power

For Institutional Trust:

**10.7% → 27.6%**

For Democratic Satisfaction:

**9.6% → 22.2%**

# ↓

### Main conclusion

**Feeling Left Behind adds information that traditional
characteristics and Subjective Social Class did not capture.**
""")

    st.warning("""
### Association ≠ causation

The analysis identifies statistical associations.

Because the data are cross-sectional, it cannot demonstrate that
Feeling Left Behind causes lower trust, dissatisfaction or
lower Party Representation.
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