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
This project asks a simple question:

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

**lower Institutional Trust** and **lower Democratic Satisfaction**.

Its relationship with **Party Representation is much weaker**.
""")

    st.divider()

    # ========================================================
    # KEY VISUAL NUMBERS
    # ========================================================

    st.header("The main result at a glance")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🏛️ Institutional Trust")
            st.metric(
                "Variation explained",
                "27.6%",
                delta="+16.9 pp after adding Left Behind"
            )
            st.caption("Before Left Behind: 10.7%")

    with col2:
        with st.container(border=True):
            st.markdown("### 🗳️ Democratic Satisfaction")
            st.metric(
                "Variation explained",
                "22.2%",
                delta="+12.6 pp after adding Left Behind"
            )
            st.caption("Before Left Behind: 9.6%")

    with col3:
        with st.container(border=True):
            st.markdown("### 👥 Party Representation")
            st.metric(
                "Variation explained",
                "5.3%",
                delta="+1.4 pp after adding Left Behind"
            )
            st.caption("Before Left Behind: 3.9%")

    st.info("""
**How to read this:** the larger the increase, the more additional
information Feeling Left Behind contributes to explaining differences
between respondents.
""")

    st.divider()

    # ========================================================
    # LEFT BEHIND CONCEPT
    # ========================================================

    st.header("What does 'Feeling Left Behind' mean?")

    st.markdown("""
It does **not simply mean having a low income**.

The index captures four different perceptions:
""")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown("### 💶 Economic attention")
            st.write(
                "Do people like me receive enough attention to their "
                "economic situation?"
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
                "Do people like me receive adequate access to basic "
                "infrastructure and services?"
            )

    with c4:
        with st.container(border=True):
            st.markdown("### 🗣️ Voice")
            st.write(
                "Do people like me feel free to express their opinions publicly?"
            )

    st.markdown("""
### Left Behind Index

**1 — Lower feeling of being left behind**  
`● ───── ● ───── ● ───── ● ───── ●`  
**5 — Higher feeling of being left behind**
""")

    st.info("""
For the exact survey questions and how the index was calculated,
open **Results → Left Behind Index**.
""")

    st.divider()

    # ========================================================
    # PROJECT NUMBERS
    # ========================================================

    st.header("About the analysis")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Survey respondents", "7,336")
    c2.metric("Analytical sample", "5,039")
    c3.metric("Democratic outcomes", "3")
    c4.metric("Regression models", "9")

    st.divider()

    # ========================================================
    # NAVIGATION
    # ========================================================

    st.header("Explore the project")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("### 📚 Research")
            st.write(
                "The research question, data, variables and logic of the analysis."
            )

        with st.container(border=True):
            st.markdown("### 📊 Results")
            st.write(
                "The main findings and the complete explanation of "
                "Feeling Left Behind."
            )

    with c2:
        with st.container(border=True):
            st.markdown("### 🔬 Methodology")
            st.write(
                "How the indices and regression models were tested and validated."
            )

        with st.container(border=True):
            st.markdown("### 💡 Policy Implications")
            st.write(
                "What the findings may mean for democratic institutions "
                "and public policy."
            )

    with c3:
        with st.container(border=True):
            st.markdown("### 👤 About")
            st.write(
                "Project background, analytical approach and author."
            )

    st.divider()

    st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Results describe statistical associations and should not be interpreted
as evidence of cause and effect.
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

research_page = st.Page(
    "pages/1_Research.py",
    title="Research",
    icon="📚"
)

results_page = st.Page(
    "pages/2_Results.py",
    title="Results",
    icon="📊"
)

methodology_page = st.Page(
    "pages/3_Methodology.py",
    title="Methodology",
    icon="🔬"
)

policy_page = st.Page(
    "pages/4_Policy_Implications.py",
    title="Policy Implications",
    icon="💡"
)

about_page = st.Page(
    "pages/5_About.py",
    title="About",
    icon="👤"
)

pg = st.navigation([
    home_page,
    research_page,
    results_page,
    methodology_page,
    policy_page,
    about_page
])

pg.run()