import streamlit as st

st.title("🧩 Feeling Left Behind")

st.subheader(
    "Understanding the central concept behind this research"
)

st.markdown("""
## What does “Feeling Left Behind” mean?

Feeling Left Behind describes a **subjective experience of social
disconnection**.

It captures whether people feel that **people like them are overlooked,
insufficiently recognized, underserved or constrained in expressing
their views**.

This is important because Feeling Left Behind is **not the same thing
as having a low income or belonging to a particular social class**.
""")

st.divider()

# ============================================================
# THREE DIFFERENT CONCEPTS
# ============================================================

st.header("Three concepts that should not be confused")

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
**Do I feel that people like me are seen and considered?**

Measures perceived attention, recognition, services and voice.
""")
        st.caption("Subjective social disconnection")

st.success("""
### Why does this distinction matter?

Two people with similar income and education may still feel very
differently about whether society recognizes, listens to or provides
adequately for people like them.

The research tests whether these differences are connected to
democratic attitudes.
""")

st.divider()

# ============================================================
# FOUR DIMENSIONS
# ============================================================

st.header("How was Feeling Left Behind measured?")

st.markdown("""
The GLES survey asked respondents:

> **“To what extent do you agree with the following statements or not?”**

Four statements are used in this project.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("### 💶 1. Economic attention")

        st.markdown("""
**In simple terms:**

*Are the economic concerns of people like me being overlooked?*

**GLES statement:**

> “The economic situation of people like me receives too little
> attention from society.”

**Variable:** `q46a`
""")

    with st.container(border=True):

        st.markdown("### 🏥 3. Infrastructure and basic services")

        st.markdown("""
**In simple terms:**

*Do people like me receive adequate access to essential services?*

**GLES statement:**

> “Society pays too little attention to ensuring that people like me
> have access to basic infrastructures and services.”

Examples provided by the survey include:

- doctors;
- public transportation;
- schools;
- banks;
- post offices;
- Internet access.

**Variable:** `q46c`
""")

with c2:

    with st.container(border=True):

        st.markdown("### 👏 2. Social recognition")

        st.markdown("""
**In simple terms:**

*Is the work and contribution of people like me recognized?*

**GLES statement:**

> “People like me receive too little recognition from society
> for the work they do.”

**Variable:** `q46b`
""")

    with st.container(border=True):

        st.markdown("### 🗣️ 4. Freedom of expression")

        st.markdown("""
**In simple terms:**

*Do people like me feel free to express their opinions publicly?*

**GLES statement:**

> “People like me are no longer allowed to freely express their
> opinions in public.”

**Variable:** `q46d`
""")

st.divider()

# ============================================================
# ORIGINAL SCALE
# ============================================================

st.header("How did respondents answer?")

st.markdown("""
Each question originally uses the same five-point scale:
""")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("1", "Strongly agree")

with c2:
    st.metric("2", "Agree")

with c3:
    st.metric("3", "Neither")

with c4:
    st.metric("4", "Disagree")

with c5:
    st.metric("5", "Strongly disagree")

st.divider()

# ============================================================
# REVERSING SCALE
# ============================================================

st.header("Why was the scale reversed?")

st.markdown("""
There is an important detail.

In the **original survey**, agreeing with these negative statements
indicates a **stronger feeling of being left behind**.

That means:

**1 = strongest agreement**

but numerically 1 is the smallest value.

To make the final index easier to understand, the scale was reversed.
""")

st.code(
    "reversed_score = 6 - original_score",
    language="python"
)

st.markdown("""
After reversing the scale:
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("""
### 1

## Lower Feeling Left Behind

Respondent tends to disagree with the statements.
""")

with c2:
    with st.container(border=True):
        st.markdown("""
### 5

## Higher Feeling Left Behind

Respondent tends to agree with the statements.
""")

st.success("""
### The final interpretation is simple:

**Higher score = stronger Feeling Left Behind**
""")

st.divider()

# ============================================================
# INDEX CREATION
# ============================================================

st.header("How do four answers become one index?")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 💶")
        st.markdown("**Economic attention**")

with c2:
    with st.container(border=True):
        st.markdown("### 👏")
        st.markdown("**Recognition**")

with c3:
    with st.container(border=True):
        st.markdown("### 🏥")
        st.markdown("**Services**")

with c4:
    with st.container(border=True):
        st.markdown("### 🗣️")
        st.markdown("**Voice**")

st.markdown("""
## ↓

The four reversed answers are **averaged for each respondent**.

## ↓

# 🧩 Left Behind Index
""")

st.markdown("""
The resulting score ranges conceptually from approximately:

### **1 — Lower Feeling Left Behind**

to

### **5 — Higher Feeling Left Behind**
""")

st.divider()

# ============================================================
# EXAMPLE
# ============================================================

st.header("A simple example")

st.markdown("""
Imagine a respondent has these **final reversed scores**:
""")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Economic attention", "5")
c2.metric("Recognition", "4")
c3.metric("Services", "4")
c4.metric("Voice", "3")

st.markdown("""
The Left Behind Index would be:

**(5 + 4 + 4 + 3) ÷ 4 = 4.0**

A score of **4.0** represents a relatively strong subjective
feeling of being left behind.
""")

st.divider()

# ============================================================
# VALIDATION
# ============================================================

st.header("Can these four questions really be combined?")

st.markdown("""
Before treating the four questions as one index, the analysis checked
whether they behave consistently enough to represent a common concept.
""")

with st.expander("Technical validation"):

    c1, c2 = st.columns(2)

    c1.metric(
        "Cronbach's α",
        "0.753"
    )

    c2.metric(
        "Factor 1 eigenvalue",
        "2.323"
    )

    st.markdown("""
**Cronbach's α = 0.753** indicates acceptable internal consistency.

The factor analysis also found a clear dominant factor.

Together, these results support summarizing the four questions
with one Left Behind Index.
""")

st.divider()

# ============================================================
# WHAT THE INDEX DOES NOT MEAN
# ============================================================

st.header("What the index does — and does not — tell us")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### ✅ What it measures")
        st.markdown("""
Respondents' **perceptions** of:

- economic attention;
- social recognition;
- access to services;
- freedom of expression.
""")

with c2:
    with st.container(border=True):
        st.markdown("### ⚠️ What it does not prove")
        st.markdown("""
It does not objectively establish that society actually neglects
a particular respondent or group.

It measures **perceived social disconnection**.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Variables used: q46a, q46b, q46c and q46d.
""")