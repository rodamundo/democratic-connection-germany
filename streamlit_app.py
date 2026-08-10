import streamlit as st

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
        "How perceptions of social neglect relate to institutional trust, "
        "democratic satisfaction and party representation"
    )

    st.markdown("""
### Does feeling overlooked or left behind tell us something about people's
### relationship with democracy that income, education and social class do not?
""")

    st.divider()

    # ========================================================
    # MAIN FINDING
    # ========================================================

    st.header("What did we find?")

    st.success("""
### Feeling Left Behind is strongly connected to trust and democratic satisfaction.

Even after accounting for income, education, age, East/West Germany,
migration background, political interest and perceived social class,
Feeling Left Behind remains strongly associated with:

- **lower Institutional Trust**
- **lower Democratic Satisfaction**

Its relationship with **Party Representation is much weaker**.
""")

    st.markdown("""
The central message is that people's **subjective experience of being
overlooked or left behind contains information that socioeconomic
characteristics alone do not fully capture**.
""")

    st.divider()

    # ========================================================
    # MAIN RESULTS
    # ========================================================

    st.header("The main result at a glance")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🏛️ Institutional Trust")
            st.metric(
                "Variation explained",
                "27.6%",
                delta="+16.9 pp"
            )
            st.caption(
                "Before adding Feeling Left Behind: 10.7%. OLS R²."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 🗳️ Democratic Satisfaction")
            st.metric(
                "Variation explained",
                "22.2%",
                delta="+12.6 pp"
            )
            st.caption(
                "Before adding Feeling Left Behind: 9.6%. OLS R²."
            )

    with col3:
        with st.container(border=True):
            st.markdown("### 👥 Party Representation")
            st.metric(
                "Pseudo R² (McFadden)",
                "4.6%",
                delta="+1.2 pp"
            )
            st.caption(
                "Before adding Feeling Left Behind: 3.4%. "
                "Logistic regression (binary outcome) — not directly "
                "comparable in scale to the OLS R² above."
            )

    st.info("""
**These percentages are not levels of trust or satisfaction.**

They show how much of the **differences between respondents** can be
statistically explained by the variables included in each model.

**Note:** Party Representation is a binary outcome (Yes/No), so it was
modeled with logistic regression instead of OLS. Its Pseudo R² is a
different statistic and should not be compared numerically to the R²
of the other two outcomes — only the relative pattern (the gain from
adding Feeling Left Behind) is meaningful across all three.
""")

    st.divider()

    # ========================================================
    # LEFT BEHIND INTRODUCTION
    # ========================================================

    st.header("What does 'Feeling Left Behind' mean?")

    st.markdown("""
It does **not simply mean having a low income**.

The concept captures whether people feel that **people like them**
receive enough attention, recognition, services and space to express
themselves.
""")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown("### 💶 Economic attention")
            st.write(
                "Are the economic concerns of people like me being considered?"
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

    st.info("""
👉 Open **Feeling Left Behind** in the navigation menu to see the
four exact survey questions and how the index was constructed.
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

    st.divider()

    st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The analysis identifies statistical associations and should not be
interpreted as evidence of cause and effect.
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