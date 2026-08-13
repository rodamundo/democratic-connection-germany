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
traditional socioeconomic and demographic characteristics.
""")

    st.info("""
### The project in one sentence

We study **three aspects of people's relationship with democracy**
and test whether Feeling Left Behind helps us understand why
respondents differ on them.
""")

    st.divider()


    # ========================================================
    # 1. THREE OUTCOMES
    # ========================================================

    st.header("1. What exactly are we trying to understand?")

    st.markdown("""
Before looking at models or statistics, we need to define the
**three democratic outcomes**.

These are the three things we want to explain.
""")

    # --------------------------------------------------------
    # INSTITUTIONAL TRUST
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🏛️ Institutional Trust")

        st.markdown("""
### Simple question:

**How much does a person trust important institutions?**

Each respondent rated their trust in **8 institutions** from:

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
The eight answers are averaged:

### 8 trust ratings → mean → one Institutional Trust score

A respondent with a **higher score has higher overall institutional trust**.
""")

    # --------------------------------------------------------
    # DEMOCRATIC SATISFACTION
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🗳️ Democratic Satisfaction")

        st.markdown("""
### Simple question:

**How satisfied is a person with how democracy works in Germany?**

This comes from **one survey question**.

The response scale is:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

        st.warning("""
### Important direction

Here, a **higher number means greater democratic dissatisfaction**.

So:

**Score ↑ → Satisfaction ↓**
""")

    # --------------------------------------------------------
    # PARTY REPRESENTATION
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 👥 Party Representation")

        st.markdown("""
### Simple question:

**Does a political party represent the respondent's political views well?**

The response is:

# Yes / No

This is therefore different from the other two outcomes.

There is **no average representation score**.
""")

    st.success("""
### Three outcomes — three different ideas

🏛️ **Institutional Trust**  
Do I trust important institutions?

🗳️ **Democratic Satisfaction**  
Am I satisfied with how democracy works?

👥 **Party Representation**  
Does a political party represent my views?

These are the **outcomes**.

They are not Model 1, Model 2 and Model 3.
""")

    st.divider()


    # ========================================================
    # 2. FEELING LEFT BEHIND
    # ========================================================

    st.header("2. What might help explain these differences?")

    st.markdown("""
Two people can have similar income, education or age and still
have very different relationships with democracy.

This project therefore tests another dimension:
""")

    st.success("""
# 🧩 Feeling Left Behind

**Does a person feel that people like them are seen,
recognized, served and heard?**
""")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown("### 💶 Economic attention")
            st.write(
                "Are the economic concerns of people like me receiving enough attention?"
            )

    with c2:
        with st.container(border=True):
            st.markdown("### 👏 Recognition")
            st.write(
                "Do people like me receive sufficient recognition?"
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

    st.markdown("### From four answers to one score")

    with st.container(border=True):

        st.markdown("""
**Economic attention + Recognition + Services + Voice**

# ↓

### Mean of the four responses

# ↓

# Left Behind Index: 1–5

**1 ───────── 2 ───────── 3 ───────── 4 ───────── 5**

Lower Feeling Left Behind　　　　　　　　　Higher Feeling Left Behind
""")

    st.info("""
There is no cut-off between “left behind” and “not left behind”.

Every respondent receives a position on the 1–5 scale.
""")

    st.divider()


    # ========================================================
    # 3. THREE MODELS
    # ========================================================

    st.header("3. How do we test what explains the outcomes?")

    st.markdown("""
Now we know **what we want to explain**.

The next step is to test different sets of information about
the respondents.

We do this with **three nested regression models**.
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

How much do these traditional characteristics help us
understand differences in the outcome?
""")

    with c2:
        with st.container(border=True):

            st.markdown("## Model 2")

            st.markdown("### Model 1 + Social Class")

            st.markdown("""
Everything from Model 1

# +

🪜 **Subjective Social Class**
""")

            st.markdown("""
**Question:**

Does people's perceived social position add
explanatory information?
""")

    with c3:
        with st.container(border=True):

            st.markdown("## Model 3")

            st.markdown("### Model 2 + Feeling Left Behind")

            st.markdown("""
Everything from Model 2

# +

🧩 **Left Behind Index**
""")

            st.markdown("""
**Question:**

Does Feeling Left Behind add information beyond
everything already included?
""")

    st.warning("""
### Do not confuse models and outcomes

**Outcomes = what we want to explain**

Trust · Satisfaction · Representation

**Models = what we use to try to explain them**

Model 1 · Model 2 · Model 3
""")

    st.divider()


    # ========================================================
    # 4. COMPLETE DESIGN
    # ========================================================

    st.header("4. How does the complete analysis work?")

    st.markdown("""
We run the same three model specifications separately
for each outcome.
""")

    st.markdown("""
| Outcome ↓ | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| 🏛️ **Institutional Trust** | Traditional factors | + Social Class | + LBI |
| 🗳️ **Democratic Satisfaction** | Traditional factors | + Social Class | + LBI |
| 👥 **Party Representation** | Traditional factors | + Social Class | + LBI |
""")

    st.success("""
# 3 outcomes × 3 model specifications = 9 regressions
""")

    st.divider()


    # ========================================================
    # 5. RESULTS
    # ========================================================

    st.header("5. What did we find?")

    # TRUST
    with st.container(border=True):

        st.markdown("## 🏛️ Institutional Trust")

        st.caption(
            "Average trust across 8 institutions, measured from 1 to 11."
        )

        c1, c2, c3 = st.columns(3)

        c1.metric("Model 1", "8.8%")
        c2.metric("Model 2", "10.7%")
        c3.metric("Model 3", "27.6%", "+16.9 pp vs Model 2")

        st.markdown("""
### What does this mean?

Before LBI, Model 2 accounts for **10.7% of the observed
differences in Institutional Trust between respondents**.

After adding LBI, the complete Model 3 accounts for **27.6%**.

### LBI ↑ → Institutional Trust ↓

Higher Feeling Left Behind is associated with lower trust.
""")

    # SATISFACTION
    with st.container(border=True):

        st.markdown("## 🗳️ Democratic Satisfaction")

        st.caption(
            "One survey response from 1 = Very satisfied "
            "to 4 = Not at all satisfied."
        )

        c1, c2, c3 = st.columns(3)

        c1.metric("Model 1", "8.2%")
        c2.metric("Model 2", "9.6%")
        c3.metric("Model 3", "22.2%", "+12.6 pp vs Model 2")

        st.markdown("""
### What does this mean?

After adding LBI, the complete Model 3 accounts for **22.2%**
of the observed variation in Democratic Satisfaction.

Because higher outcome scores mean **greater dissatisfaction**:

### LBI ↑ → Democratic Dissatisfaction ↑
""")

    # REPRESENTATION
    with st.container(border=True):

        st.markdown("## 👥 Party Representation")

        st.caption(
            "Binary outcome: whether a party represents "
            "the respondent's political views — Yes or No."
        )

        c1, c2, c3 = st.columns(3)

        c1.metric("Model 1", "2.9%")
        c2.metric("Model 2", "3.4%")
        c3.metric("Model 3", "4.6%", "+1.2 pp vs Model 2")

        st.markdown("""
### What does this mean?

Higher Feeling Left Behind is associated with **lower odds**
of saying that a party represents the respondent's views.

### LBI ↑ → odds of Party Representation ↓
""")

    st.warning("""
Party Representation uses **logistic regression and McFadden's
Pseudo R²**.

Its percentages should not be directly compared numerically with
the OLS R² values for Trust and Satisfaction.
""")

    st.divider()


    # ========================================================
    # FINAL MAP
    # ========================================================

    st.header("The project in one map")

    st.markdown("""
### What are we trying to explain?

🏛️ Trust  
🗳️ Democratic Satisfaction  
👥 Party Representation

# ↓

### Start with traditional information

Income · Education · Age · Region · Migration · Political Interest

# ↓

### Add perceived social position

Subjective Social Class

# ↓

### Add subjective social experience

Feeling Left Behind

# ↓

### Does explanatory power improve?

**Yes — especially for Institutional Trust and Democratic Satisfaction.**
""")

    st.warning("""
These are statistical associations, not causal effects.
""")


# ============================================================
# NAVIGATION
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