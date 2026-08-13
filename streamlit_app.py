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
# HELPER: PUZZLE VISUAL
# ============================================================

def puzzle_visual(explained, label, value):

    explained_round = round(explained)
    unexplained_round = 100 - explained_round

    with st.container(border=True):

        st.markdown(f"### {label}")

        st.progress(explained / 100)

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "🧩 Accounted for by the model",
                f"≈ {explained_round} / 100"
            )

        with c2:
            st.metric(
                "Not accounted for by the model",
                f"≈ {unexplained_round} / 100"
            )

        st.caption(f"Statistical value: {value}")


# ============================================================
# HOME
# ============================================================

def home():

    st.title("🏛️ Feeling Left Behind and Democracy in Germany")

    st.subheader(
        "What helps us understand why people relate differently to democracy?"
    )

    st.markdown("""
This project asks whether people's **economic and social position**
is enough to understand democratic disconnection, or whether another
dimension also matters:

### **How people experience their place in society.**
""")

    st.divider()


    # ========================================================
    # 1. OUTCOMES
    # ========================================================

    st.header("1. What are we trying to understand?")

    st.markdown("""
People do not all relate to democracy in the same way.

This project examines **three different outcomes**.
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

The ratings are averaged into one trust score for each person.
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Respondents answered:

**1 = Very satisfied**

to

**4 = Not at all satisfied**

Higher values mean greater dissatisfaction.
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
### There is an important difference

For **Institutional Trust** and **Democratic Satisfaction**, people are
not divided into “trust” / “no trust” groups.

They have different scores.

The question is:

> **Why do some people have higher scores and others lower scores?**
""")

    st.divider()


    # ========================================================
    # 2. MODELS
    # ========================================================

    st.header("2. What information might help us understand those differences?")

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

    st.markdown("""
The logic is simple:

> **If adding new information makes the model much better at understanding
> why people's scores differ, that information is adding something useful.**
""")

    st.divider()


    # ========================================================
    # 3. LEFT BEHIND
    # ========================================================

    st.header("3. What is Feeling Left Behind?")

    st.markdown("""
The GLES contains four questions about whether respondents feel that
**people like them** are sufficiently considered by society.
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
The four answers are averaged into one score for each person:
""")

    c1, c2, c3 = st.columns([1, 1.3, 1])

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
There is **no cut-off** between “left behind” and “not left behind”.

The index measures **degrees** of Feeling Left Behind.
""")

    st.divider()


    # ========================================================
    # 4. PUZZLE
    # ========================================================

    st.header("4. What do the percentages actually mean?")

    st.markdown("""
Let's use **Institutional Trust** as an example.

People in the survey have different trust scores.

Some score low. Others score high.

The question is:

> ### Why are people's trust scores different?

To make the statistical result easier to understand, imagine all those
differences as a **100-piece puzzle**.
""")

    st.markdown("""
## 🧩 100 pieces = all the observed differences in trust scores

The model tries to account for as much of that puzzle as possible
using the information we give it.
""")

    puzzle_visual(
        8.8,
        "Model 1 — Traditional Factors",
        "R² = 8.8%"
    )

    st.markdown("**Traditional factors help account for roughly 9 of 100 pieces.**")

    puzzle_visual(
        10.7,
        "Model 2 — + Subjective Social Class",
        "R² = 10.7%"
    )

    st.markdown("**Adding Social Class moves this to roughly 11 of 100 pieces.**")

    puzzle_visual(
        27.6,
        "Model 3 — + Feeling Left Behind",
        "R² = 27.6%"
    )

    st.success("""
### This is the important jump

After Feeling Left Behind is added, the complete model can account for
roughly:

# 🧩 28 of every 100 pieces

of the observed differences in Institutional Trust scores.

About **72 of 100 pieces remain unaccounted for by this model.**
""")

    st.caption("""
The puzzle is a teaching analogy.

Statistically, R² measures the share of observed variation in the outcome
that the model can account for.

The 100 pieces do not represent 100 separate causes.
""")

    st.divider()


    # ========================================================
    # 5. WHAT 27.6% MEANS
    # ========================================================

    st.header("5. So what does 27.6% actually mean?")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### ❌ It does NOT mean")

            st.markdown("""
**27.6% of people trust institutions**

or

**trust increased by 27.6%**

or

**Feeling Left Behind alone explains 27.6%**
""")

    with c2:
        with st.container(border=True):

            st.markdown("### ✅ It DOES mean")

            st.markdown("""
The **complete Model 3** can account for:

# 27.6%

of the observed differences in Institutional Trust scores
between respondents.
""")

    st.divider()


    # ========================================================
    # 6. RESULTS
    # ========================================================

    st.header("6. Does the same pattern appear elsewhere?")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Traditional Factors  
**8.8%**

↓

+ Social Class  
**10.7%**

↓

+ Feeling Left Behind  
# **27.6%**
""")

            st.metric(
                "Gain after adding Feeling Left Behind",
                "+16.9 pp"
            )

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Traditional Factors  
**8.5%**

↓

+ Social Class  
**9.6%**

↓

+ Feeling Left Behind  
# **22.2%**
""")

            st.metric(
                "Gain after adding Feeling Left Behind",
                "+12.6 pp"
            )

    st.success("""
### The pattern is similar

Adding Subjective Social Class changes the models relatively little.

Adding **Feeling Left Behind** adds substantially more information.
""")

    st.divider()


    # ========================================================
    # 7. PARTY REPRESENTATION
    # ========================================================

    st.header("7. Party Representation is different")

    st.markdown("""
Party Representation is different because respondents answer:

# **Yes / No**

So this outcome uses **logistic regression** rather than the same
type of regression used above.
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
These are **McFadden Pseudo R² values**.

They do not have the same interpretation as the R² values for
Institutional Trust and Democratic Satisfaction.

So we do **not** use the 100-piece puzzle literally here.

The important result is that adding Feeling Left Behind improves
this model much less.
""")

    st.divider()


    # ========================================================
    # 8. CONCLUSION
    # ========================================================

    st.header("8. What does this tell us?")

    st.success("""
### Socioeconomic position does not tell the whole story.

Income, education, age, region and social class provide useful information.

But for **Institutional Trust** and **Democratic Satisfaction**, knowing
how left behind people feel adds substantially more information.
""")

    st.markdown("""
> ## What people have matters.
>
> ## But how people feel seen, recognized, served and heard may matter too.
""")

    st.warning("""
The analysis identifies **associations, not causation**.

It cannot establish which direction the relationship runs.
""")

    st.divider()


    # ========================================================
    # ABOUT
    # ========================================================

    st.header("About the analysis")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Survey respondents",
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

    c4.metric(
        "Regression models",
        "9"
    )

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