import streamlit as st
import pandas as pd
import plotly.express as px


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

Two people with similar income, education or perceived social position
may still feel very differently about whether society recognizes,
listens to or provides adequately for people like them.

The research tests whether Feeling Left Behind is associated with
democratic attitudes beyond traditional characteristics.
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

c1.metric("1", "Strongly agree")
c2.metric("2", "Agree")
c3.metric("3", "Neither")
c4.metric("4", "Disagree")
c5.metric("5", "Strongly disagree")

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
The resulting score ranges conceptually from:

### **1: Lower Feeling Left Behind**

to

### **5: Higher Feeling Left Behind**
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
# WHO FEELS MORE LEFT BEHIND?
# ============================================================

st.header("Who feels more left behind?")

st.markdown("""
Before looking at how Feeling Left Behind relates to democratic
attitudes, it helps to see how the index itself varies across
different groups.

These are **descriptive averages**, not the regression models used
elsewhere in the project.

They describe patterns in the raw index rather than adjusted effects.
""")


region_df = pd.DataFrame({
    "Region": ["East Germany", "West Germany"],
    "Left Behind Index": [2.73, 2.48]
})

age_df = pd.DataFrame({
    "Age group": ["16-29", "30-44", "45-59", "60+"],
    "Left Behind Index": [2.56, 2.64, 2.58, 2.52]
})

migration_df = pd.DataFrame({
    "Migration background": [
        "No migration background",
        "Migration background"
    ],
    "Left Behind Index": [2.56, 2.65]
})

class_df = pd.DataFrame({
    "Subjective Social Class": [
        "Lower class",
        "Working class",
        "Lower middle class",
        "Middle class",
        "Upper middle class",
        "Upper class"
    ],
    "Left Behind Index": [
        3.26,
        3.13,
        2.81,
        2.42,
        2.14,
        1.89
    ]
})

income_df = pd.DataFrame({
    "Income group": [
        "< €500",
        "€500–749",
        "€750–999",
        "€1,000–1,249",
        "€1,250–1,499",
        "€1,500–1,999",
        "€2,000–2,499",
        "€2,500–2,999",
        "€3,000–3,999",
        "€4,000–4,999",
        "€5,000–7,499",
        "€7,500–9,999",
        "€10,000+"
    ],
    "Left Behind Index": [
        3.05,
        2.69,
        3.00,
        3.01,
        2.96,
        2.81,
        2.78,
        2.65,
        2.58,
        2.46,
        2.28,
        2.10,
        2.01
    ]
})


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "By Subjective Social Class",
    "By Income",
    "By Region",
    "By Age",
    "By Migration Background"
])


with tab1:

    st.subheader("Subjective Social Class")

    fig = px.bar(
        class_df,
        x="Subjective Social Class",
        y="Left Behind Index",
        text="Left Behind Index",
        title="Left Behind Index by Subjective Social Class"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        yaxis=dict(range=[0, 4])
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.success("""
People who place themselves in a lower subjective social class report
a much stronger sense of being left behind, with a clear, steady gradient
from the lowest to the highest class category.
""")


with tab2:

    st.subheader("Household Income")

    fig = px.bar(
        income_df,
        x="Income group",
        y="Left Behind Index",
        text="Left Behind Index",
        title="Left Behind Index by Household Net Monthly Income"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=460,
        yaxis=dict(range=[0, 4]),
        xaxis=dict(tickangle=-40)
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.success("""
A similar gradient appears for income: respondents in lower income
groups report higher Left Behind scores, decreasing fairly steadily
toward higher income groups.
""")


with tab3:

    st.subheader("East vs. West Germany")

    fig = px.bar(
        region_df,
        x="Region",
        y="Left Behind Index",
        text="Left Behind Index",
        title="Left Behind Index by Region"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        yaxis=dict(range=[0, 3.2])
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.info("""
Respondents in **East Germany** report a higher average Left Behind
score than respondents in **West Germany** in this descriptive comparison.

These are unadjusted group averages, so the difference should not be
interpreted as a causal effect of region. It provides a reason to examine
what lies behind the East-West gap more closely.
""")


with tab4:

    st.subheader("Age Group")

    fig = px.bar(
        age_df,
        x="Age group",
        y="Left Behind Index",
        text="Left Behind Index",
        title="Left Behind Index by Age Group"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        yaxis=dict(range=[0, 3.2])
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.info("""
Differences across age groups are small.

Feeling Left Behind does not appear to be primarily a
generational phenomenon in this sample.
""")


with tab5:

    st.subheader("Migration Background")

    fig = px.bar(
        migration_df,
        x="Migration background",
        y="Left Behind Index",
        text="Left Behind Index",
        title="Left Behind Index by Migration Background"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        yaxis=dict(range=[0, 3.2])
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.info("""
Respondents with a migration background report a slightly higher
average score, but the difference is modest compared with the
gradients seen for Subjective Social Class and income.
""")


st.caption("""
Figures are simple group averages of the Left Behind Index,
calculated after removing non-response codes for each demographic
variable.

Subjective Social Class is shown here as a **descriptive comparison**.
It is not a separate regression stage in the final two-model design.

GLES variables: ostwest, age, migration_background,
d38 (Subjective Social Class), and d63 (household net monthly income).
""")

st.divider()


# ============================================================
# WHAT THE INDEX DOES NOT MEAN
# ============================================================

st.header("What the index does and does not tell us")

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
