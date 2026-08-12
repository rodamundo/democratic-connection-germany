import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 Results")


# ============================================================
# HELPER
# ============================================================

def puzzle_visual(explained, label, value, total=100):

    filled = round(explained)
    empty = total - filled

    squares = (
        "<span style='color:#2E86DE;'>■</span>" * filled +
        "<span style='color:#D9D9D9;'>■</span>" * empty
    )

    st.markdown(
        f"""
        <div style="
            border:1px solid #dddddd;
            border-radius:12px;
            padding:18px;
            margin-bottom:12px;
        ">
            <div style="font-size:19px;font-weight:700;margin-bottom:6px;">
                {label}
            </div>

            <div style="
                font-size:20px;
                line-height:1.25;
                letter-spacing:2px;
                word-break:break-all;
                margin-bottom:10px;
            ">
                {squares}
            </div>

            <div style="font-size:18px;font-weight:700;">
                ≈ {round(explained)} of 100 pieces
            </div>

            <div style="font-size:14px;color:#777777;">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DATA
# ============================================================

ols_data = pd.DataFrame({
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


party_data = pd.DataFrame({
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
# INTRO
# ============================================================

st.header("What are we trying to explain?")

st.markdown("""
The analysis starts with a very simple question:

> ### Why do people give different answers about democracy?
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Trust")

        st.markdown("""
People have different **Institutional Trust scores**.

Some are low.

Some are high.

The model tries to understand why.
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Satisfaction")

        st.markdown("""
People give different answers about how satisfied they are
with democracy.

The model tries to understand why.
""")

with c3:
    with st.container(border=True):

        st.markdown("### 👥 Representation")

        st.markdown("""
People answer:

**Yes / No**

to whether a party represents their views.
""")

st.info("""
For Trust and Democratic Satisfaction, we are **not deciding who trusts
and who does not**.

We are looking at the full range of answers and trying to understand
why they differ from person to person.
""")

st.divider()


# ============================================================
# PUZZLE INTRO
# ============================================================

st.header("Think of the differences as a puzzle")

st.markdown("""
Take **Institutional Trust**.

Imagine all the differences in trust scores between the 5,039 respondents
as a puzzle made of **100 pieces**.

### 🧩 100 pieces = all observed differences in trust scores

The models try to account for some of those differences.
""")


# ============================================================
# PUZZLES
# ============================================================

puzzle_visual(
    8.8,
    "Model 1 — Income, education, age, region, migration and political interest",
    "R² = 8.8%"
)

st.markdown("""
Traditional information helps us understand roughly:

### **9 of every 100 pieces**
""")

puzzle_visual(
    10.7,
    "Model 2 — + Subjective Social Class",
    "R² = 10.7%"
)

st.markdown("""
Adding Subjective Social Class adds only a little:

### **about 11 of every 100 pieces**
""")

puzzle_visual(
    27.6,
    "Model 3 — + Feeling Left Behind",
    "R² = 27.6%"
)

st.success("""
### This is the important jump

After Feeling Left Behind is added, the complete model can account for
approximately:

# **28 of every 100 pieces**

of the observed differences in Institutional Trust scores.

The remaining roughly **72 pieces** are not accounted for by the
variables in this model.
""")

st.caption("""
The puzzle is a visual analogy.

R² is technically the share of observed variation in the outcome
accounted for by the model. The pieces do not represent individual causes.
""")

st.divider()


# ============================================================
# CLARIFICATION
# ============================================================

st.header("What 27.6% does — and does not — mean")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### ❌ It does not mean")

        st.markdown("""
- 27.6% of people trust institutions
- trust increased by 27.6%
- Feeling Left Behind alone explains 27.6%
- 27.6% of the causes of distrust were discovered
""")

with c2:
    with st.container(border=True):

        st.markdown("### ✅ It means")

        st.markdown("""
The **complete Model 3** can statistically account for **27.6% of the
observed differences in Institutional Trust scores between respondents**.
""")

st.divider()


# ============================================================
# TWO OLS OUTCOMES
# ============================================================

st.header("Does the pattern also appear for Democratic Satisfaction?")

chart_data = ols_data.melt(
    id_vars="Outcome",
    var_name="Model",
    value_name="Share"
)

fig = px.bar(
    chart_data,
    x="Outcome",
    y="Share",
    color="Model",
    barmode="group",
    text="Share",
    title="How Much of the Observed Differences Can Each Model Account For?"
)

fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside"
)

fig.update_layout(
    height=520,
    xaxis_title="",
    yaxis_title="Share of observed differences accounted for",
    legend_title="",
    yaxis=dict(
        range=[0, 0.35],
        tickformat=".0%"
    )
)

st.plotly_chart(fig, width="stretch")

st.markdown("""
### Institutional Trust

**8.8% → 10.7% → 27.6%**

### Democratic Satisfaction

**8.5% → 9.6% → 22.2%**
""")

st.success("""
The pattern is similar:

**Subjective Social Class adds relatively little.**

**Feeling Left Behind adds substantially more information.**
""")

st.divider()


# ============================================================
# DIRECT GAINS
# ============================================================

st.header("How much does Feeling Left Behind add to the existing model?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.metric(
            "Before Feeling Left Behind",
            "10.7%"
        )

        st.metric(
            "After Feeling Left Behind",
            "27.6%"
        )

        st.metric(
            "Gain",
            "+16.9 percentage points"
        )

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.metric(
            "Before Feeling Left Behind",
            "9.6%"
        )

        st.metric(
            "After Feeling Left Behind",
            "22.2%"
        )

        st.metric(
            "Gain",
            "+12.6 percentage points"
        )

st.info("""
These gains show how much **R² increases when Feeling Left Behind is
added to a model that already contains the other variables**.

They should not be interpreted as Feeling Left Behind acting alone.
""")

st.divider()


# ============================================================
# PARTY REPRESENTATION
# ============================================================

st.header("Party Representation is a different type of question")

st.markdown("""
Here respondents answer:

# **Yes / No**

So the analysis uses **logistic regression**.

Its model-fit statistic is **McFadden Pseudo R²**, not the same R²
used for Trust and Democratic Satisfaction.
""")

party_fig = px.bar(
    party_data,
    x="Model",
    y="Pseudo R²",
    text="Pseudo R²",
    title="Party Representation — Model Fit"
)

party_fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside"
)

party_fig.update_layout(
    height=430,
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
### Do not use the 100-piece puzzle literally for this outcome.

Pseudo R² does not have the same interpretation as OLS R².

The useful comparison is **within the Party Representation models**:

**3.4% → 3.4% → 4.6%**

The improvement after Feeling Left Behind is much smaller.
""")

st.divider()


# ============================================================
# DETAILED TABS
# ============================================================

tab1, tab2, tab3 = st.tabs([
    "Institutional Trust",
    "Democratic Satisfaction",
    "Party Representation"
])


# ============================================================
# TRUST
# ============================================================

with tab1:

    st.header("🏛️ Institutional Trust")

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
The eight answers are averaged into one score.

There is no threshold for “trusting” versus “not trusting”.
""")

    st.success("""
### Finding

As Feeling Left Behind scores increase,
Institutional Trust tends to decrease.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "27.6%")
        c2.metric("Standardized β", "−0.459")
        c3.metric("p-value", "< .001")

        st.caption("""
OLS regression with HC3 robust standard errors.
""")


# ============================================================
# SATISFACTION
# ============================================================

with tab2:

    st.header("🗳️ Democratic Satisfaction")

    st.markdown("""
Respondents answered:

**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.info("""
The full 1–4 scale is used.

There is no binary cut-off between satisfied and dissatisfied.
""")

    st.success("""
### Finding

As Feeling Left Behind scores increase,
democratic dissatisfaction also tends to increase.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "22.2%")
        c2.metric("Standardized β", "0.395")
        c3.metric("p-value", "< .001")

        st.caption("""
OLS regression with HC3 robust standard errors.

The positive coefficient reflects the coding:
higher outcome values mean greater dissatisfaction.
""")


# ============================================================
# PARTY
# ============================================================

with tab3:

    st.header("👥 Party Representation")

    st.markdown("""
Respondents were asked:

> **Does any political party represent your political views well?**

**Yes / No**
""")

    st.success("""
### Finding

Higher Feeling Left Behind scores are associated with lower odds
of saying that a political party represents the respondent's views well.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final Pseudo R²", "4.6%")
        c2.metric("Logit coefficient", "−0.348")
        c3.metric("p-value", "< .001")

        st.markdown("""
**Odds ratio: 0.706**

Holding the other variables constant, each one-point increase in the
Left Behind Index is associated with approximately **29% lower odds**
of saying that a party represents the respondent's views well.
""")


# ============================================================
# FINAL
# ============================================================

st.divider()

st.header("The main message")

st.success("""
### Feeling Left Behind does not complete the puzzle.

But for Institutional Trust and Democratic Satisfaction,
it adds substantially more information than income,
education and Subjective Social Class alone.
""")

st.markdown("""
> ## What people have matters.
>
> ## How people feel seen, recognized, served and heard may matter too.
""")

st.warning("""
The analysis shows **associations, not causation**.

The direction of the relationship cannot be established from
cross-sectional data.
""")

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")