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
        "What helps us understand why people relate differently to democracy?"
    )

    st.markdown("""
This project explores whether people's **social and economic position**
is enough to understand democratic disconnection in Germany, or whether
another dimension also matters:

### **How people experience their place in society.**
""")

    st.divider()


    # ========================================================
    # 1. WHAT ARE WE TRYING TO UNDERSTAND?
    # ========================================================

    st.header("1. What are we trying to understand?")

    st.markdown("""
People can relate to democracy in different ways.

This project looks at **three different outcomes**:
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
**Do people trust important institutions?**

Respondents rated eight institutions from:

**1 = Do not trust at all**

to

**11 = Trust completely**
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
**Are people satisfied with how democracy works in Germany?**

Responses range from:

**1 = Very satisfied**

to

**4 = Not at all satisfied**
""")

    with c3:
        with st.container(border=True):

            st.markdown("### 👥 Party Representation")

            st.markdown("""
**Does any political party represent the person's views well?**

Respondents answer:

**Yes / No**
""")

    st.divider()


    # ========================================================
    # 2. HOW IS THE QUESTION TESTED? (THREE MODELS OVERVIEW)
    # ========================================================

    st.header("2. How is the question tested?")

    st.markdown("""
To find out what helps explain these three outcomes, the analysis
builds understanding in **three stages**, adding one layer of
information at a time.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### Model 1")
            st.markdown("**Traditional Factors**")

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

            st.markdown("### Model 2")
            st.markdown("**+ Social Class**")

            st.markdown("""
Everything in Model 1

**+**

🪜 Subjective Social Class

*Where the respondent believes they belong in the social hierarchy.*
""")

    with c3:
        with st.container(border=True):

            st.markdown("### Model 3")
            st.markdown("**+ Feeling Left Behind**")

            st.markdown("""
Everything in Model 2

**+**

🧩 Left Behind Index

*A new measure introduced in this project — explained in detail
below.*
""")

    st.info("""
Each stage adds one layer of information. The central test is simple:

> **Does the last layer — Feeling Left Behind — help us understand
> democratic attitudes beyond everything already captured by income,
> education, age, region, migration background, political interest
> and perceived social class?**

To answer that, we first need to unpack what Feeling Left Behind
actually measures.
""")

    st.divider()


    # ========================================================
    # 3. WHAT IS FEELING LEFT BEHIND?
    # ========================================================

    st.header("3. What is Feeling Left Behind?")

    st.markdown("""
Even after knowing someone's income, education and perceived social
class, we may still know very little about **how that person feels
society treats people like them**. That is what this index tries to
capture.
""")

    st.success("""
# 🧩 Feeling Left Behind

Feeling Left Behind captures whether people feel that **people like them**
are overlooked, insufficiently recognized, underserved or unable to
freely express their views.
""")

    st.markdown("""
The GLES survey contains four questions covering:
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
                "Is the contribution of people like me recognized?"
            )

    with c3:
        with st.container(border=True):

            st.markdown("### 🏥 Services")

            st.write(
                "Do people like me receive adequate access to essential services?"
            )

    with c4:
        with st.container(border=True):

            st.markdown("### 🗣️ Voice")

            st.write(
                "Do people like me feel free to express their opinions?"
            )

    st.markdown("""
The four answers are combined into a single score for each respondent:
""")

    c1, c2, c3 = st.columns([1, 1.4, 1])

    with c1:
        st.metric(
            "Lower Feeling Left Behind",
            "1"
        )

    with c2:
        st.markdown("""
### 4 answers

### ↓

### Average

### ↓

## Left Behind Index
""")

    with c3:
        st.metric(
            "Higher Feeling Left Behind",
            "5"
        )

    st.info("""
There is **no cut-off** separating people into “left behind” and
“not left behind”.

The index measures **degrees of Feeling Left Behind**, from lower to higher.
""")

    st.markdown("""
So the central test from Model 3 becomes:

> ### Does knowing how left behind someone feels help us understand
> ### their democratic attitudes beyond everything already included
> ### in Models 1 and 2?
""")

    st.divider()


    # ========================================================
    # 4. MAIN RESULTS
    # ========================================================

    st.header("4. What happens when Feeling Left Behind is added?")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.metric(
                "Model fit",
                "27.6%",
                delta="+16.9 pp"
            )

            st.markdown("""
**Before:** 10.7%

**After adding Feeling Left Behind:** 27.6%
""")

            st.caption("OLS R²")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.metric(
                "Model fit",
                "22.2%",
                delta="+12.6 pp"
            )

            st.markdown("""
**Before:** 9.6%

**After adding Feeling Left Behind:** 22.2%
""")

            st.caption("OLS R²")

    with c3:
        with st.container(border=True):

            st.markdown("### 👥 Party Representation")

            st.metric(
                "Model fit",
                "4.6%",
                delta="+1.2 pp"
            )

            st.markdown("""
**Before:** 3.4%

**After adding Feeling Left Behind:** 4.6%
""")

            st.caption(
                "McFadden Pseudo R² · Logistic regression"
            )

    st.info("""
### How should these percentages be read?

They are **not percentages of people who trust institutions or are
satisfied with democracy**.

For example, the **27.6%** means that the final model can account for
27.6% of the differences in Institutional Trust between respondents.

Party Representation uses a different statistic, Pseudo R², because
the outcome is Yes/No. Its numerical value should not be directly
compared with the two OLS R² values.
""")

    st.divider()


    # ========================================================
    # 5. MAIN MESSAGE
    # ========================================================

    st.header("5. What does this tell us?")

    st.success("""
### Socioeconomic position does not tell the whole story.

Income, education, age, region and social class provide useful information.

But for **Institutional Trust** and **Democratic Satisfaction**, knowing
how left behind people feel adds substantially more information.

The pattern is much weaker for **Party Representation**, suggesting that
democratic disconnection has different dimensions.
""")

    st.markdown("""
In simple terms:

> ## What people have matters.
>
> ## But how people feel seen, recognized, served and heard may matter too.
""")

    st.warning("""
The analysis identifies **statistical associations**, not cause and effect.

It cannot establish whether Feeling Left Behind causes lower trust or
democratic dissatisfaction, or whether people who already distrust
institutions are more likely to report feeling left behind.
""")

    st.divider()


    # ========================================================
    # PROJECT
    # ========================================================

    st.header("About the analysis")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Survey respondents", "7,336")
    c2.metric("Analytical sample", "5,039")
    c3.metric("Democratic outcomes", "3")
    c4.metric("Regression models", "9")

    st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
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