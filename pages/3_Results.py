import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.title("📊 Results")


# ============================================================
# HELPERS — VISUAL EXPLAINERS FOR "MODEL FIT" / R²
# ============================================================

def build_gap_chart():
    """Illustrative scatter chart showing prediction 'gaps' shrinking
    when information is added. Uses synthetic data — NOT real GLES
    values — purely to teach the concept of model fit visually."""

    rng = np.random.default_rng(7)
    n = 22
    x = rng.uniform(1, 5, n)
    true_trend = 9 - 1.3 * x
    y = np.clip(true_trend + rng.normal(0, 1.1, n), 1, 11)
    mean_y = y.mean()
    coeffs = np.polyfit(x, y, 1)
    fit_y = np.polyval(coeffs, x)
    order = np.argsort(x)

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            "Guessing the same number for everyone",
            "Adjusting the guess per person"
        ),
        horizontal_spacing=0.12
    )

    for xi, yi in zip(x, y):
        fig.add_trace(go.Scatter(
            x=[xi, xi], y=[yi, mean_y], mode="lines",
            line=dict(color="#B7C1E0", width=1.5),
            showlegend=False, hoverinfo="skip"
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=sorted(x), y=[mean_y] * n, mode="lines",
        line=dict(color="#F96167", width=3), name="Model's guess"
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="markers",
        marker=dict(color="#1E2761", size=9), name="Actual person"
    ), row=1, col=1)

    for xi, yi, pi in zip(x, y, fit_y):
        fig.add_trace(go.Scatter(
            x=[xi, xi], y=[yi, pi], mode="lines",
            line=dict(color="#B7C1E0", width=1.5),
            showlegend=False, hoverinfo="skip"
        ), row=1, col=2)
    fig.add_trace(go.Scatter(
        x=x[order], y=fit_y[order], mode="lines",
        line=dict(color="#F96167", width=3),
        name="Model's guess", showlegend=False
    ), row=1, col=2)
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="markers",
        marker=dict(color="#1E2761", size=9),
        name="Actual person", showlegend=False
    ), row=1, col=2)

    fig.update_xaxes(title_text="Feeling Left Behind (illustrative)", row=1, col=1)
    fig.update_xaxes(title_text="Feeling Left Behind (illustrative)", row=1, col=2)
    fig.update_yaxes(title_text="Institutional Trust (1–11)", range=[0, 12], row=1, col=1)
    fig.update_yaxes(range=[0, 12], row=1, col=2)

    fig.update_layout(
        height=440,
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, x=0.28),
        margin=dict(t=50, b=70, l=10, r=10),
    )
    return fig


def build_donut(pct, label, color="#1E2761"):
    """Small donut showing the identified slice vs. the unknown
    remainder — the 'slice of the pizza' metaphor, made visual."""

    fig = go.Figure(data=[go.Pie(
        labels=["Accounted for", "Not captured by this model"],
        values=[pct, 100 - pct],
        hole=0.7,
        marker=dict(colors=[color, "#E7EAF4"]),
        textinfo="none",
        sort=False,
        direction="clockwise",
        hoverinfo="skip",
    )])
    fig.update_layout(
        showlegend=False,
        height=230,
        margin=dict(t=10, b=10, l=10, r=10),
        annotations=[dict(
            text=f"<b>{pct:.1f}%</b><br><span style='font-size:11px;color:#5B6B9C'>{label}</span>",
            x=0.5, y=0.5, font_size=22, showarrow=False, font_color="#1E2761"
        )],
    )
    return fig


# ============================================================
# DATA
# ============================================================

comparison = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Traditional Factors": [0.088, 0.085, 0.0337],
    "+ Social Class": [0.107, 0.096, 0.0343],
    "+ Feeling Left Behind": [0.276, 0.222, 0.0462]
})

gain_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Before Feeling Left Behind": [0.107, 0.096, 0.0337],
    "After Feeling Left Behind": [0.276, 0.222, 0.0462]
})


# ============================================================
# WHAT THIS PROJECT ADDS
# ============================================================

st.header("What did this project add?")

st.markdown("""
The **GLES 2025 survey already asks people** about their income,
education, social position and democratic attitudes.

It also asks four separate questions about whether people feel
economically overlooked, unrecognized, underserved and unable to
express themselves — but it does not combine them into a single
measure.

This project builds that missing measure — the **Left Behind Index** —
validates it statistically, and asks:

> ### If we already know someone's socioeconomic characteristics,
> ### does knowing **how left behind they feel** help us better understand
> ### their relationship with democracy?
""")

st.success("""
### The answer is yes, especially for Institutional Trust
### and Democratic Satisfaction.

Knowing how left behind people feel adds substantial information
beyond income, education, age, region, migration background,
political interest and Subjective Social Class.

For **Party Representation**, the additional contribution is much smaller.
""")

st.divider()


# ============================================================
# EXPLAIN R-SQUARED — VISUALLY
# ============================================================

st.header("Before looking at the numbers: what are we measuring?")

st.markdown("""
Imagine trying to guess how much each of the **5,039 respondents**
trusts institutions, using only what you know about them — their
income, age, how left behind they feel.

You won't guess perfectly. But some information helps more than others.
The chart below shows this with an illustrative example: the dots are
people, the red line is the model's guess, and the **gray lines are the
gaps** — how far off each guess is.
""")

st.plotly_chart(build_gap_chart(), width="stretch")

st.info("""
**This is the idea behind "model fit" (R²): it measures how much
smaller those gray gaps get** when information is added — from
guessing the same number for everyone, to adjusting the guess per
person.

*(The chart above uses illustrative, made-up numbers to explain the
concept — not real survey data. The real model uses 7 variables at
once, which can't be drawn on a simple 2D chart.)*
""")

st.markdown("""
Now here is what that looks like for the actual results. Each circle
below shows: of all the differences between real respondents, what
share can the final model (with Feeling Left Behind included) account for?
""")

d1, d2, d3 = st.columns(3)

with d1:
    st.plotly_chart(
        build_donut(27.6, "Institutional Trust"),
        width="stretch"
    )

with d2:
    st.plotly_chart(
        build_donut(22.2, "Democratic Satisfaction"),
        width="stretch"
    )

with d3:
    st.plotly_chart(
        build_donut(4.6, "Party Representation", color="#F96167"),
        width="stretch"
    )

st.caption("""
The colored slice is what the model accounts for. The gray slice is
everything else — reasons not captured by this survey (personality,
specific life events, and so on). Party Representation's slice uses a
different statistic (Pseudo R², from logistic regression) — see the
note further down this page.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### ❌ It does NOT mean")

        st.markdown("""
**“Trust increased by 27.6%.”**

The percentages are not the level of trust,
satisfaction or representation.
""")

with c2:
    with st.container(border=True):

        st.markdown("### ✅ It DOES mean")

        st.markdown("""
**“The model can account for 27.6% of the differences
in Institutional Trust between respondents.”**
""")

st.divider()


# ============================================================
# BEFORE / AFTER GRAPH
# ============================================================

st.header("What changes when Feeling Left Behind is added?")

st.markdown("""
The chart below compares each model **before and after we tell it how
left behind each respondent feels**. For Institutional Trust, this
means the model's fit moves from **10.7%** to **27.6%** — an increase
of nearly 17 percentage points.
""")

gain_long = gain_data.melt(
    id_vars="Outcome",
    value_vars=[
        "Before Feeling Left Behind",
        "After Feeling Left Behind"
    ],
    var_name="Stage",
    value_name="Model Fit"
)

gain_fig = px.bar(
    gain_long,
    y="Outcome",
    x="Model Fit",
    color="Stage",
    barmode="group",
    orientation="h",
    text="Model Fit",
    title="Before vs. After Adding Feeling Left Behind"
)

gain_fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside",
    hovertemplate=(
        "<b>%{y}</b><br>"
        "%{fullData.name}<br>"
        "%{x:.1%}"
        "<extra></extra>"
    )
)

gain_fig.update_layout(
    height=480,
    xaxis_title="Share of differences between people accounted for",
    yaxis_title="",
    legend_title="",
    xaxis=dict(
        range=[0, 0.32],
        tickformat=".0%"
    )
)

st.plotly_chart(
    gain_fig,
    width="stretch"
)

st.success("""
### What should you notice?

The jump is particularly large for:

**Institutional Trust:** 10.7% → 27.6%

and

**Democratic Satisfaction:** 9.6% → 22.2%

The change is much smaller for **Party Representation**: 3.4% → 4.6%.
This last outcome uses a different statistic (Pseudo R² from logistic
regression, since it is a Yes/No question) — not directly comparable
in scale to the other two, but the pattern of a modest gain still holds.
""")

st.warning("""
The percentages above are **not** the share of people who trust
institutions or are satisfied with democracy. They show how much of
the **differences between respondents** each model can statistically
account for.
""")

st.divider()


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "Full Comparison",
    "Institutional Trust",
    "Democratic Satisfaction",
    "Party Representation"
])


# ============================================================
# FULL COMPARISON
# ============================================================

with tab1:

    st.header("What happens as more information is added?")

    st.markdown("""
The models are built in three stages.

The purpose is to see whether Feeling Left Behind contributes
something that the more traditional variables do not already capture.
""")

    c1, c2, c3 = st.columns(3)

    with c1:

        with st.container(border=True):

            st.markdown("### 1️⃣ Traditional Factors")

            st.markdown("""
- Income
- Education
- Age
- East / West Germany
- Migration background
- Political interest
""")


    with c2:

        with st.container(border=True):

            st.markdown("### 2️⃣ + Social Class")

            st.markdown("""
Everything in Stage 1

**+**

Subjective Social Class
""")


    with c3:

        with st.container(border=True):

            st.markdown("### 3️⃣ + Feeling Left Behind")

            st.markdown("""
Everything above

**+**

Left Behind Index
""")


    st.subheader("Model comparison")

    st.dataframe(
        comparison.style.format({
            "Traditional Factors": "{:.1%}",
            "+ Social Class": "{:.1%}",
            "+ Feeling Left Behind": "{:.1%}"
        }),
        hide_index=True,
        width="stretch"
    )

    st.caption("""
Institutional Trust and Democratic Satisfaction use OLS R².

Party Representation uses McFadden Pseudo R² from logistic regression,
so its values should not be compared numerically with the other two.
""")

    st.markdown("""
*Reminder: these percentages measure how much smaller the prediction
gaps get as each layer of information is added — not a share of
people, and not a level of trust or satisfaction. See the chart at
the top of this page if this needs a refresher.*
""")

    chart_data = comparison.melt(
        id_vars="Outcome",
        var_name="Stage",
        value_name="Model Fit"
    )

    fig = px.bar(
        chart_data,
        x="Outcome",
        y="Model Fit",
        color="Stage",
        barmode="group",
        text="Model Fit",
        title="How Much of the Differences Between People Each Model Accounts For"
    )

    fig.update_traces(
        texttemplate="%{text:.1%}",
        textposition="outside"
    )

    fig.update_layout(
        height=520,
        xaxis_title="",
        yaxis_title="Share of differences between people accounted for",
        legend_title="",
        yaxis=dict(
            range=[0, 0.35],
            tickformat=".0%"
        ),
        title_font_size=15,
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


    st.success("""
### The key comparison

Adding **Subjective Social Class** produces only a relatively small
improvement.

The much larger change for Institutional Trust and Democratic Satisfaction
comes when **Feeling Left Behind** is added.

This is the central contribution of the project:

> **Feeling Left Behind captures information about democratic attitudes
> that income, education and perceived social class alone do not fully capture.**
""")


# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("🏛️ Institutional Trust")

    st.markdown("""
## What are we trying to understand?

**Why do some people trust important institutions more than others?**
""")

    st.subheader("What was measured?")

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
Respondents rated each institution from:

**1 = Do not trust at all**

to

**11 = Trust completely**

The eight answers were averaged into one Institutional Trust Index.
""")

    st.caption(
        "GLES variables: q79a–q79g and q79i."
    )

    st.divider()


    st.success("""
## Main finding

### People who feel more left behind tend to report substantially
### lower Institutional Trust.
""")


    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Before Feeling Left Behind",
        "10.7%"
    )

    c2.metric(
        "After Feeling Left Behind",
        "27.6%"
    )

    c3.metric(
        "Additional explanatory power",
        "+16.9 pp"
    )


    st.markdown("""
In simple terms:

Knowing someone's income, education, age, region, migration background,
political interest and social class gives us **some information** about
why trust differs between people.

Knowing **how left behind they feel** adds substantially more information.
""")


    st.info("""
### An especially interesting result

**Household Income is not statistically significant in the final model.**

Feeling Left Behind remains strongly associated with Institutional Trust.

This suggests that people's subjective experience of recognition and
social inclusion captures something that household income alone does not.
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
Method: OLS regression.

The negative coefficient means that higher Feeling Left Behind scores
are associated with lower Institutional Trust.
""")


# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab3:

    st.header("🗳️ Democratic Satisfaction")

    st.markdown("""
## What are we trying to understand?

**Why are some people more satisfied with how democracy works
in Germany than others?**
""")

    st.subheader("What was measured?")

    st.markdown("""
Respondents were asked:

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
Higher values therefore mean **greater dissatisfaction**.
""")

    st.caption(
        "GLES variable: q119."
    )

    st.divider()


    st.success("""
## Main finding

### People who feel more left behind tend to be less satisfied
### with how democracy works in Germany.
""")


    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Before Feeling Left Behind",
        "9.6%"
    )

    c2.metric(
        "After Feeling Left Behind",
        "22.2%"
    )

    c3.metric(
        "Additional explanatory power",
        "+12.6 pp"
    )


    st.markdown("""
Adding Subjective Social Class increases explanatory power only from:

**8.5% → 9.6%**

Adding Feeling Left Behind then increases it to:

### **22.2%**

Again, the subjective experience of being left behind adds information
that socioeconomic position alone does not fully capture.
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
Method: OLS regression.

The coefficient is positive because higher values on the original
Democratic Satisfaction variable represent greater dissatisfaction.
""")


# ============================================================
# PARTY REPRESENTATION
# ============================================================

with tab4:

    st.header("👥 Party Representation")

    st.markdown("""
## What are we trying to understand?

**Do people feel that any political party represents their views well?**
""")

    st.subheader("What was measured?")

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

    st.caption(
        "GLES variable: q141."
    )


    st.info("""
Because the answer is binary — Yes or No — this outcome is analyzed
with **logistic regression**, not OLS.
""")

    st.divider()


    st.success("""
## Main finding

### Feeling Left Behind is also associated with feeling less represented
### by a political party, but this part of the story is much weaker.
""")


    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Before Feeling Left Behind",
        "3.4%"
    )

    c2.metric(
        "After Feeling Left Behind",
        "4.6%"
    )

    c3.metric(
        "Increase in Pseudo R²",
        "+1.2 pp"
    )

    st.caption("""
These values are McFadden Pseudo R² and are not directly comparable
to the OLS R² values used for the other two outcomes.
""")


    st.markdown("""
This is important because it shows that **Feeling Left Behind is not
a universal explanation for every democratic attitude**.

Its relationship is much more pronounced for:

- Institutional Trust
- Democratic Satisfaction

than for Party Representation.
""")


    st.info("""
Political Interest is the strongest predictor in this model.

Most of the differences in Party Representation therefore depend
on factors that are not captured by the variables included here.
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

Holding the other variables constant, each one-point increase in the
Left Behind Index is associated with approximately **29% lower odds**
of saying that a political party represents the respondent's views well.
""")

        st.caption("""
Method: binary logistic regression.

The logit coefficient is not a standardized OLS beta and should not be
compared directly with the coefficients from Institutional Trust or
Democratic Satisfaction.
""")


# ============================================================
# FINAL TAKEAWAYS
# ============================================================

st.divider()

st.header("So what did this project actually find?")


with st.container(border=True):

    st.markdown("""
### 1. Income and social class do not tell the whole story

People's subjective experience of whether they feel seen, recognized,
served and able to express themselves adds information beyond their
socioeconomic characteristics.
""")


with st.container(border=True):

    st.markdown("""
### 2. Feeling Left Behind matters particularly for Institutional Trust

After Feeling Left Behind is added, the model accounts for
**27.6% of the differences in trust between respondents**, compared
with **10.7% before**.
""")


with st.container(border=True):

    st.markdown("""
### 3. A similar pattern appears for Democratic Satisfaction

The model moves from accounting for **9.6%** to **22.2%** of the
differences between respondents.
""")


with st.container(border=True):

    st.markdown("""
### 4. Party Representation is different

Feeling Left Behind is still associated with whether people feel represented,
but the model improvement is much smaller.

This suggests that **democratic disconnection has different dimensions**.
""")


st.warning("""
### What this project does NOT show

The results do not prove that Feeling Left Behind **causes**
lower trust or democratic dissatisfaction.

The GLES data are cross-sectional, so the analysis identifies
**statistical associations**, not cause and effect.
""")


st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")