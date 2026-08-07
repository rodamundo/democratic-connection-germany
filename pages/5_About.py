import streamlit as st

st.title("👤 About")

st.markdown("""
## About the project

**Feeling Left Behind and Democracy in Germany** is a data analytics project
examining whether subjective perceptions of social neglect help explain
people's relationship with democratic institutions.
""")

st.divider()

# ============================================================
# PROJECT AT A GLANCE
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
        st.markdown("### 🧩 Main concept")
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
# APPROACH
# ============================================================

st.header("From survey data to public-facing evidence")

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
The analytical workflow includes:

**Python · Pandas · Statistical modelling · Reliability analysis ·
Factor analysis · Regression diagnostics · Plotly · Streamlit**
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
Areas of professional interest include:

**Democratic Participation · Public Policy · Sustainability ·
Social Impact · Data Analytics · Evidence-based Decision Making**
""")

st.divider()

# ============================================================
# PURPOSE
# ============================================================

st.header("Why this project?")

st.markdown("""
The project combines **social science and data analytics**.

Its purpose is not only to perform statistical analysis, but to demonstrate
how complex social research can be transformed into evidence that is useful
for both **technical and non-technical audiences**.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### Scientific goal")
        st.write(
            "Test whether subjective social disconnection adds information "
            "beyond traditional socioeconomic characteristics."
        )

with c2:
    with st.container(border=True):
        st.markdown("### Communication goal")
        st.write(
            "Make statistical findings understandable without requiring "
            "the reader to be a statistician."
        )

st.divider()

# ============================================================
# TRANSPARENCY
# ============================================================

st.header("Transparency")

st.markdown("""
The project distinguishes carefully between:

### What the data show

Statistical relationships between Feeling Left Behind and democratic attitudes.

### What the data do not show

Proof that Feeling Left Behind causes changes in trust, satisfaction
or political representation.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The analyses use cross-sectional observational data.
""")