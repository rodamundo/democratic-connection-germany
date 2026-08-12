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
    # 1. OUTCOMES
    # ========================================================

    st.header("1. What are we trying to understand?")

    st.markdown("""
The project looks at **three different democratic outcomes**.

Importantly, they are not all measured in the same way.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Respondents rated **eight institutions**.

**1 = Do not trust at all**

**11 = Trust completely**

The eight ratings are averaged into one trust score for each person.
""")

            st.caption(
                "There is no cut-off between 'trusting' and 'not trusting'."
            )

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

            st.caption(
                "Higher values mean greater dissatisfaction."
            )

    with c3:
        with st.container(border=True):

            st.markdown("### 👥 Party Representation")

            st.markdown("""
Respondents were asked whether any political party represents
their political views well.

**Yes / No**
""")

            st.caption(
                "This is the only binary outcome."
            )

    st.info("""
### What are the models trying to explain?

For **Institutional Trust** and **Democratic Satisfaction**, the analysis
does not divide people into two groups.

Instead, it asks:

> **Why do respondents have different scores?**

For **Party Representation**, the outcome really is Yes/No.
""")

    st.divider()


    # ========================================================
    # 2. MODELS
    # ========================================================

    st.header("2. How is the question tested?")

    st.markdown("""
The analysis builds three models.

Each model adds another layer of information about the same respondents.
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

### +

🪜 **Subjective Social Class**

Where respondents believe they belong in the social hierarchy.
""")

    with c3:
        with st.container(border=True):

            st.markdown("### Model 3")
            st.markdown("**+ Feeling Left Behind**")

            st.markdown("""
Everything in Model 2

### +

🧩 **Left Behind Index**
""")

    st.info("""
The central question is:

> **Does knowing how left behind someone feels add useful information
> beyond income, education, age, region, migration background,
> political interest and social class?**
""")

    st.divider()


    # ========================================================
    # 3. LEFT BEHIND
    # ========================================================

    st.header("3. What is Feeling Left Behind?")

    st.markdown("""
Even if two people have similar income and education, they may experience
their place in society very differently.

The GLES contains four questions about whether **people like the respondent**
feel sufficiently considered by society.
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
The four answers are converted into one score for each respondent.
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

## 🧩 Left Behind Index
""")

    with c3:
        st.metric(
            "Higher Feeling Left Behind",
            "5"
        )

    st.info("""
There is **no threshold** separating people into
“left behind” and “not left behind”.

Each respondent simply receives a score between approximately **1 and 5**.

The analysis then asks whether democratic attitudes tend to change
as this score changes.
""")

    st.divider()


    # ========================================================
    # 4. HOW TO READ R²
    # ========================================================

    st.header("4. Before the results: what does '27.6%' actually mean?")

    st.markdown("""
This is easiest to understand with **Institutional Trust**.

Each of the 5,039 respondents has a different trust score.

Imagine that:

### **100% = all the observed differences in trust scores between respondents**

The models try to understand why those scores differ.
""")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### ❌ 27.6% does NOT mean")

            st.markdown("""
- 27.6% of people trust institutions
- trust increased by 27.6%
- Feeling Left Behind alone explains 27.6%
""")

    with c2:
        with st.container(border=True):

            st.markdown("### ✅ 27.6% means")

            st.markdown("""
The **complete Model 3** can statistically account for:

### **27.6% of the observed differences in Institutional Trust scores between respondents.**
""")

    st.markdown("""
For Institutional Trust:

**Model 1:** 8.8% of the observed differences accounted for

**Model 2:** 10.7%

**Model 3:** 27.6%

So adding Feeling Left Behind increases the model's explanatory power
by **16.9 percentage points compared with Model 2**.
""")

    st.divider()


    # ========================================================
    # 5. RESULTS
    # ========================================================

    st.header("5. What happens when Feeling Left Behind is added?")

    st.markdown("""
For the two outcomes measured as scores, the pattern is clear:
""")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
**Traditional Factors:** 8.8%

**+ Social Class:** 10.7%

**+ Feeling Left Behind:** **27.6%**
""")

            st.metric(
                "Gain after adding Feeling Left Behind",
                "+16.9 pp"
            )

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
**Traditional Factors:** 8.5%

**+ Social Class:** 9.6%

**+ Feeling Left Behind:** **22.2%**
""")

            st.metric(
                "Gain after adding Feeling Left Behind",
                "+12.6 pp"
            )

    st.success("""
### Main pattern

Adding Subjective Social Class changes the models only slightly.

Adding **Feeling Left Behind** produces a much larger improvement,
especially for Institutional Trust and Democratic Satisfaction.
""")

    st.divider()


    # ========================================================
    # PARTY REPRESENTATION SEPARATE
    # ========================================================

    st.header("6. Party Representation is different")

    st.markdown("""
Party Representation is a **Yes/No outcome**.

Because of that, it requires **logistic regression** and uses
**McFadden Pseudo R²**, not the same R² used above.
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
        "4.6%",
        delta="+1.2 pp"
    )

    st.warning("""
These percentages should **not be numerically compared** with the
27.6% and 22.2% above.

The useful conclusion is simply that Feeling Left Behind improves
the Party Representation model much less.
""")

    st.divider()


    # ========================================================
    # 7. CONCLUSION
    # ========================================================

    st.header("7. What does this tell us?")

    st.success("""
### Socioeconomic position does not tell the whole story.

Income, education, age, region and social class help explain some
differences in democratic attitudes.

But for **Institutional Trust** and **Democratic Satisfaction**,
knowing how left behind people feel adds substantial information.

The much weaker pattern for **Party Representation** suggests that
democratic disconnection has different dimensions.
""")

    st.markdown("""
> ## What people have matters.
>
> ## But how people feel seen, recognized, served and heard may matter too.
""")

    st.warning("""
The analysis identifies **associations, not causation**.

It cannot establish whether Feeling Left Behind causes lower trust
or dissatisfaction, or whether people who already distrust institutions
are more likely to report feeling left behind.
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