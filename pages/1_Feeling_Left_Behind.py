import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE
# ============================================================

st.title("🧩 Feeling Left Behind")

st.subheader(
    "How the Left Behind Index is defined, constructed and interpreted"
)

st.markdown("""
## What does “Feeling Left Behind” mean?

Feeling Left Behind describes a **subjective experience of social and
political disconnection**.

It captures whether people feel that people like them receive too little
attention, recognition or access to services, and whether they perceive
that people like them are no longer able to express their opinions freely
in public.

This is not the same thing as having a low income, belonging to a
particular social class or supporting a particular political party.
""")

st.divider()


# ============================================================
# THREE CONCEPTS
# ============================================================

st.header("1. Three concepts that should not be confused")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 💰 Household Income")
        st.markdown("""
**What resources do I have?**

Measures the economic resources available to a household.
""")
        st.caption("Objective socioeconomic position")

with c2:
    with st.container(border=True):
        st.markdown("### 🪜 Subjective Social Class")
        st.markdown("""
**Where do I see myself in society?**

Measures where people believe they sit in the social hierarchy.
""")
        st.caption("Perceived social position")

with c3:
    with st.container(border=True):
        st.markdown("### 🧩 Feeling Left Behind")
        st.markdown("""
**Do I feel that people like me are considered?**

Measures perceived attention, recognition, services and public expression.
""")
        st.caption("Subjective disconnection")

st.success("""
### Why the distinction matters

Two people with similar income, education or social position may still
feel very differently about whether people like them are recognized,
served or able to speak openly.
""")

st.divider()


# ============================================================
# FOUR ITEMS
# ============================================================

st.header("2. The four survey items")

st.markdown("""
The project constructs the Left Behind Index from four items in the
**GLES 2025 Post-Election Cross-Section**.

Respondents were asked how strongly they agreed or disagreed with four
statements.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### 💶 Economic attention")
        st.markdown("""
**In simple terms**

*Do the economic concerns of people like me receive too little attention?*

**GLES statement**

> “The economic situation of people like me receives too little attention from society.”

**Variable:** `q46a`
""")

    with st.container(border=True):
        st.markdown("### 🏥 Infrastructure and basic services")
        st.markdown("""
**In simple terms**

*Do people like me receive adequate access to essential services?*

**GLES statement**

> “Society pays too little attention to ensuring that people like me have access to basic infrastructures and services.”

Examples in the survey include doctors, public transportation, schools,
banks, post offices and Internet access.

**Variable:** `q46c`
""")

with c2:
    with st.container(border=True):
        st.markdown("### 👏 Social recognition")
        st.markdown("""
**In simple terms**

*Is the work and contribution of people like me recognized?*

**GLES statement**

> “People like me receive too little recognition from society for the work they do.”

**Variable:** `q46b`
""")

    with st.container(border=True):
        st.markdown("### 🗣️ Perceived freedom of public expression")
        st.markdown("""
**In simple terms**

*Do people like me feel able to express their opinions freely in public?*

**GLES statement**

> “People like me are no longer allowed to freely express their opinions in public.”

**Variable:** `q46d`
""")

st.warning("""
### A necessary distinction

The fourth item measures a **perception**. It tells us whether respondents
agree that people like them are no longer allowed to express their
opinions freely in public.

It does not tell us what opinions they have in mind, what they believe
prevents them from speaking, or whether an objective restriction is
actually present.
""")

st.divider()


# ============================================================
# SCALE
# ============================================================

st.header("3. From survey answers to a 1–5 index")

st.markdown("""
Each original item uses the same five-point response scale:
""")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("1", "Strongly agree")
c2.metric("2", "Agree")
c3.metric("3", "Neither")
c4.metric("4", "Disagree")
c5.metric("5", "Strongly disagree")

st.markdown("""
Agreement with these negative statements indicates **stronger Feeling
Left Behind**, but the original survey codes stronger agreement with a
smaller number.

The project therefore reverses each item:
""")

st.code("reversed_score = 6 - original_score", language="python")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric("1", "Lower Feeling Left Behind")
        st.caption("Respondent tends to disagree with the statements.")

with c2:
    with st.container(border=True):
        st.metric("5", "Higher Feeling Left Behind")
        st.caption("Respondent tends to agree with the statements.")

st.divider()


# ============================================================
# INDEX CREATION
# ============================================================

st.header("4. How the four items become one index")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 💶")
        st.markdown("**Economic attention**")

with c2:
    with st.container(border=True):
        st.markdown("### 👏")
        st.markdown("**Social recognition**")

with c3:
    with st.container(border=True):
        st.markdown("### 🏥")
        st.markdown("**Services**")

with c4:
    with st.container(border=True):
        st.markdown("### 🗣️")
        st.markdown("**Public expression**")

st.markdown("""
### ↓

The four reversed responses are **averaged with equal weight**.

### ↓

# Left Behind Index: 1–5
""")

st.info("""
### Equal weighting

Each item contributes one quarter of the overall LBI.

The index itself does **not** assume that one component is more important
than another. Later analyses ask a different question: whether the four
components have equally strong relationships with political outcomes.
""")

c1, c2, c3 = st.columns(3)

c1.metric("Complete four-item LBI", "6,831 respondents")
c2.metric("Minimum", "1")
c3.metric("Maximum", "5")

st.divider()


# ============================================================
# EXAMPLE
# ============================================================

st.header("5. A simple example")

st.markdown("""
Imagine a respondent has these **reversed scores**:
""")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Economic attention", "5")
c2.metric("Recognition", "4")
c3.metric("Services", "4")
c4.metric("Public expression", "3")

st.markdown("""
The Left Behind Index is:

### **(5 + 4 + 4 + 3) ÷ 4 = 4.0**

A value of **4.0** represents relatively strong Feeling Left Behind on
this constructed measure.
""")

st.divider()


# ============================================================
# VALIDATION
# ============================================================

st.header("6. Can the four items be combined?")

st.markdown("""
The project checks whether the four items behave consistently enough to
be summarized by a common index.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric("Cronbach's α: four items", "0.753")
        st.caption("Acceptable internal consistency for the four-item scale.")

with c2:
    with st.container(border=True):
        st.metric("Cronbach's α without public expression", "0.757")
        st.caption("An increase of only about 0.004.")

st.success("""
### Measurement conclusion

The public-expression item is somewhat distinct, but removing it barely
changes the scale's internal consistency. The measurement checks do not
provide a strong reason to drop it from the LBI.
""")

st.divider()


# ============================================================
# DESCRIPTIVE PATTERNS
# ============================================================

st.header("7. What does the overall index look like descriptively?")

st.markdown("""
These examples show **raw descriptive averages**. They are not adjusted
regression results and should not be interpreted as causal effects.
""")

region_df = pd.DataFrame({
    "Region": ["East Germany", "West Germany"],
    "Average LBI": [2.73, 2.48]
})

class_df = pd.DataFrame({
    "Subjective social class": [
        "Lower class",
        "Working class",
        "Lower middle class",
        "Middle class",
        "Upper middle class",
        "Upper class"
    ],
    "Average LBI": [3.26, 3.13, 2.81, 2.42, 2.14, 1.89]
})

tab1, tab2 = st.tabs([
    "By subjective social class",
    "By East / West region"
])

with tab1:
    fig = px.bar(
        class_df,
        x="Subjective social class",
        y="Average LBI",
        text="Average LBI",
        title="Average Left Behind Index by Subjective Social Class"
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(
        height=440,
        xaxis_title="",
        yaxis_title="Average LBI",
        yaxis=dict(range=[0, 3.6])
    )
    st.plotly_chart(fig, width="stretch")

with tab2:
    fig = px.bar(
        region_df,
        x="Region",
        y="Average LBI",
        text="Average LBI",
        title="Average Left Behind Index by East / West Region"
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(
        height=420,
        xaxis_title="",
        yaxis_title="Average LBI",
        yaxis=dict(range=[0, 3.1])
    )
    st.plotly_chart(fig, width="stretch")

st.caption(
    "Descriptive averages from the GLES 2025 project data. "
    "Adjusted relationships are examined on the evidence pages."
)

st.divider()


# ============================================================
# WHY COMPONENTS
# ============================================================

st.header("8. Why open the index?")

st.markdown("""
An overall LBI score is useful because it summarizes four related
experiences in one number.

But two respondents can reach the same overall score through different
combinations of those experiences. The newer analyses therefore compare
the four components separately.
""")

st.success("""
### The key analytical distinction

**Equal weight in the index does not imply equal relationship with every
political outcome.**

The LBI Components page shows which parts of Feeling Left Behind stand
out for party choice, Institutional Trust and Democratic Satisfaction.
""")

st.divider()

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

The Left Behind Index is constructed for this project and is not an
official GLES scale.
""")
