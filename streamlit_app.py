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
# HOME PAGE
# ============================================================

def home():

    # ========================================================
    # INTRO
    # ========================================================

    st.title("🏛️ Feeling Left Behind and Democracy in Germany")

    st.subheader(
        "Does feeling socially left behind help us understand "
        "people's relationship with democracy?"
    )

    st.markdown("""
This project uses the **German Longitudinal Election Study (GLES 2025)**
to investigate whether people's subjective experience of being left
behind adds information beyond income, education and social class.
""")

    st.info("""
### The project in one sentence

We first measure **three democratic outcomes**, then test whether
traditional characteristics, social class and finally
**Feeling Left Behind** help us understand why people differ on them.
""")

    st.divider()


    # ========================================================
    # 1. OUTCOMES
    # ========================================================

    st.header("1. First: what are we trying to explain?")

    st.markdown("""
The project studies **three different aspects of people's relationship
with democracy**.

These are called the **outcomes**.

They are **not the three statistical models**.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("## 🏛️ Institutional Trust")

            st.markdown("""
### Simple question

**“How much do I trust important institutions?”**

Respondents rate their trust in **eight institutions** from:

**1 = Do not trust at all**

to

**11 = Trust completely**

The eight answers are averaged to create one
**Institutional Trust score** for each respondent.
""")

            st.caption(
                "Numerical outcome → analyzed with OLS regression."
            )


    with c2:
        with st.container(border=True):

            st.markdown("## 🗳️ Democratic Satisfaction")

            st.markdown("""
### Simple question

**“How satisfied am I with how democracy works?”**

Respondents answer on a scale from:

**1 = Very satisfied**

to

**4 = Not at all satisfied**

So a **higher number means greater dissatisfaction**.

This is one survey measure — it is not an index made from
several questions.
""")

            st.caption(
                "Ordered numerical outcome → analyzed with OLS regression."
            )


    with c3:
        with st.container(border=True):

            st.markdown("## 👥 Party Representation")

            st.markdown("""
### Simple question

**“Does any political party represent my political views well?”**

The answer is:

# Yes / No

Unlike the other two outcomes, this is not a continuous score.

It is a **binary outcome**.
""")

            st.caption(
                "Binary outcome → analyzed with logistic regression."
            )


    st.success("""
### Remember this distinction

🏛️ **Institutional Trust** = trust in institutions

🗳️ **Democratic Satisfaction** = satisfaction with how democracy works

👥 **Party Representation** = whether a party represents the respondent's views

These are the **three things we want to understand**.
""")

    st.divider()


    # ========================================================
    # 2. FEELING LEFT BEHIND
    # ========================================================

    st.header("2. What might help explain these differences?")

    st.markdown("""
People with similar income, education or age do not necessarily
have the same relationship with democracy.

This project therefore asks whether another dimension matters:
""")

    st.success("""
# 🧩 Feeling Left Behind

**Do I feel that people like me are seen, recognized, served and heard?**
""")

    st.markdown("""
The GLES survey contains four questions related to this experience.
""")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown("### 💶 Economic attention")
            st.write(
                "Are the economic concerns of people like me being overlooked?"
            )

    with c2:
        with st.container(border=True):
            st.markdown("### 👏 Recognition")
            st.write(
                "Is the contribution of people like me sufficiently recognized?"
            )

    with c3:
        with st.container(border=True):
            st.markdown("### 🏥 Services")
            st.write(
                "Do people like me have adequate access to basic services?"
            )

    with c4:
        with st.container(border=True):
            st.markdown("### 🗣️ Voice")
            st.write(
                "Do people like me feel able to express their opinions?"
            )


    st.markdown("### How do four answers become one measure?")

    with st.container(border=True):

        st.markdown("""
### Four survey answers

Economic attention + Recognition + Services + Voice

# ↓

### Calculate the mean for each respondent

# ↓

# 🧩 Left Behind Index

**1 ───────── 2 ───────── 3 ───────── 4 ───────── 5**

Lower Feeling Left Behind　　　　　　　　　Higher Feeling Left Behind
""")


    st.info("""
There is **no cut-off** between “left behind” and “not left behind”.

Every respondent receives a score somewhere on the 1–5 scale.
""")

    st.divider()


    # ========================================================
    # 3. THREE MODELS
    # ========================================================

    st.header("3. How do we test what explains the three outcomes?")

    st.markdown("""
Now we know:

**WHAT we want to explain**

→ Trust, Satisfaction and Representation

and we have a new possible explanation:

→ Feeling Left Behind.

The next step is to compare **three statistical models**.
""")

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

            st.markdown("""
**Question:**

How much can these characteristics help us understand
differences in the democratic outcome?
""")


    with c2:
        with st.container(border=True):

            st.markdown("## Model 2")

            st.markdown("### Model 1 + Social Class")

            st.markdown("""
Everything from Model 1

# +

🪜 **Subjective Social Class**

Where the respondent believes they stand in society.
""")

            st.markdown("""
**Question:**

Does perceived social position add information beyond
the traditional factors?
""")


    with c3:
        with st.container(border=True):

            st.markdown("## Model 3")

            st.markdown("### Model 2 + Feeling Left Behind")

            st.markdown("""
Everything from Model 2

# +

🧩 **Left Behind Index**

How left behind the respondent feels.
""")

            st.markdown("""
**Question:**

Does Feeling Left Behind add information beyond
everything we already know?
""")


    st.info("""
### Very important

Model 1, Model 2 and Model 3 are **not scores given to people**.

They are three different sets of information entered into
the regression.
""")

    st.divider()


    # ========================================================
    # 4. COMPLETE DESIGN
    # ========================================================

    st.header("4. The complete research design")

    st.markdown("""
The same three models are applied separately to each democratic outcome.
""")

    st.markdown("""
| What we want to explain | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| 🏛️ **Institutional Trust** | Traditional factors | + Social Class | + Feeling Left Behind |
| 🗳️ **Democratic Satisfaction** | Traditional factors | + Social Class | + Feeling Left Behind |
| 👥 **Party Representation** | Traditional factors | + Social Class | + Feeling Left Behind |
""")

    st.success("""
### 3 outcomes × 3 model specifications = 9 regressions

The comparison tells us whether adding new information improves
our ability to understand differences between respondents.
""")

    st.divider()


    # ========================================================
    # 5. R-SQUARED
    # ========================================================

    st.header("5. How do we know whether the model improves?")

    st.markdown("""
For **Institutional Trust** and **Democratic Satisfaction**, the analysis
uses multiple OLS regression.

One important measure is **R²**, which can be understood here as the
model's **explanatory power**.
""")

    st.info("""
### R² = explanatory power

It tells us how much of the observed differences between respondents
on the outcome can be accounted for by the variables in the model.
""")

    st.markdown("""
### Example: Institutional Trust

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
### The important comparison

**10.7% → 27.6%**

Adding Feeling Left Behind increases the model's explanatory power
by **16.9 percentage points**.

The **27.6% belongs to the complete Model 3**.

It does NOT mean that Feeling Left Behind alone explains 27.6%.
""")

    st.divider()


    # ========================================================
    # 6. COEFFICIENT VS R2
    # ========================================================

    st.header("6. Two different statistical questions")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### ↕️ Coefficient")

            st.markdown("""
Answers:

**In which direction is the relationship?**

For Institutional Trust:

**Feeling Left Behind ↑**

# ↓

**Institutional Trust ↓**
""")


    with c2:
        with st.container(border=True):

            st.markdown("### 📊 R²")

            st.markdown("""
Answers:

**How much of the differences in the outcome can the complete
model explain?**

For final Institutional Trust model:

# 27.6%
""")


    st.info("""
### Easy way to remember

**Coefficient = direction and strength of an association**

**R² = explanatory power of the complete model**
""")

    st.divider()


    # ========================================================
    # 7. RESULTS
    # ========================================================

    st.header("7. What did we find?")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.metric(
                "Final explanatory power",
                "27.6%",
                delta="+16.9 pp"
            )

            st.markdown("""
**Before LBI:** 10.7%

**After LBI:** 27.6%

Higher Feeling Left Behind is associated with
**lower Institutional Trust**.
""")


    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.metric(
                "Final explanatory power",
                "22.2%",
                delta="+12.6 pp"
            )

            st.markdown("""
**Before LBI:** 9.6%

**After LBI:** 22.2%

Higher Feeling Left Behind is associated with
**greater democratic dissatisfaction**.
""")


    with c3:
        with st.container(border=True):

            st.markdown("### 👥 Party Representation")

            st.metric(
                "Final Pseudo R²",
                "4.6%",
                delta="+1.2 pp"
            )

            st.markdown("""
**Before LBI:** 3.4%

**After LBI:** 4.6%

Higher Feeling Left Behind is associated with
**lower odds of feeling represented**.
""")


    st.warning("""
Party Representation uses **logistic regression and McFadden's
Pseudo R²** because the outcome is Yes/No.

Its 4.6% should therefore **not be directly compared numerically**
with the OLS R² values of 27.6% and 22.2%.
""")

    st.divider()


    # ========================================================
    # FINAL MAP
    # ========================================================

    st.header("The whole project in one map")

    st.markdown("""
### 1️⃣ What do we want to understand?

🏛️ Trust · 🗳️ Satisfaction · 👥 Representation

# ↓

### 2️⃣ What information do we already have?

Income · Education · Age · Region · Migration · Political Interest

# ↓

### 3️⃣ What else do we add?

🪜 Subjective Social Class

# ↓

### 4️⃣ What new information does this project test?

🧩 Feeling Left Behind

# ↓

### 5️⃣ Does the model explain more after adding it?

**Yes — particularly for Institutional Trust and Democratic Satisfaction.**
""")

    st.warning("""
### Final methodological caution

These results show **statistical associations**, not causation.

The data are cross-sectional, so the analysis cannot demonstrate
that Feeling Left Behind causes changes in democratic attitudes.
""")

    st.divider()

    st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
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