import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Feeling Left Behind | Germany",
    page_icon="🏛️",
    layout="wide"
)


# ============================================================
# OPTIONAL PUBLIC LINKS
# ============================================================

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
What happens when people feel **unseen, insufficiently recognized,
poorly served or unable to speak openly**?

This project uses the **German Longitudinal Election Study (GLES 2025)**
to examine whether Feeling Left Behind adds information beyond
conventional socioeconomic, demographic and political characteristics.

The research has developed in stages. It first examined democratic
attitudes, then party choice, and now opens the Left Behind Index to ask
whether its four components carry the same political information.
""")

    st.info("""
### The central idea

Two people with similar income, education or demographic profiles can
still experience their relationship with society and politics very
differently.

The project asks whether those **subjective experiences of disconnection**
help us diagnose democratic and electoral patterns more clearly.
""")

    st.divider()

    # ========================================================
    # RESEARCH STREAM
    # ========================================================

    st.header("The research stream")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 1️⃣ Democratic attitudes")

            st.markdown("""
Does the overall Left Behind Index add information about:

- Institutional Trust
- Democratic Satisfaction
- Party Representation

beyond a conventional profile?
""")

            st.metric(
                "Trust R²",
                "11.1% → 28.1%"
            )

            st.metric(
                "Satisfaction R²",
                "9.4% → 22.0%"
            )

            st.caption(
                "Controls-only model → controls + overall LBI. "
                "The gain is much smaller for generic party representation."
            )

    with c2:
        with st.container(border=True):

            st.markdown("### 2️⃣ Party choice")

            st.markdown("""
Does Feeling Left Behind help distinguish reported second-vote choices
across seven parties?

The overall LBI adds modest predictive information beyond the
conventional voter profile.
""")

            st.metric(
                "Conventional profile",
                "35.8%"
            )

            st.metric(
                "+ overall LBI",
                "38.2%"
            )

            st.caption(
                "Repeated held-out accuracy in the common seven-party sample."
            )

    with c3:
        with st.container(border=True):

            st.markdown("### 3️⃣ Opening the index")

            st.markdown("""
The four LBI items count equally in the index, but they do **not** show
the same relationships with political outcomes.

The strongest contrast concerns perceived inability to express opinions
freely in public.
""")

            st.metric(
                "Party accuracy with 4 components",
                "39.9%"
            )

            st.metric(
                "AfD: public-expression scenario",
                "+34.1 pp"
            )

            st.caption(
                "Adjusted model-based association when the item is moved "
                "from 1 to 4, with other modeled characteristics unchanged."
            )

    st.divider()

    # ========================================================
    # KEY DIAGNOSIS
    # ========================================================

    st.header("What the newer analyses add")

    st.markdown("""
The overall Left Behind Index remains useful, but opening it reveals an
important distinction.

Among the four components, **perceived inability to express opinions
freely in public** is much more strongly related to:

- higher estimated AfD support;
- lower Institutional Trust; and
- lower Democratic Satisfaction.

The relationship with AfD becomes smaller after respondents' own
left-right political position is taken into account, but only by about
**14%**. The result therefore cannot be reduced to left-right
self-placement alone.
""")

    st.warning("""
### Important interpretation

The survey measures whether respondents **perceive** that people like
them are no longer allowed to express their opinions freely in public.

The analysis does **not** establish that freedom of expression is
objectively restricted, and it does not identify what opinions
respondents have in mind.
""")

    st.divider()

    # ========================================================
    # SAXONY-ANHALT
    # ========================================================

    st.header("A prospective extension: Saxony-Anhalt")

    st.markdown("""
Saxony-Anhalt remains a useful extension of the project because it has a
high average Left Behind Index in the historical party-choice sample.
The comparison is used as a **directional benchmark**, not as an opinion
poll or a formal vote-share forecast.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric("Saxony-Anhalt mean LBI", "2.84")
    c2.metric("Rest of Germany", "2.49")
    c3.metric("Difference", "+0.35")

    st.caption(
        "Descriptive comparison in the historical party-choice analytical sample."
    )

    st.divider()

    # ========================================================
    # HOW TO USE
    # ========================================================

    st.header("How to use this site")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown("### 🧩 Concept")
            st.markdown(
                "See how Feeling Left Behind is defined, constructed "
                "and checked as a four-item index."
            )

    with c2:
        with st.container(border=True):
            st.markdown("### 📊 Outcomes")
            st.markdown(
                "Explore the evidence for democratic attitudes and party choice."
            )

    with c3:
        with st.container(border=True):
            st.markdown("### 🧭 Components")
            st.markdown(
                "Compare the four LBI components and the political patterns "
                "associated with each one."
            )

    with c4:
        with st.container(border=True):
            st.markdown("### 🔬 Method")
            st.markdown(
                "See the model design, cross-validation, robustness tests "
                "and limitations."
            )

    st.success("""
### Portfolio logic

The public articles tell the **story and political relevance**.

This site provides the **analytical depth, model comparisons and
robustness checks behind that story**.
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
Post-Election Cross-Section, ZA10100 Version 3.0.0.

The analyses use observational survey data. Reported relationships are
associational and should not be interpreted as causal effects.
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

democratic_attitudes_page = st.Page(
    "pages/3_Democratic_Attitudes.py",
    title="Democratic Attitudes",
    icon="📊"
)

party_choice_page = st.Page(
    "pages/4_Party_Choice.py",
    title="Party Choice",
    icon="🗳️"
)

components_page = st.Page(
    "pages/5_LBI_Components.py",
    title="LBI Components",
    icon="🧭"
)

methodology_page = st.Page(
    "pages/6_Methodology.py",
    title="Methodology",
    icon="🔬"
)

diagnosis_page = st.Page(
    "pages/7_Political_Diagnosis.py",
    title="Political Diagnosis",
    icon="💡"
)

about_page = st.Page(
    "pages/8_About.py",
    title="About",
    icon="👤"
)


pg = st.navigation([
    home_page,
    left_behind_page,
    research_page,
    democratic_attitudes_page,
    party_choice_page,
    components_page,
    methodology_page,
    diagnosis_page,
    about_page
])

pg.run()
