import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Feeling Left Behind | Research Portfolio",
    page_icon="🏛️",
    layout="wide"
)


# ============================================================
# OPTIONAL PUBLIC LINKS
# ============================================================

# Add your public links here when you want buttons on the Home and About pages.
LINKEDIN_NEWSLETTER_URL = ""
GITHUB_URL = ""


# ============================================================
# HOME
# ============================================================

def home():

    st.title("🏛️ Feeling Left Behind")

    st.subheader(
        "An ongoing research project on citizens, representation "
        "and democracy in Germany"
    )

    st.markdown("""
What happens when people feel **unseen, unheard or poorly served by politics**?

This project uses German election survey data to study whether
**Feeling Left Behind** adds information that conventional
socioeconomic, demographic and political characteristics do not capture.

The project has developed in stages. The first study focuses on
**institutional trust, democratic satisfaction and party representation**.
The second asks whether the same concept also helps us understand
**actual party choice**, and whether those historical patterns are useful
for interpreting the political context in Saxony-Anhalt before its
2026 state election.
""")

    st.info("""
### The central idea

Political disconnection may not be only about **what resources people have**.

It may also be about whether people feel that people like them are
**seen, recognized, served and heard**.
""")

    st.divider()

    # ========================================================
    # RESEARCH STREAM
    # ========================================================

    st.header("The research stream")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### 1️⃣ Democratic attitudes")

            st.markdown("""
**Question**

Does Feeling Left Behind help us understand people's relationship
with democracy beyond conventional voter characteristics?

**Outcomes**

- Institutional Trust
- Democratic Satisfaction
- Party Representation
""")

            m1, m2 = st.columns(2)

            with m1:
                st.metric(
                    "Trust model fit",
                    "8.46% → 26.29%"
                )

            with m2:
                st.metric(
                    "Satisfaction model fit",
                    "7.97% → 21.20%"
                )

            st.caption(
                "Model fit improves substantially for Trust and "
                "Democratic Satisfaction after Feeling Left Behind is added."
            )

    with c2:
        with st.container(border=True):

            st.markdown("### 2️⃣ Party choice")

            st.markdown("""
**Question**

Does Feeling Left Behind add useful information about party choice
beyond age, income, education, region, migration background and
political interest?

**Main contrast**

AfD and Green voters occupy particularly different positions
on the Left Behind Index.
""")

            m1, m2 = st.columns(2)

            with m1:
                st.metric(
                    "AfD probability",
                    "1.7% → 33.7%"
                )

            with m2:
                st.metric(
                    "Green probability",
                    "37.7% → 5.0%"
                )

            st.caption(
                "Model-based estimates when the same conventional "
                "voter profiles are used and only the Left Behind Index changes."
            )

    st.divider()

    # ========================================================
    # WHY SAXONY-ANHALT
    # ========================================================

    st.header("Why Saxony-Anhalt enters the project")

    st.markdown("""
Saxony-Anhalt provides a useful new context because respondents from the
state have the **highest average Feeling Left Behind score among the
16 German states in the party-choice analytical sample**.

The project does not treat the Left Behind Index as an alternative
to opinion polling. Instead, the historical relationship between
Feeling Left Behind and party choice is used as a **directional benchmark**
that can be compared with the political pattern visible before election day.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Saxony-Anhalt mean LBI",
        "2.84"
    )

    c2.metric(
        "Rest of Germany",
        "2.49"
    )

    c3.metric(
        "Difference",
        "+0.35"
    )

    st.caption(
        "Descriptive comparison in the party-choice analytical sample."
    )

    st.divider()

    # ========================================================
    # HOW TO USE
    # ========================================================

    st.header("How to use this site")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("### 🧩 Concept")
            st.markdown(
                "See how Feeling Left Behind is defined, constructed "
                "and validated."
            )

    with c2:
        with st.container(border=True):
            st.markdown("### 📊 Evidence")
            st.markdown(
                "Explore the statistical results for democratic attitudes "
                "and party choice."
            )

    with c3:
        with st.container(border=True):
            st.markdown("### 🔬 Method")
            st.markdown(
                "See how the analyses were designed, tested and interpreted."
            )

    st.success("""
### The portfolio logic

The public articles tell the **story and political relevance**.

This site provides the **analytical depth behind that story**.
""")

    if LINKEDIN_NEWSLETTER_URL or GITHUB_URL:

        st.divider()
        st.header("Public links")

        c1, c2 = st.columns(2)

        if LINKEDIN_NEWSLETTER_URL:
            c1.link_button(
                "Read the LinkedIn newsletter",
                LINKEDIN_NEWSLETTER_URL,
                use_container_width=True
            )

        if GITHUB_URL:
            c2.link_button(
                "View the code",
                GITHUB_URL,
                use_container_width=True
            )

    st.divider()

    st.caption("""
Data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The analyses use observational survey data. Reported relationships
should not be interpreted as causal effects.
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
    icon="🔎"
)

results_page = st.Page(
    "pages/3_Results.py",
    title="Study 1 Results",
    icon="📊"
)

party_choice_page = st.Page(
    "pages/7_Party_Choice.py",
    title="Party Choice",
    icon="🗳️"
)

methodology_page = st.Page(
    "pages/4_Methodology.py",
    title="Study 1 Methodology",
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
    party_choice_page,
    methodology_page,
    policy_page,
    about_page
])

pg.run()
