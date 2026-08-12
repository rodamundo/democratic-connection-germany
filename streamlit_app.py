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

def puzzle_visual(explained, label, value, total=100):
    """
    Didactic visual:
    100 squares represent all observed variation.
    Filled squares approximate the share accounted for by the model.
    """

    filled = round(explained)
    empty = total - filled

    squares = (
        "<span style='color:#2E86DE;'>■</span>" * filled +
        "<span style='color:#D9D9D9;'>■</span>" * empty
    )

    st.markdown(
        f"""
        <div style="
            border:1px solid #dddddd;
            border-radius:12px;
            padding:18px;
            margin-bottom:12px;
        ">
            <div style="font-size:19px;font-weight:700;margin-bottom:6px;">
                {label}
            </div>

            <div style="
                font-size:20px;
                line-height:1.25;
                letter-spacing:2px;
                word-break:break-all;
                margin-bottom:10px;
            ">
                {squares}
            </div>

            <div style="font-size:18px;font-weight:700;">
                ≈ {round(explained)} of 100 pieces
            </div>

            <div style="font-size:14px;color:#777777;">
                Statistical value: {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
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
        st.metric("Lower Feeling Left Behind", "1")

    with c2:
        st.markdown("""
### 4 answers
### ↓
### Average
### ↓
## 🧩 Left Behind Index
""")

    with c3:
        st.metric("Higher Feeling Left Behind", "5")

    st.info("""
There is **no cut-off** between “left behind” and “not left behind”.

The index measures **degrees** of Feeling Left Behind.
""")

    st.divider()


    # ========================================================
    # 4. PUZZLE EXPLANATION
    # ========================================================

    st.header("4. What do the percentages actually mean?")

    st.markdown("""
This is the part that can be difficult to understand statistically,
so here is a visual analogy.

Imagine all the differences in **Institutional Trust scores**
between respondents as a **100-piece puzzle**.

### 🧩 100 pieces = all the observed differences in trust scores

The model tries to account for as many of those differences as possible
using the information we give it.
""")

    puzzle_visual(
        8.8,
        "Model 1 — Traditional Factors",
        "R² = 8.8%"
    )

    puzzle_visual(
        10.7,
        "Model 2 — + Subjective Social Class",
        "R² = 10.7%"
    )

    puzzle_visual(
        27.6,
        "Model 3 — + Feeling Left Behind",
        "R² = 27.6%"
    )

    st.success("""
### What changed?

Traditional factors account for roughly **9 of 100 pieces**.

Adding Subjective Social Class moves this to roughly **11 of 100**.

Adding Feeling Left Behind moves it to roughly **28 of 100**.

### Feeling Left Behind does not complete the puzzle.

But it adds substantially more information than Social Class alone.
""")

    st.caption("""
The puzzle is a teaching analogy.

Statistically, R² measures the share of observed variation in the outcome
that the model can account for. The pieces do not represent 100 separate causes.
""")

    st.divider()


    # ========================================================
    # 5. RESULTS
    # ========================================================

    st.header("5. Does the same pattern appear elsewhere?")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
Model 1: **8.8%**

Model 2: **10.7%**

Model 3: **27.6%**
""")

            st.metric(
                "Gain after Feeling Left Behind",
                "+16.9 pp"
            )

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
Model 1: **8.5%**

Model 2: **9.6%**

Model 3: **22.2%**
""")

            st.metric(
                "Gain after Feeling Left Behind",
                "+12.6 pp"
            )

    st.success("""
For both outcomes, adding Subjective Social Class changes relatively little.

Adding **Feeling Left Behind** changes the model much more.
""")

    st.divider()


    # ========================================================
    # PARTY
    # ========================================================

    st.header("6. Party Representation is different")

    st.markdown("""
Party Representation is **Yes / No**, so it uses logistic regression
rather than the same R² measure used above.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric("Traditional Factors", "3.4%")
    c2.metric("+ Social Class", "3.4%")
    c3.metric("+ Feeling Left Behind", "4.6%", delta="+1.2 pp")

    st.warning("""
These are **McFadden Pseudo R² values**.

Do not interpret them as “pieces of the puzzle explained” in exactly
the same way as the R² values above.

The important message is that the improvement is much smaller.
""")

    st.divider()


    # ========================================================
    # CONCLUSION
    # ========================================================

    st.header("7. What does this tell us?")

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