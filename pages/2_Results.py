import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Results")

# ============================================================
# DATA
# ============================================================

comparison = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Model 1": [0.088, 0.085, 0.039],
    "Model 2": [0.107, 0.096, 0.039],
    "Model 3": [0.276, 0.222, 0.053]
})

standardized_results = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Left Behind β": [-0.459, 0.395, 0.128]
})

# ============================================================
# INTRODUCTION
# ============================================================

st.markdown("""
## What did we find?

People who feel more **left behind** tend to have:

- **lower trust in institutions**;
- **lower satisfaction with how democracy works in Germany**;
- and, to a much smaller extent, **a lower sense of being represented
  by a political party**.

These relationships remain after accounting for income, education, age,
East/West Germany, migration background, political interest and
Subjective Social Class.
""")

st.success("""
### Main takeaway

Feeling Left Behind adds substantial explanatory power for
**Institutional Trust** and **Democratic Satisfaction**, but much less
for **Party Representation**.
""")

st.divider()

# ============================================================
# QUICK RESULT
# ============================================================

st.header("The result in one view")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
### 🏛️ Institutional Trust

**10.7% → 27.6%**

**+16.9 percentage points**
""")

with c2:
    st.markdown("""
### 🗳️ Democratic Satisfaction

**9.6% → 22.2%**

**+12.6 percentage points**
""")

with c3:
    st.markdown("""
### 👥 Party Representation

**3.9% → 5.3%**

**+1.4 percentage points**
""")

st.info("""
These percentages show how much of the differences between respondents
the statistical models can explain.

The key comparison is how much the percentage increases when
**Feeling Left Behind is added**.
""")

st.divider()

# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Left Behind Index",
    "Institutional Trust",
    "Democratic Satisfaction",
    "Party Representation"
])

# ============================================================
# OVERVIEW
# ============================================================

with tab1:

    st.header("Understanding the results")

    st.subheader("What does Feeling Left Behind mean?")

    st.markdown("""
Feeling Left Behind does **not simply mean having a low income**.

It captures whether people feel that people like them are:

- economically overlooked;
- socially unrecognized;
- underserved by basic infrastructure and services;
- constrained in expressing their views publicly.
""")

    st.info("""
Open the **Left Behind Index** tab for the four exact survey questions,
response scale and construction of the index.
""")

    st.divider()

    st.subheader("Why are there three models?")

    st.markdown("""
The variables are added in stages so that we can see whether Feeling
Left Behind contributes information beyond socioeconomic characteristics.
""")

    st.info("""
**Model 1 — Traditional characteristics**

Income, education, age, East/West Germany, migration background and
political interest.

**Model 2 — + Subjective Social Class**

Adds how respondents perceive their own position in society.

**Model 3 — + Left Behind Index**

Adds the subjective experience of Feeling Left Behind.
""")

    st.dataframe(
        comparison.style.format({
            "Model 1": "{:.1%}",
            "Model 2": "{:.1%}",
            "Model 3": "{:.1%}"
        }),
        hide_index=True,
        width="stretch"
    )

    chart_data = comparison.melt(
        id_vars="Outcome",
        var_name="Model",
        value_name="R²"
    )

    fig = px.bar(
        chart_data,
        x="Outcome",
        y="R²",
        color="Model",
        barmode="group",
        text="R²",
        title="How Much of Each Outcome Can the Models Explain?",
        color_discrete_map={
            "Model 1": "#1f77b4",
            "Model 2": "#ff7f0e",
            "Model 3": "#2ca02c"
        }
    )

    fig.update_traces(
        texttemplate="%{text:.1%}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "%{fullData.name}<br>"
            "Variation explained: %{y:.1%}<extra></extra>"
        )
    )

    fig.update_layout(
        height=550,
        xaxis_title="",
        yaxis_title="Variation explained",
        legend_title="",
        yaxis=dict(
            range=[0, 0.35],
            tickformat=".0%"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.success("""
### What does this graph tell us?

Adding Subjective Social Class changes the models relatively little.

The much larger change happens when **Feeling Left Behind** is added:

- Institutional Trust: **10.7% → 27.6%**
- Democratic Satisfaction: **9.6% → 22.2%**
- Party Representation: **3.9% → 5.3%**

Feeling Left Behind therefore appears particularly relevant to
**trust and satisfaction with democracy**.
""")

    with st.expander("Technical evidence: standardized coefficients"):

        beta_fig = px.bar(
            standardized_results,
            x="Outcome",
            y="Left Behind β",
            text="Left Behind β",
            title="Standardized Association of the Left Behind Index"
        )

        beta_fig.update_traces(
            texttemplate="%{text:.3f}",
            textposition="outside"
        )

        beta_fig.add_hline(
            y=0,
            line_width=1
        )

        beta_fig.update_layout(
            height=480,
            xaxis_title="",
            yaxis_title="Standardized coefficient (β)",
            yaxis=dict(range=[-0.55, 0.5])
        )

        st.plotly_chart(
            beta_fig,
            width="stretch"
        )

# ============================================================
# LEFT BEHIND INDEX
# ============================================================

with tab2:

    st.header("🧩 Left Behind Index")

    st.markdown("""
## What does “Feeling Left Behind” mean?

The central idea of this project is that people's democratic attitudes
may depend not only on their objective socioeconomic position, but also
on whether they **feel overlooked, unrecognized or excluded by society**.

This is a **subjective perception**.

It is not the same thing as poverty, income or social class.
""")

    st.divider()

    st.subheader("The four survey questions")

    st.markdown("""
Respondents were asked:

> **“To what extent do you agree with the following statements or not?”**
""")

    st.info("""
### 1. Economic attention — q46a

**“The economic situation of people like me receives too little attention
from society.”**

This captures whether respondents feel that the economic concerns of
people like them are being overlooked.
""")

    st.info("""
### 2. Social recognition — q46b

**“People like me receive too little recognition from society for the
work they do.”**

This captures whether respondents feel that their contribution to society
is sufficiently recognized.
""")

    st.info("""
### 3. Infrastructure and basic services — q46c

**“Society pays too little attention to ensuring that people like me
have access to basic infrastructures and services.”**

Examples in the questionnaire include:

- post offices;
- doctors;
- banks;
- public transportation;
- schools;
- Internet access.
""")

    st.info("""
### 4. Freedom of expression — q46d

**“People like me are no longer allowed to freely express their opinions
in public.”**

This captures perceived constraints on expressing one's views publicly.
""")

    st.divider()

    st.subheader("How were the answers scored?")

    st.markdown("""
The original questionnaire uses:

**1 = Strongly agree**  
**2 = Agree**  
**3 = Neither agree nor disagree**  
**4 = Disagree**  
**5 = Strongly disagree**

Agreement represents a stronger feeling of being left behind.

To make the final index easier to understand, the scale was therefore
**reversed**.
""")

    st.code(
        "reversed_score = 6 - original_score",
        language="python"
    )

    st.markdown("""
After reversing:

**1 = lower feeling of being left behind**

**5 = higher feeling of being left behind**

So:

### Higher Left Behind Index = stronger feeling of being left behind
""")

    st.divider()

    st.subheader("How is the final score calculated?")

    st.markdown("""
For every respondent, the four reversed answers are averaged:

**Economic attention**

+

**Social recognition**

+

**Infrastructure and services**

+

**Freedom of expression**

→ **Average**

→ **Left Behind Index**
""")

    st.divider()

    st.subheader("Why is this different from income?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
### Income

How much economic resources a household has.

This is an **objective socioeconomic measure**.
""")

    with col2:
        st.markdown("""
### Subjective Social Class

Where people believe they sit in the social hierarchy.

This measures **perceived social position**.
""")

    with col3:
        st.markdown("""
### Feeling Left Behind

Whether people feel that people like them receive attention,
recognition, services and space to express themselves.

This measures **subjective social disconnection**.
""")

    st.success("""
### This distinction is central to the research

Two people with similar income and education may feel very differently
about whether society recognizes or pays attention to people like them.

The analysis tests whether those differences are connected to democratic
attitudes.
""")

    st.divider()

    st.subheader("Can the four questions be combined?")

    st.markdown("""
The analysis tested whether the four questions behave consistently enough
to represent one underlying concept.

Results:

- **Cronbach's α = 0.753**
- **First-factor eigenvalue = 2.323**
- clear one-factor structure

These results support combining the four items into one Left Behind Index.
""")

    with st.expander("What does Cronbach's α = 0.753 mean?"):

        st.markdown("""
Cronbach's alpha measures whether several questions tend to measure a
related underlying concept.

A value of **0.753** indicates acceptable internal consistency.

In practical terms, the four questions are sufficiently related to be
summarized into one index, while still capturing different aspects of
Feeling Left Behind.
""")

    st.warning("""
The index measures respondents' **perceptions**.

It does not establish whether society objectively provides too little
attention, recognition, infrastructure or freedom of expression to a
particular respondent.
""")

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab3:

    st.header("🏛️ Institutional Trust")

    st.markdown("""
### In simple terms

**Do people trust important institutions?**
""")

    st.subheader("What was actually asked?")

    st.markdown("""
Respondents were asked how much they personally trust several institutions
and groups.

The analysis uses eight:
""")

    st.info("""
- Federal Government
- Bundestag
- Political Parties
- Politicians
- Police
- Justice
- Science
- Public-Service Broadcasting
""")

    st.markdown("""
Each is rated from:

**1 = Do not trust at all**

to

**11 = Trust completely**

The eight answers are averaged into the **Institutional Trust Index**.
""")

    st.caption(
        "GLES variables used: q79a–q79g and q79i."
    )

    st.divider()

    st.success("""
## People who feel more left behind tend to trust institutions substantially less.
""")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Before adding Feeling Left Behind",
            "10.7%"
        )

    with c2:
        st.metric(
            "After adding Feeling Left Behind",
            "27.6%",
            delta="+16.9 percentage points"
        )

    st.markdown("""
The model's explanatory power increases dramatically when Feeling Left
Behind is added.

The relationship remains after accounting for income, education, age,
region, migration background, political interest and Subjective Social Class.

**Household Income is not statistically significant in the final model.**
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "27.6%")
        c2.metric("Standardized β", "−0.459")
        c3.metric("Significance", "p < .001")

    st.info("""
This is an association. The analysis does not demonstrate that Feeling
Left Behind causes lower institutional trust.
""")

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab4:

    st.header("🗳️ Democratic Satisfaction")

    st.markdown("""
### In simple terms

**Are people satisfied with how democracy works in Germany?**
""")

    st.subheader("What was actually asked?")

    st.markdown("""
Respondents were asked:

> **“How satisfied are you with the way democracy works in Germany?”**
""")

    st.info("""
**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.markdown("""
Higher values therefore mean **greater dissatisfaction**.
""")

    st.caption(
        "GLES variable: q119."
    )

    st.divider()

    st.success("""
## People who feel more left behind tend to be less satisfied with how democracy works.
""")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Before adding Feeling Left Behind",
            "9.6%"
        )

    with c2:
        st.metric(
            "After adding Feeling Left Behind",
            "22.2%",
            delta="+12.6 percentage points"
        )

    st.markdown("""
Adding Subjective Social Class raises explanatory power only from
**8.5% to 9.6%**.

Adding Feeling Left Behind raises it from **9.6% to 22.2%**.

This suggests that perceived social disconnection captures information
about democratic dissatisfaction that socioeconomic position alone does not.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "22.2%")
        c2.metric("Standardized β", "0.395")
        c3.metric("Significance", "p < .001")

        st.markdown("""
The coefficient is positive because higher values of q119 represent
**greater dissatisfaction**.
""")

# ============================================================
# PARTY REPRESENTATION
# ============================================================

with tab5:

    st.header("👥 Party Representation")

    st.markdown("""
### In simple terms

**Do people feel that a political party represents their views?**
""")

    st.subheader("What was actually asked?")

    st.markdown("""
Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**
""")

    st.info("""
**1 = Yes**

**2 = No**
""")

    st.caption(
        "GLES variable: q141."
    )

    st.divider()

    st.success("""
## Feeling Left Behind is related to lower perceived party representation,
## but the relationship is much weaker.
""")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Before adding Feeling Left Behind",
            "3.9%"
        )

    with c2:
        st.metric(
            "After adding Feeling Left Behind",
            "5.3%",
            delta="+1.4 percentage points"
        )

    st.markdown("""
Compare the increases:

- Institutional Trust: **+16.9 percentage points**
- Democratic Satisfaction: **+12.6 percentage points**
- Party Representation: **+1.4 percentage points**

Political Interest is the strongest predictor in this model.

This suggests that Feeling Left Behind is **not a general explanation for
every form of democratic disconnection**.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "5.3%")
        c2.metric("Standardized β", "0.128")
        c3.metric("Significance", "p < .001")

# ============================================================
# BIG PICTURE
# ============================================================

st.divider()

st.header("What does this tell us?")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
### Economic position is not the whole story

Democratic attitudes are connected not only to material circumstances,
but also to people's perceptions of recognition and social inclusion.
""")

with c2:
    st.markdown("""
### Feeling Left Behind is not simply social class

Subjective Social Class adds relatively little explanatory power.

The Left Behind Index adds much more.
""")

with c3:
    st.markdown("""
### Democratic disconnection has different dimensions

Feeling Left Behind is closely related to trust and satisfaction,
but only weakly to Party Representation.
""")

st.warning("""
The data are cross-sectional.

The analysis identifies relationships between variables but cannot
demonstrate that Feeling Left Behind causes changes in democratic attitudes.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Left Behind Index: q46a–q46d  
Institutional Trust: q79a–q79g and q79i  
Democratic Satisfaction: q119  
Party Representation: q141
""")