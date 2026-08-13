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
# HELPER
# ============================================================

def explanation_bar(value, title, description):

    with st.container(border=True):

        st.markdown(f"### {title}")

        st.progress(value / 100)

        c1, c2 = st.columns([1, 3])

        with c1:
            st.metric(
                "Share accounted for",
                f"{value:.1f}%"
            )

        with c2:
            st.markdown(description)


# ============================================================
# HOME
# ============================================================

def home():

    st.title("🏛️ Feeling Left Behind and Democracy in Germany")

    st.subheader(
        "Can how people feel treated by society tell us something "
        "that income and social class do not?"
    )

    st.markdown("""
This project uses **GLES 2025** data to investigate why people
relate differently to democracy in Germany.
""")

    st.divider()


    # ========================================================
    # 1. WHAT DO WE MEASURE?
    # ========================================================

    st.header("1. First: what are we trying to understand?")

    st.markdown("""
The project looks at **three different democratic outcomes**.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Respondents rated **eight institutions** from:

**1 = Do not trust at all**

to

**11 = Trust completely**

The eight ratings are averaged into one trust score.
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Respondents answered:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    with c3:
        with st.container(border=True):

            st.markdown("### 👥 Party Representation")

            st.markdown("""
Respondents were asked:

**Does any political party represent your views well?**

**Yes / No**
""")

    st.info("""
### Important

For **Institutional Trust** and **Democratic Satisfaction**,
we do not divide people into “yes” and “no” groups.

People simply have **different scores**.

The question is:

> **Why do some people have higher scores and others lower scores?**

Party Representation is different because it really is a Yes/No question.
""")

    st.divider()


    # ========================================================
    # 2. MODELS
    # ========================================================

    st.header("2. What might help explain these differences?")

    st.markdown("""
We build three models.

Each model knows a little more about the same respondents.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### Model 1")

            st.markdown("""
### Traditional information

💰 Income  
🎓 Education  
🎂 Age  
📍 East / West  
🌍 Migration background  
🗳️ Political interest
""")

    with c2:
        with st.container(border=True):

            st.markdown("### Model 2")

            st.markdown("""
### Model 1 +

🪜 **Subjective Social Class**

Where people believe they sit in the social hierarchy.
""")

    with c3:
        with st.container(border=True):

            st.markdown("### Model 3")

            st.markdown("""
### Model 2 +

🧩 **Feeling Left Behind**

How overlooked, unrecognized, underserved or unheard people feel.
""")

    st.markdown("""
So the experiment is simple:

> ### If Model 3 understands the differences between people much better
> ### than Model 2, Feeling Left Behind is adding useful information.
""")

    st.divider()


    # ========================================================
    # 3. LEFT BEHIND
    # ========================================================

    st.header("3. What exactly is Feeling Left Behind?")

    st.markdown("""
The GLES includes four questions about whether respondents feel that
**people like them** receive enough attention and consideration.
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
                "Is the work and contribution of people like me recognized?"
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
The four answers are combined into one score for each respondent.
""")

    c1, c2, c3 = st.columns([1, 1.5, 1])

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
# 🧩 Left Behind Index
""")

    with c3:
        st.metric(
            "Higher Feeling Left Behind",
            "5"
        )

    st.info("""
There is **no cut-off** between “left behind” and “not left behind”.

A respondent might have a score of **1.8, 2.6, 3.4, 4.2**, and so on.

The model uses the complete scale.
""")

    st.divider()


    # ========================================================
    # 4. EXPLAIN R2
    # ========================================================

    st.header("4. Now the important part: what do the percentages mean?")

    st.markdown("""
Let's use **Institutional Trust**.

Imagine three people:

**Person A → Trust score 3**

**Person B → Trust score 6**

**Person C → Trust score 9**

Their scores are different.

The statistical question is:

> # Why are these scores different?

Now imagine that **all the differences in trust scores across all
5,039 respondents = 100%**.

The models try to account for part of those differences.
""")

    st.markdown("## Institutional Trust")

    explanation_bar(
        8.8,
        "Model 1 — Traditional information",
        """
Using income, education, age, region, migration background and
political interest, the model can account for **8.8% of the observed
differences in trust scores between respondents**.
"""
    )

    explanation_bar(
        10.7,
        "Model 2 — + Subjective Social Class",
        """
After adding Subjective Social Class, the model can account for
**10.7% of the observed differences**.
"""
    )

    explanation_bar(
        27.6,
        "Model 3 — + Feeling Left Behind",
        """
After also adding Feeling Left Behind, the model can account for
**27.6% of the observed differences in trust scores**.
"""
    )

    st.success("""
### The result in one sentence

The model goes from accounting for **10.7%** of the differences
in Institutional Trust to **27.6%** after Feeling Left Behind is added.

That is an increase of **16.9 percentage points**.
""")

    st.warning("""
### 27.6% does NOT mean:

❌ 27.6% of people trust institutions  
❌ trust increased by 27.6%  
❌ Feeling Left Behind alone explains 27.6%

### It means:

✅ The **complete Model 3** accounts for 27.6% of the observed
differences in trust scores between respondents.
""")

    st.divider()


    # ========================================================
    # 5. SECOND OUTCOME
    # ========================================================

    st.header("5. The same pattern appears for Democratic Satisfaction")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Traditional factors  
**8.8%**

+ Social Class  
**10.7%**

+ Feeling Left Behind  
# **27.6%**
""")

            st.metric(
                "Gain after Feeling Left Behind",
                "+16.9 pp"
            )

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Traditional factors  
**8.5%**

+ Social Class  
**9.6%**

+ Feeling Left Behind  
# **22.2%**
""")

            st.metric(
                "Gain after Feeling Left Behind",
                "+12.6 pp"
            )

    st.success("""
### Main pattern

Adding Subjective Social Class changes relatively little.

Adding **Feeling Left Behind** changes much more.

So Feeling Left Behind contains information about Trust and
Democratic Satisfaction that the traditional variables do not fully capture.
""")

    st.divider()


    # ========================================================
    # 6. PARTY SEPARATE
    # ========================================================

    st.header("6. Party Representation is different")

    st.markdown("""
Party Representation is a **Yes / No** question.

That means it needs a different statistical model:
**logistic regression**.

So we should not interpret its numbers in exactly the same way
as the percentages above.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Traditional Factors",
        "3.4%"
    )

    c2.metric(
        "+ Social Class",
        "3.4%"
    )

    c3.metric(
        "+ Feeling Left Behind",
        "4.6%"
    )

    st.info("""
The useful message here is simple:

**Feeling Left Behind adds much less to Party Representation than
it adds to Institutional Trust or Democratic Satisfaction.**
""")

    st.divider()


    # ========================================================
    # 7. CONCLUSION
    # ========================================================

    st.header("7. What does the project tell us?")

    st.success("""
### Income and social class do not tell the whole story.

For Institutional Trust and Democratic Satisfaction,
knowing **how left behind people feel** adds substantial information
beyond their socioeconomic characteristics.

For Party Representation, the relationship is much weaker.
""")

    st.markdown("""
> # What people have matters.
>
> # How people feel seen, recognized, served and heard may matter too.
""")

    st.warning("""
The analysis shows **statistical associations, not causation**.

It cannot establish whether Feeling Left Behind causes lower trust
or dissatisfaction.
""")

    st.divider()


    # ========================================================
    # PROJECT
    # ========================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Survey respondents", "7,336")
    c2.metric("Analytical sample", "5,039")
    c3.metric("Democratic outcomes", "3")
    c4.metric("Regression models", "9")

    st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
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