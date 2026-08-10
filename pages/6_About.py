import streamlit as st

st.title("👤 About")

st.markdown("""
## About the project

**Feeling Left Behind and Democracy in Germany** is a data analytics
project examining whether subjective perceptions of social disconnection
help explain people's relationship with democratic institutions.
""")

st.divider()

# ============================================================
# PROJECT
# ============================================================

st.header("Project at a glance")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 📊 Data")

        st.markdown("""
German Longitudinal Election Study

**GLES 2025**

Post-Election Cross-Section
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🧩 Central concept")

        st.markdown("""
**Feeling Left Behind**

Economic attention  
Recognition  
Services  
Voice
""")

with c3:
    with st.container(border=True):

        st.markdown("### 🏛️ Outcomes")

        st.markdown("""
Institutional Trust  
Democratic Satisfaction  
Party Representation
""")

st.divider()

# ============================================================
# INTERDISCIPLINARY APPROACH
# ============================================================

st.header("Why this project?")

st.markdown("""
This project brings together **social science, programme thinking and
data analytics** to examine a public-policy question through empirical data.

The goal is not only to run statistical models, but also to translate
the results into evidence that can be understood by people without a
technical background.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🔬 Analytical goal")

        st.write(
            "Test whether subjective social disconnection provides "
            "information beyond traditional socioeconomic characteristics."
        )

with c2:
    with st.container(border=True):

        st.markdown("### 💬 Communication goal")

        st.write(
            "Make statistical evidence understandable without requiring "
            "the reader to be a statistician."
        )

st.divider()

# ============================================================
# WORKFLOW
# ============================================================

st.header("From survey data to evidence")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 1️⃣")
        st.markdown("**Data preparation**")

with c2:
    with st.container(border=True):
        st.markdown("### 2️⃣")
        st.markdown("**Index construction**")

with c3:
    with st.container(border=True):
        st.markdown("### 3️⃣")
        st.markdown("**Statistical analysis**")

with c4:
    with st.container(border=True):
        st.markdown("### 4️⃣")
        st.markdown("**Data communication**")

st.markdown("""
**Tools and methods**

Python · Pandas · Statistical modelling · Reliability analysis ·
Factor analysis · Regression diagnostics (OLS and logistic regression) ·
Plotly · Streamlit
""")

st.divider()

# ============================================================
# AUTHOR
# ============================================================

st.header("Author")

st.markdown("""
### Ricardo Martins Batista

**Sociologist · Programme Manager · Data Analyst**

Berlin, Germany
""")

st.markdown("""
Professional interests:

- Democratic Participation
- Public Policy
- Sustainability
- Social Impact
- Data Analytics
- Evidence-based Decision Making
""")

st.divider()

# ============================================================
# TRANSPARENCY
# ============================================================

st.header("Transparency")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### What the data show")

        st.write(
            "Statistical relationships between Feeling Left Behind "
            "and different democratic attitudes."
        )

with c2:
    with st.container(border=True):

        st.markdown("### What the data do not show")

        st.write(
            "Proof that Feeling Left Behind causes changes in trust, "
            "satisfaction or party representation."
        )

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The analyses use cross-sectional observational data.
""")