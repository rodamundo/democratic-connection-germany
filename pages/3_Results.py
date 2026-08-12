import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.title("📊 Results")


# ============================================================
# DATA
# ============================================================

ols_comparison = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction"
    ],
    "Traditional Factors": [
        0.088,
        0.085
    ],
    "+ Social Class": [
        0.107,
        0.096
    ],
    "+ Feeling Left Behind": [
        0.276,
        0.222
    ]
})


party_comparison = pd.DataFrame({
    "Model": [
        "Traditional Factors",
        "+ Social Class",
        "+ Feeling Left Behind"
    ],
    "Pseudo R²": [
        0.0337,
        0.0343,
        0.0462
    ]
})


# ============================================================
# INTRODUCTION
# ============================================================

st.header("What did this project test?")

st.markdown("""
The GLES already contains information about respondents' income,
education, social position and democratic attitudes.

It also includes four questions about whether people feel economically
overlooked, socially unrecognized, underserved and unable to freely
express themselves.

This project combines those four questions into a validated
**Left Behind Index** and asks:

> ### Does knowing how left behind someone feels help us understand
> ### democratic attitudes beyond traditional socioeconomic factors?
""")

st.divider()


# ============================================================
# WHAT IS BEING EXPLAINED?
# ============================================================

st.header("First: what exactly are the models trying to explain?")

st.markdown("""
The answer is different depending on the outcome.
""")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Every respondent receives a **trust score** based on ratings
of eight institutions.

The score can take many different values.

The model asks:

> **Why do people's trust scores differ?**
""")

with c2:

    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
Every respondent answers on a scale from:

**1 = Very satisfied**

to

**4 = Not at all satisfied**

The model asks:

> **Why do people's satisfaction responses differ?**
""")

with c3:

    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
This outcome is different.

Respondents answer:

**Yes / No**

The model asks:

> **What is associated with whether someone feels represented?**
""")

st.info("""
### Important

For Institutional Trust and Democratic Satisfaction, there is **no
classification into people who trust / do not trust** or people who are
satisfied / dissatisfied.

The analysis uses the full range of responses.

Party Representation is the only Yes/No outcome.
""")

st.divider()


# ============================================================
# EXPLAIN R2
# ============================================================

st.header("What does an R² percentage mean?")

st.markdown("""
Take **Institutional Trust** as an example.

The 5,039 respondents have different trust scores.

Imagine that:

# **100% = all the observed differences in trust scores between respondents**

The models try to account for those differences using the information
we know about each person.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("### ❌ 27.6% does NOT mean")

        st.markdown("""
- 27.6% of respondents trust institutions
- trust increased by 27.6%
- Feeling Left Behind alone explains 27.6%
""")

with c2:

    with st.container(border=True):

        st.markdown("### ✅ 27.6% DOES mean")

        st.markdown("""
The **complete final model** can statistically account for:

# **27.6%**

of the observed differences in Institutional Trust scores
between respondents.
""")

st.markdown("""
For Institutional Trust:

**Model 1 → 8.8%**

**Model 2 → 10.7%**

**Model 3 → 27.6%**

The remaining **72.4%** of the differences are not accounted for
by the variables included in Model 3.
""")

st.divider()


# ============================================================
# OLS RESULTS
# ============================================================

st.header(
    "How much of the differences between respondents can the models account for?"
)

st.markdown("""
The chart below includes **only Institutional Trust and Democratic Satisfaction**.

Both use OLS regression and R², so their percentages have the same
general interpretation:

> **100% = all observed differences between respondents in that outcome.**
""")

ols_long = ols_comparison.melt(
    id_vars="Outcome",
    var_name="Model",
    value_name="R²"
)

fig = px.bar(
    ols_long,
    x="Outcome",
    y="R²",
    color="Model",
    barmode="group",
    text="R²",
    title="Share of Observed Differences Accounted for by Each Model"
)

fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside",
    hovertemplate=(
        "<b>%{x}</b><br>"
        "%{fullData.name}<br>"
        "R²: %{y:.1%}"
        "<extra></extra>"
    )
)

fig.update_layout(
    height=540,
    xaxis_title="",
    yaxis_title="Share of observed differences accounted for",
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

st.caption("""
For each outcome, 100% represents all observed variation between respondents.
R² shows what share of that variation the model can statistically account for.
""")

st.success("""
### What should you notice?

For **Institutional Trust**:

**8.8% → 10.7% → 27.6%**

For **Democratic Satisfaction**:

**8.5% → 9.6% → 22.2%**

Adding Subjective Social Class produces only a small improvement.

The much larger change comes when **Feeling Left Behind** is added.
""")

st.divider()


# ============================================================
# SHOW THE GAIN ITSELF
# ============================================================

st.header("How much does Feeling Left Behind add?")

gain_df = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction"
    ],
    "Before Feeling Left Behind": [
        0.107,
        0.096
    ],
    "After Feeling Left Behind": [
        0.276,
        0.222
    ],
    "Gain": [
        0.169,
        0.126
    ]
})


c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.metric(
            "Before",
            "10.7%"
        )

        st.metric(
            "After",
            "27.6%"
        )

        st.metric(
            "Additional explanatory power",
            "+16.9 percentage points"
        )


with c2:

    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.metric(
            "Before",
            "9.6%"
        )

        st.metric(
            "After",
            "22.2%"
        )

        st.metric(
            "Additional explanatory power",
            "+12.6 percentage points"
        )


st.info("""
The **16.9 and 12.6 percentage-point gains** are the clearest way to describe
what changes when Feeling Left Behind is added.

They do **not** mean that Feeling Left Behind by itself explains exactly
16.9% or 12.6% of the outcome.

They mean that adding it to the existing model increases R² by that amount.
""")

st.divider()


# ============================================================
# PARTY REPRESENTATION
# ============================================================

st.header("Party Representation must be read separately")

st.markdown("""
Party Representation is a **Yes/No outcome**.

Because of this, the analysis uses **logistic regression** rather than OLS.

Its model fit is measured with **McFadden Pseudo R²**.

This is why Party Representation should not appear on the same R² chart
as Institutional Trust and Democratic Satisfaction.
""")

party_fig = px.bar(
    party_comparison,
    x="Model",
    y="Pseudo R²",
    text="Pseudo R²",
    title="Party Representation: McFadden Pseudo R²"
)

party_fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside"
)

party_fig.update_layout(
    height=450,
    xaxis_title="",
    yaxis_title="McFadden Pseudo R²",
    yaxis=dict(
        range=[0, 0.06],
        tickformat=".0%"
    )
)

st.plotly_chart(
    party_fig,
    width="stretch"
)

st.warning("""
### Do not interpret 4.6% as “4.6% of representation explained”

Pseudo R² is a different measure of model fit.

The important conclusion is the **relative change within this model**:

**3.4% → 3.4% → 4.6%**

Feeling Left Behind improves the Party Representation model,
but much less than it improves the two OLS models.
""")

st.divider()


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3 = st.tabs([
    "Institutional Trust",
    "Democratic Satisfaction",
    "Party Representation"
])


# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab1:

    st.header("🏛️ Institutional Trust")

    st.subheader("How is trust measured?")

    st.markdown("""
Respondents rated eight institutions from:

**1 = Do not trust at all**

to

**11 = Trust completely**
""")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
- Federal Government
- Bundestag
- Political Parties
- Politicians
""")

    with c2:

        st.markdown("""
- Police
- Justice
- Science
- Public-Service Broadcasting
""")

    st.info("""
The eight answers are averaged into one Institutional Trust score.

There is **no cut-off** saying that someone “trusts” or “does not trust”.

People simply have different trust scores.
""")

    st.divider()

    st.success("""
### Main finding

People with higher Feeling Left Behind scores tend to report
lower Institutional Trust.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Model 1",
        "8.8%"
    )

    c2.metric(
        "Model 2",
        "10.7%"
    )

    c3.metric(
        "Model 3",
        "27.6%"
    )

    st.markdown("""
### How to read this

Imagine all differences in trust scores between respondents = **100%**.

Model 1 accounts for **8.8%** of those differences.

After Subjective Social Class is added, Model 2 accounts for **10.7%**.

After Feeling Left Behind is added, Model 3 accounts for **27.6%**.

So Feeling Left Behind increases the model's explanatory power by:

# **+16.9 percentage points**
""")

    st.info("""
Household Income is not statistically significant in the final model.

Feeling Left Behind remains strongly associated with Institutional Trust.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final R²",
            "27.6%"
        )

        c2.metric(
            "Standardized β",
            "−0.459"
        )

        c3.metric(
            "p-value",
            "< .001"
        )

        st.caption("""
Method: OLS regression with HC3 robust standard errors.

Higher Feeling Left Behind scores are associated with lower
Institutional Trust.
""")


# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab2:

    st.header("🗳️ Democratic Satisfaction")

    st.subheader("How is satisfaction measured?")

    st.markdown("""
Respondents answered:

> **“How satisfied are you with the way democracy works in Germany?”**
""")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "1",
        "Very satisfied"
    )

    c2.metric(
        "2",
        "Fairly satisfied"
    )

    c3.metric(
        "3",
        "Not very satisfied"
    )

    c4.metric(
        "4",
        "Not at all satisfied"
    )

    st.info("""
There is no binary division into “satisfied” and “not satisfied”.

The analysis uses the complete 1–4 response scale.

Higher values mean greater dissatisfaction.
""")

    st.divider()

    st.success("""
### Main finding

People with higher Feeling Left Behind scores tend to report
greater dissatisfaction with how democracy works.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Model 1",
        "8.5%"
    )

    c2.metric(
        "Model 2",
        "9.6%"
    )

    c3.metric(
        "Model 3",
        "22.2%"
    )

    st.markdown("""
### How to read this

Imagine all observed differences in Democratic Satisfaction responses
between respondents = **100%**.

Model 1 accounts for **8.5%**.

Model 2 accounts for **9.6%**.

Model 3 accounts for **22.2%**.

Adding Feeling Left Behind therefore increases R² by:

# **+12.6 percentage points**
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final R²",
            "22.2%"
        )

        c2.metric(
            "Standardized β",
            "0.395"
        )

        c3.metric(
            "p-value",
            "< .001"
        )

        st.caption("""
Method: OLS regression with HC3 robust standard errors.

The coefficient is positive because higher values on the original
Democratic Satisfaction scale mean greater dissatisfaction.
""")


# ============================================================
# PARTY REPRESENTATION
# ============================================================

with tab3:

    st.header("👥 Party Representation")

    st.subheader("How is representation measured?")

    st.markdown("""
Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**
""")

    c1, c2 = st.columns(2)

    c1.metric(
        "1",
        "Yes"
    )

    c2.metric(
        "2",
        "No"
    )

    st.info("""
This outcome really is binary.

Because the answer is Yes/No, it is analyzed with
**logistic regression**.
""")

    st.divider()

    st.success("""
### Main finding

Higher Feeling Left Behind scores are associated with lower odds
of saying that a political party represents the respondent's views well.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Traditional Factors",
        "3.4%"
    )

    c2.metric(
        "+ Social Class",
        "3.4%"
    )

    c3.metric(
        "+ Feeling Left Behind",
        "4.6%"
    )

    st.warning("""
These are **McFadden Pseudo R² values**.

Do not interpret them as percentages of differences explained
and do not compare them numerically with the R² values from
Institutional Trust and Democratic Satisfaction.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final Pseudo R²",
            "4.6%"
        )

        c2.metric(
            "Logit coefficient",
            "−0.348"
        )

        c3.metric(
            "p-value",
            "< .001"
        )

        st.markdown("""
**Odds ratio: 0.706**

Holding the other variables constant, each one-point increase
in the Left Behind Index is associated with approximately
**29% lower odds** of saying that a political party represents
the respondent's views well.
""")


# ============================================================
# FINAL TAKEAWAYS
# ============================================================

st.divider()

st.header("So what did the analysis find?")

with st.container(border=True):

    st.markdown("""
### 1. Traditional factors explain only part of the differences

Income, education, age, region, migration background and political
interest provide useful information, but leave most differences unexplained.
""")


with st.container(border=True):

    st.markdown("""
### 2. Subjective Social Class adds relatively little

For Institutional Trust:

**8.8% → 10.7%**

For Democratic Satisfaction:

**8.5% → 9.6%**
""")


with st.container(border=True):

    st.markdown("""
### 3. Feeling Left Behind adds much more information

For Institutional Trust:

**10.7% → 27.6%**

For Democratic Satisfaction:

**9.6% → 22.2%**
""")


with st.container(border=True):

    st.markdown("""
### 4. Party Representation behaves differently

Feeling Left Behind is still associated with representation,
but the improvement in model fit is much smaller.

This suggests that democratic disconnection has different dimensions.
""")


st.warning("""
### What this analysis does not show

These are statistical associations.

The data do not establish that Feeling Left Behind causes lower trust
or democratic dissatisfaction.

Reverse causality is also possible.
""")


st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")