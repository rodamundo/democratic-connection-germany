import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.title("👤 About")

st.markdown("""
## About the project

**Feeling Left Behind** is an ongoing research and data-communication
project about the relationship between citizens, representation and
democracy in Germany.

The project asks whether subjective perceptions of being overlooked,
insufficiently recognized, poorly served or unable to speak openly provide
information that conventional socioeconomic, demographic and political
characteristics do not fully capture.
""")

st.divider()


# ============================================================
# PROJECT AT A GLANCE
# ============================================================

st.header("Project at a glance")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 📊 Primary data")
        st.markdown("""
German Longitudinal Election Study

**GLES 2025**

Post-Election Cross-Section

ZA10100 Version 3.0.0
""")

with c2:
    with st.container(border=True):
        st.markdown("### 🧩 Central concept")
        st.markdown("""
**Feeling Left Behind**

Economic attention

Social recognition

Services

Public expression
""")

with c3:
    with st.container(border=True):
        st.markdown("### 🏛️ Political questions")
        st.markdown("""
Institutional Trust

Democratic Satisfaction

Party Representation

Party Choice
""")

st.divider()


# ============================================================
# RESEARCH STREAM
# ============================================================

st.header("The research stream")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### Stage 1")
        st.markdown("""
## Democratic attitudes

Does the overall Left Behind Index add information about Trust,
Democratic Satisfaction and Party Representation beyond a conventional
socioeconomic, demographic and political profile?
""")

with c2:
    with st.container(border=True):
        st.markdown("### Stage 2")
        st.markdown("""
## Party choice

Does Feeling Left Behind add useful information about reported 2025
second-vote choice across the seven-party system?
""")

with c3:
    with st.container(border=True):
        st.markdown("### Stage 3")
        st.markdown("""
## LBI components

Do the four equally weighted components carry the same political
information, or do some stand out for particular outcomes and parties?
""")

st.divider()


# ============================================================
# WHY THIS PROJECT
# ============================================================

st.header("Why this project?")

st.markdown("""
This project brings together **social science, programme thinking, data
analytics and public communication**.

The goal is not only to run statistical models. It is also to turn those
models into evidence that can be understood, questioned and used by
people who do not work with data every day.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### 🔬 Analytical goal")
        st.write(
            "Test whether subjective political and social experience "
            "provides information beyond conventional characteristics, "
            "and examine where that information is concentrated."
        )

with c2:
    with st.container(border=True):
        st.markdown("### 💬 Communication goal")
        st.write(
            "Translate statistical evidence into clear public-facing "
            "research without hiding uncertainty, alternative explanations "
            "or limitations."
        )

st.divider()


# ============================================================
# METHODS
# ============================================================

st.header("Methods used across the project")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 🧩 Measurement")
        st.markdown("""
- Index construction
- Scale reversal
- Equal weighting
- Reliability analysis
- Descriptive comparisons
""")

with c2:
    with st.container(border=True):
        st.markdown("### 📈 Statistical analysis")
        st.markdown("""
- Multiple linear regression
- Binary logistic regression
- Multinomial logistic regression
- Standardized coefficients
- Odds ratios
- Model-implied probabilities
""")

with c3:
    with st.container(border=True):
        st.markdown("### 🧪 Robustness and prediction")
        st.markdown("""
- Repeated cross-validation
- Held-out evaluation
- Bootstrap resampling
- Left-right robustness
- Matched-sample comparison
""")

st.divider()


# ============================================================
# WORKFLOW
# ============================================================

st.header("From survey data to public evidence")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 1️⃣")
        st.markdown("**Data preparation**")

with c2:
    with st.container(border=True):
        st.markdown("### 2️⃣")
        st.markdown("**Model design**")

with c3:
    with st.container(border=True):
        st.markdown("### 3️⃣")
        st.markdown("**Testing and robustness**")

with c4:
    with st.container(border=True):
        st.markdown("### 4️⃣")
        st.markdown("**Public communication**")

st.markdown("""
**Tools**

Python · Pandas · NumPy · scikit-learn · statsmodels · Plotly · Streamlit
""")

st.divider()


# ============================================================
# PORTFOLIO LOGIC
# ============================================================

st.header("How the portfolio is structured")

st.info("""
### Public articles

The newsletter focuses on **the question, the evidence and why it matters**.

### This Streamlit site

The site provides the **analytical layer behind the public-facing research**:
model comparisons, component results, robustness tests and interpretation boundaries.
""")

st.markdown("""
The two formats are designed to complement each other:

**Public communication**

↓

**Transparent analytical evidence**

↓

**A research programme that can be extended and tested over time**
""")

st.divider()


# ============================================================
# AUTHOR
# ============================================================

st.header("Author")

st.markdown("""
### Ricardo Martins Batista

**Senior Program Director · Sustainability, Public Policy & Social Impact
· Data Analytics (SQL, Python, Tableau)**

Berlin, Germany
""")

st.markdown("""
10+ years of international experience leading public policy, sustainability
and social impact initiatives across Europe, Latin America and Africa —
turning high-level strategy into execution, navigating complex political
ecosystems, scaling grassroots organizations, and building multi-stakeholder
partnerships between public administrations, international networks, NGOs
and corporate partners.

In 2026, I completed a Data Analytics Certification (SQL, Python, Tableau,
Power BI) at WBS Coding School. **Feeling Left Behind** — this project —
was the certification's capstone: an application of data analysis to a
real democratic-representation question. It was featured in a LinkedIn
newsletter and covered by *Público*, Portugal's national newspaper.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 🎤 Public speaking")
        st.write(
            "TEDx speaker (TEDxUniMannheim) and UN presenter (COP23) on "
            "advocacy and fundraising methodologies."
        )

with c2:
    with st.container(border=True):
        st.markdown("### 🌍 Programme leadership")
        st.write(
            "Founded and scaled social-impact and mobility programmes "
            "across Brazil, Portugal and Africa/Europe."
        )

with c3:
    with st.container(border=True):
        st.markdown("### 📊 Data + impact")
        st.write(
            "Now combining stakeholder management with hands-on data "
            "modeling for impact evaluation (MEL/ESG)."
        )

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("#### Experience")
        st.markdown("""
**Data Analytics Bootcamp** — WBS Coding School
Berlin, Germany · 2026

**Co-Founder & Executive Director, Community Development & Mobility**
— PEDALA QUEIMADOS (NGO)
Rio de Janeiro, Brazil · 2016 – 2026

**Customer Experience Officer, CX Ambassador International** — Canyon
Remote, Germany · 2024 – 2026

**Founder & Program Director, Sustainable Mobility & Social Impact**
— Roda Mundo
Lisbon, Portugal · 2023 – 2025

**Founder & Global Program Director, Global Leadership & Capacity
Building** — The Bamboo Trip Project
Africa & Europe · 2016 – 2023
""")

with c2:
    with st.container(border=True):
        st.markdown("#### Education & languages")
        st.markdown("""
**Instituto Universitário de Pesquisas do Rio de Janeiro**
Sociology, Urban Planning specialization · 2013 – 2016

**Universidade Cândido Mendes**
Bachelor's degree, Marketing · 2003 – 2007

**WBS Coding School**
Data Analytics Certification · 2026

---

**Languages:** Portuguese (native) · English (C1) · Spanish (C1) ·
German (A2)
""")

st.link_button(
    "Connect on LinkedIn",
    "https://www.linkedin.com/in/ricardo-martins-batista/",
    use_container_width=True
)

st.divider()


# ============================================================
# TRANSPARENCY
# ============================================================

st.header("Transparency")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### What the analyses show")
        st.write(
            "Statistical relationships between Feeling Left Behind, its "
            "components and democratic or electoral outcomes, together "
            "with tests of whether those relationships add information "
            "beyond conventional profiles."
        )

with c2:
    with st.container(border=True):
        st.markdown("### What the analyses do not show")
        st.write(
            "Proof that Feeling Left Behind causes changes in trust, "
            "satisfaction, representation or voting behaviour, or proof "
            "that perceived restrictions on public expression are objectively present."
        )

st.divider()

st.caption("""
Primary source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

The Left Behind Index is constructed for this project and is not an
official GLES scale. The analyses use observational survey data.
""")
