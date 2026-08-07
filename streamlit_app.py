import streamlit as st

st.set_page_config(
    page_title="Feeling Left Behind and Democracy in Germany",
    page_icon="🏛️",
    layout="wide"
)

# ============================================================
# HOME PAGE
# ============================================================

def home():

    st.title(
        "🏛️ Feeling Left Behind: "
        "A Hidden Dimension of Democratic Disconnection"
    )

    st.subheader(
        "How perceptions of social neglect relate to institutional trust, "
        "democratic satisfaction and party representation in Germany"
    )

    st.divider()

    # ========================================================
    # MAIN QUESTION
    # ========================================================

    st.header("The question")

    st.markdown("""
**Does feeling left behind help us understand people's relationship with
democracy better than income, education and social class alone?**

This project uses data from the **German Longitudinal Election Study
(GLES 2025)** to examine whether people who feel overlooked,
unrecognized or underserved also evaluate democracy differently.
""")

    st.divider()

    # ========================================================
    # KEY NUMBERS
    # ========================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Survey respondents",
            "7,336"
        )

    with col2:
        st.metric(
            "Analytical sample",
            "5,039"
        )

    with col3:
        st.metric(
            "Democratic outcomes studied",
            "3"
        )

    st.divider()

    # ========================================================
    # MAIN FINDING
    # ========================================================

    st.header("What did we find?")

    st.success("""
### Feeling left behind is strongly connected to trust and democratic satisfaction.

After taking into account income, education, age, East/West Germany,
migration background, political interest and perceived social class,
the **Left Behind Index remained the strongest standardized predictor**
of both:

- **Institutional Trust**
- **Democratic Satisfaction**

Its relationship with **Party Representation** was much weaker.
""")

    st.markdown("""
This means that people's **subjective experience of being overlooked or
left behind contains information that socioeconomic characteristics
alone do not capture**.
""")

    st.divider()

    # ========================================================
    # QUICK RESULTS
    # ========================================================

    st.header("The result at a glance")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
### 🏛️ Institutional Trust

Before Left Behind:

**10.7% explained**

After Left Behind:

## **27.6%**

**+16.9 percentage points**
""")

    with c2:
        st.markdown("""
### 🗳️ Democratic Satisfaction

Before Left Behind:

**9.6% explained**

After Left Behind:

## **22.2%**

**+12.6 percentage points**
""")

    with c3:
        st.markdown("""
### 👥 Party Representation

Before Left Behind:

**3.9% explained**

After Left Behind:

## **5.3%**

**+1.4 percentage points**
""")

    st.divider()

    # ========================================================
    # WHAT LEFT BEHIND MEANS
    # ========================================================

    st.header("What does 'Feeling Left Behind' mean?")

    st.markdown("""
It does **not simply mean having a low income**.

The index captures whether people feel that people like them:

- receive too little attention to their economic situation;
- receive too little recognition for their work;
- receive insufficient attention regarding infrastructure and basic services;
- have less freedom to express their opinions publicly.

These four dimensions are combined into the project's
**Left Behind Index**.
""")

    st.info("""
👉 Open **Results → Left Behind Index** for the complete explanation
of the four questions and how the index was constructed.
""")

    st.divider()

    # ========================================================
    # NAVIGATION
    # ========================================================

    st.header("Explore the project")

    st.markdown("""
**📚 Research**  
What was studied, which data were used and why these variables were selected.

**📊 Results**  
What the analysis found, what Feeling Left Behind means and how the
three democratic outcomes were measured.

**🔬 Methodology**  
Index validation, regression models and statistical diagnostics.

**💡 Policy Implications**  
What the findings may mean for democratic institutions and public policy.

**👤 About**  
Project background and author.
""")

    st.divider()

    st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The analysis describes statistical associations and does not establish
cause-and-effect relationships.
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