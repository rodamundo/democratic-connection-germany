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

    # ========================================================
    # INTRO
    # ========================================================

    st.title("🏛️ Feeling Left Behind and Democracy in Germany")

    st.subheader(
        "Does feeling left behind help us understand democratic "
        "disconnection beyond income and social class?"
    )

    st.markdown("""
This project uses **GLES 2025** survey data to investigate whether
people's feeling of being overlooked, unrecognized, underserved or
unheard is associated with their relationship with democracy.
""")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Survey respondents", "7,336")
    c2.metric("Analytical sample", "5,039")
    c3.metric("Democratic outcomes", "3")
    c4.metric("Regression models", "9")

    st.divider()


    # ========================================================
    # THE WHOLE PROJECT IN ONE VIEW
    # ========================================================

    st.header("The whole project, step by step")

    st.markdown("""
Before looking at regression models or R², here is exactly what
the analysis does.
""")

    # ========================================================
    # STEP 1
    # ========================================================

    st.markdown("## ① Ask four questions")

    st.markdown("""
Each respondent answers four questions about how society treats
**people like them**.
""")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown("### 💶 Economic attention")
            st.markdown("""
**Does society pay enough attention to the economic situation
of people like me?**
""")

    with c2:
        with st.container(border=True):
            st.markdown("### 👏 Recognition")
            st.markdown("""
**Do people like me receive enough recognition for the work
they do?**
""")

    with c3:
        with st.container(border=True):
            st.markdown("### 🏥 Services")
            st.markdown("""
**Does society ensure that people like me have adequate access
to basic services?**
""")

    with c4:
        with st.container(border=True):
            st.markdown("### 🗣️ Voice")
            st.markdown("""
**Do people like me feel able to express their opinions freely?**
""")

    st.markdown(
        "<h2 style='text-align:center;'>↓</h2>",
        unsafe_allow_html=True
    )


    # ========================================================
    # STEP 2
    # ========================================================

    st.markdown("## ② Turn the four answers into one score")

    st.markdown("""
For each respondent, the four answers are combined by taking
their **average**.

This creates that person's **Feeling Left Behind Index**.
""")

    with st.container(border=True):

        st.markdown(
            """
            <div style="text-align:center">
                <h3>4 survey answers</h3>
                <h2>↓</h2>
                <h3>Average</h3>
                <h2>↓</h2>
                <h2>Feeling Left Behind Index</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns([1, 2, 1])

        with c1:
            st.metric(
                "Lower Feeling Left Behind",
                "1"
            )

        with c2:
            st.markdown("""
<div style="text-align:center; font-size:24px; padding-top:18px;">
1 ───────── 2 ───────── 3 ───────── 4 ───────── 5
</div>
""", unsafe_allow_html=True)

        with c3:
            st.metric(
                "Higher Feeling Left Behind",
                "5"
            )

    st.info("""
### There are no two groups.

We do **not** classify respondents as either
“left behind” or “not left behind”.

Every respondent receives a score on a continuous scale from
**lower to higher Feeling Left Behind**.
""")

    st.markdown(
        "<h2 style='text-align:center;'>↓</h2>",
        unsafe_allow_html=True
    )


    # ========================================================
    # STEP 3
    # ========================================================

    st.markdown("## ③ Look at the same person's democratic attitudes")

    st.markdown("""
Each respondent also has information about three democratic outcomes.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("### 🏛️ Institutional Trust")
            st.markdown("""
Trust in **8 institutions**.

The ratings are averaged into one trust score.

**1 = lowest trust**

**11 = highest trust**
""")

    with c2:
        with st.container(border=True):
            st.markdown("### 🗳️ Democratic Satisfaction")
            st.markdown("""
How satisfied is the respondent with democracy?

**1 = Very satisfied**

to

**4 = Not at all satisfied**
""")

    with c3:
        with st.container(border=True):
            st.markdown("### 👥 Party Representation")
            st.markdown("""
Does the respondent think that any political party represents
their views well?

**Yes / No**
""")

    st.markdown(
        "<h2 style='text-align:center;'>↓</h2>",
        unsafe_allow_html=True
    )


    # ========================================================
    # STEP 4
    # ========================================================

    st.markdown("## ④ Ask a very simple question")

    st.markdown("""
Now each respondent has a **Feeling Left Behind score** and
democratic outcome information.

So the central question becomes:
""")

    st.success("""
# As Feeling Left Behind increases,
# what tends to happen to democratic attitudes?
""")

    st.markdown("""
The analysis finds the following pattern:
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("""
### 🧩 Feeling Left Behind

# ↑

### 🏛️ Institutional Trust

# ↓

**More Feeling Left Behind is associated with lower trust.**
""")

    with c2:
        with st.container(border=True):
            st.markdown("""
### 🧩 Feeling Left Behind

# ↑

### 🗳️ Democratic Dissatisfaction

# ↑

**More Feeling Left Behind is associated with greater dissatisfaction.**
""")

    with c3:
        with st.container(border=True):
            st.markdown("""
### 🧩 Feeling Left Behind

# ↑

### 👥 Party Representation

# ↓

**More Feeling Left Behind is associated with lower odds of feeling
represented by a party.**
""")

    st.warning("""
### Association ≠ causation

These results show statistical relationships.

They do **not** prove that Feeling Left Behind causes lower trust,
greater dissatisfaction or lower representation.
""")

    st.markdown(
        "<h2 style='text-align:center;'>↓</h2>",
        unsafe_allow_html=True
    )


    # ========================================================
    # STEP 5
    # ========================================================

    st.markdown("## ⑤ But does Feeling Left Behind add anything new?")

    st.markdown("""
This is the next question.

Maybe people who feel left behind simply have lower incomes,
less education, or belong to different social groups.

So we compare **three models**.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### Model 1")

            st.markdown("""
## Traditional factors

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
## Model 1 +

🪜 **Subjective Social Class**

Where respondents believe they belong in the social hierarchy.
""")

    with c3:
        with st.container(border=True):

            st.markdown("### Model 3")

            st.markdown("""
## Model 2 +

🧩 **Feeling Left Behind Index**

How overlooked, unrecognized, underserved or unheard respondents feel.
""")

    st.markdown("""
The comparison asks:

> ### Does adding Feeling Left Behind help us understand why people's
> ### democratic attitudes differ, beyond what we already know about
> ### their socioeconomic characteristics?
""")

    st.markdown(
        "<h2 style='text-align:center;'>↓</h2>",
        unsafe_allow_html=True
    )


    # ========================================================
    # STEP 6
    # ========================================================

    st.markdown("## ⑥ This is where R² enters")

    st.markdown("""
For **Institutional Trust** and **Democratic Satisfaction**,
people have different scores.

R² answers:
""")

    st.info("""
# How much of the differences between people's scores
# can the variables in the model explain?
""")

    st.markdown("""
A **higher R²** means that the variables included in the model
help us understand more of the differences between respondents.

It does **not** tell us whether trust goes up or down.

The **coefficients** tell us the direction of each relationship.
""")

    st.markdown("### Example: Institutional Trust")

    with st.container(border=True):

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("### Model 1")
            st.metric(
                "Differences explained",
                "8.8%"
            )
            st.caption(
                "Traditional socioeconomic and demographic factors"
            )

        with c2:
            st.markdown("### Model 2")
            st.metric(
                "Differences explained",
                "10.7%",
                "+1.9 pp"
            )
            st.caption(
                "+ Subjective Social Class"
            )

        with c3:
            st.markdown("### Model 3")
            st.metric(
                "Differences explained",
                "27.6%",
                "+16.9 pp"
            )
            st.caption(
                "+ Feeling Left Behind"
            )

    st.success("""
### What does this tell us?

Before Feeling Left Behind is included, the model explains
**10.7% of the differences in Institutional Trust scores**.

After Feeling Left Behind is included, it explains **27.6%**.

So Feeling Left Behind adds substantial information that was not
captured by the previous variables.
""")

    st.warning("""
### 27.6% does NOT mean:

❌ 27.6% of people trust institutions

❌ Feeling Left Behind increases trust by 27.6%

❌ Feeling Left Behind alone explains 27.6%

### It means:

✅ All variables in Model 3 **together** explain 27.6% of the
variation in Institutional Trust scores.
""")

    st.divider()


    # ========================================================
    # RESULTS AT A GLANCE
    # ========================================================

    st.header("Results at a glance")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
**Model 1**

8.8%

↓

**+ Social Class**

10.7%

↓

**+ Feeling Left Behind**

# 27.6%
""")

            st.metric(
                "Gain after adding Feeling Left Behind",
                "+16.9 percentage points"
            )

            st.markdown("""
**Direction:**

🧩 Feeling Left Behind ↑

**→ Institutional Trust ↓**
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
**Model 1**

8.5%

↓

**+ Social Class**

9.6%

↓

**+ Feeling Left Behind**

# 22.2%
""")

            st.metric(
                "Gain after adding Feeling Left Behind",
                "+12.6 percentage points"
            )

            st.markdown("""
**Direction:**

🧩 Feeling Left Behind ↑

**→ Democratic Dissatisfaction ↑**
""")

    st.markdown("### 👥 Party Representation")

    with st.container(border=True):

        c1, c2 = st.columns([1, 2])

        with c1:

            st.metric(
                "Pseudo R² before Feeling Left Behind",
                "3.4%"
            )

            st.metric(
                "Pseudo R² after Feeling Left Behind",
                "4.6%"
            )

        with c2:

            st.markdown("""
### 🧩 Feeling Left Behind ↑

# ↓

### Odds of feeling represented by a party

Each one-point increase in the Left Behind Index is associated
with approximately **29% lower odds** of saying that a political
party represents the respondent's views well.
""")

            st.caption("""
Party Representation uses logistic regression.
Its McFadden Pseudo R² should not be interpreted in exactly the
same way as the OLS R² above.
""")

    st.divider()


    # ========================================================
    # FINAL STORY
    # ========================================================

    st.header("The story in one sentence")

    st.success("""
# The more left behind people feel, the more democratically
# disconnected they tend to be — and this relationship contains
# information that income and social class alone do not capture.
""")

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