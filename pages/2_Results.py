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

gain_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Before Left Behind": [0.107, 0.096, 0.039],
    "After Left Behind": [0.276, 0.222, 0.053],
    "Increase": [0.169, 0.126, 0.014]
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
# INTRO
# ============================================================

st.markdown("""
## What did we find?

Feeling Left Behind is much more strongly connected to **Institutional Trust**
and **Democratic Satisfaction** than to **Party Representation**.
""")

st.success("""
### The central finding

Knowing whether people feel overlooked, unrecognized or left behind adds
substantial information about **trust in institutions** and
**satisfaction with democracy**, even after accounting for socioeconomic
and demographic characteristics.
""")

st.divider()

# ============================================================
# MAIN VISUAL
# ============================================================

st.header("What changes when Feeling Left Behind is added?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 🏛️ Institutional Trust")
        st.metric(
            "Increase",
            "+16.9 pp"
        )
        st.write("10.7% → **27.6%**")

with c2:
    with st.container(border=True):
        st.markdown("### 🗳️ Democratic Satisfaction")
        st.metric(
            "Increase",
            "+12.6 pp"
        )
        st.write("9.6% → **22.2%**")

with c3:
    with st.container(border=True):
        st.markdown("### 👥 Party Representation")
        st.metric(
            "Increase",
            "+1.4 pp"
        )
        st.write("3.9% → **5.3%**")

# ------------------------------------------------------------
# GAIN CHART
# ------------------------------------------------------------

gain_long = gain_data.melt(
    id_vars="Outcome",
    value_vars=["Before Left Behind", "After Left Behind"],
    var_name="Stage",
    value_name="Explained"
)

gain_fig = px.bar(
    gain_long,
    y="Outcome",
    x="Explained",
    color="Stage",
    barmode="group",
    orientation="h",
    text="Explained",
    title="Before vs. After Adding Feeling Left Behind"
)

gain_fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside",
    hovertemplate=(
        "<b>%{y}</b><br>"
        "%{fullData.name}: %{x:.1%}"
        "<extra></extra>"
    )
)

gain_fig.update_layout(
    height=480,
    xaxis_title="Variation explained",
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

st.info("""
### How to read this graph

The longer the **After Left Behind** bar grows compared with the
**Before Left Behind** bar, the more additional information the
Left Behind Index contributes.

The difference is large for trust and democratic satisfaction,
but small for party representation.
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

    st.header("The complete picture")

    st.subheader("Three steps in the analysis")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("### Model 1")
            st.markdown("**Traditional factors**")
            st.caption(
                "Income, education, age, region, migration background "
                "and political interest."
            )

    with c2:
        with st.container(border=True):
            st.markdown("### Model 2")
            st.markdown("**+ Subjective Social Class**")
            st.caption(
                "Adds where respondents believe they sit in society."
            )

    with c3:
        with st.container(border=True):
            st.markdown("### Model 3")
            st.markdown("**+ Feeling Left Behind**")
            st.caption(
                "Adds perceptions of neglect, recognition, services and voice."
            )

    st.subheader("Full model comparison")

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
        title="How Much of Each Outcome Can the Models Explain?"
    )

    fig.update_traces(
        texttemplate="%{text:.1%}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "%{fullData.name}<br>"
            "Variation explained: %{y:.1%}"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        height=520,
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
### What stands out?

**Subjective Social Class adds relatively little.**

The much larger improvement appears only after the
**Left Behind Index** is introduced.

This suggests that Feeling Left Behind is not simply another way of
measuring income or perceived social class.
""")

    with st.expander("Technical evidence: standardized coefficients"):

        beta_fig = px.bar(
            standardized_results,
            x="Outcome",
            y="Left Behind β",
            text="Left Behind β",
            title="Standardized Association of Feeling Left Behind"
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
            height=450,
            xaxis_title="",
            yaxis_title="Standardized coefficient (β)",
            yaxis=dict(range=[-0.55, 0.5])
        )

        st.plotly_chart(
            beta_fig,
            width="stretch"
        )

        st.markdown("""
The absolute size of β indicates how strongly Feeling Left Behind
is associated with each outcome within the final model.
""")

# ============================================================
# LEFT BEHIND INDEX
# ============================================================

with tab2:

    st.header("🧩 Left Behind Index")

    st.markdown("""
## What exactly are we measuring?

Feeling Left Behind is treated here as a **subjective experience of social
disconnection**.

It asks whether people feel that **people like them** receive adequate
attention, recognition, services and space to express themselves.
""")

    st.warning("""
### Important distinction

**Feeling Left Behind ≠ Low Income**

A person can have relatively limited economic resources without feeling
socially ignored.

Likewise, someone who is not economically poor may still feel overlooked,
unrecognized or excluded.
""")

    st.divider()

    # --------------------------------------------------------
    # FOUR DIMENSIONS
    # --------------------------------------------------------

    st.subheader("Four dimensions")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.markdown("### 💶 1. Economic attention — q46a")
            st.markdown("""
**Simple idea:**  
*Are the economic concerns of people like me being ignored?*

**Original statement:**

> “The economic situation of people like me receives too little
> attention from society.”
""")

        with st.container(border=True):
            st.markdown("### 🏥 3. Infrastructure and services — q46c")
            st.markdown("""
**Simple idea:**  
*Do people like me receive adequate access to essential services?*

**Original statement:**

> “Society pays too little attention to ensuring that people like me
> have access to basic infrastructures and services.”

Examples include doctors, banks, public transport, schools,
post offices and Internet access.
""")

    with c2:
        with st.container(border=True):
            st.markdown("### 👏 2. Social recognition — q46b")
            st.markdown("""
**Simple idea:**  
*Is the work of people like me valued?*

**Original statement:**

> “People like me receive too little recognition from society
> for the work they do.”
""")

        with st.container(border=True):
            st.markdown("### 🗣️ 4. Freedom of expression — q46d")
            st.markdown("""
**Simple idea:**  
*Do people like me feel free to express their opinions?*

**Original statement:**

> “People like me are no longer allowed to freely express their
> opinions in public.”
""")

    st.divider()

    # --------------------------------------------------------
    # SCALE
    # --------------------------------------------------------

    st.subheader("How does the scale work?")

    st.markdown("""
The original GLES questions are coded in the opposite direction:
""")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("1", "Strongly agree")
    c2.metric("2", "Agree")
    c3.metric("3", "Neutral")
    c4.metric("4", "Disagree")
    c5.metric("5", "Strongly disagree")

    st.markdown("""
Because **agreement means a stronger feeling of being left behind**,
the scale is reversed before constructing the index.
""")

    st.code(
        "reversed_score = 6 - original_score",
        language="python"
    )

    st.markdown("""
### Final interpretation

**1 — Lower Feeling Left Behind**

`● ───── ● ───── ● ───── ● ───── ●`

**5 — Higher Feeling Left Behind**
""")

    st.divider()

    # --------------------------------------------------------
    # CONSTRUCTION
    # --------------------------------------------------------

    st.subheader("How is one index created from four answers?")

    c1, c2, c3, c4 = st.columns(4)

    c1.markdown("### 💶")
    c1.markdown("Economic attention")

    c2.markdown("### 👏")
    c2.markdown("Recognition")

    c3.markdown("### 🏥")
    c3.markdown("Services")

    c4.markdown("### 🗣️")
    c4.markdown("Voice")

    st.markdown("""
### ↓

### Average of the four reversed responses

# → Left Behind Index
""")

    st.divider()

    # --------------------------------------------------------
    # DIFFERENCE FROM OTHER CONCEPTS
    # --------------------------------------------------------

    st.subheader("Three concepts that should not be confused")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("### 💰 Household Income")
            st.write(
                "Measures economic resources."
            )
            st.caption("Objective socioeconomic position")

    with c2:
        with st.container(border=True):
            st.markdown("### 🪜 Subjective Social Class")
            st.write(
                "Measures where people believe they sit in the social hierarchy."
            )
            st.caption("Perceived social position")

    with c3:
        with st.container(border=True):
            st.markdown("### 🧩 Feeling Left Behind")
            st.write(
                "Measures whether people feel overlooked, unrecognized, "
                "underserved or constrained."
            )
            st.caption("Subjective social disconnection")

    st.success("""
### Why this distinction matters

The research asks whether **how people experience their place in society**
adds information beyond **where they objectively or subjectively sit in
the socioeconomic hierarchy**.
""")

    st.divider()

    with st.expander("How do we know the four questions belong together?"):

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
The four questions showed acceptable internal consistency and a clear
one-factor structure.

This supports combining them into one summary measure.
""")

    st.warning("""
The index measures **perceptions**.

It does not determine whether society objectively provides too little
attention, recognition, infrastructure or freedom of expression.
""")

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab3:

    st.header("🏛️ Institutional Trust")

    st.markdown("""
## Do people trust important institutions?
""")

    st.subheader("What was measured?")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
Respondents rated their trust in:

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
Each was rated from **1 = Do not trust at all**
to **11 = Trust completely**.

The eight answers were averaged into one Institutional Trust Index.
""")

    st.caption("GLES variables: q79a–q79g and q79i.")

    st.divider()

    st.success("""
## Finding

### People who feel more left behind tend to trust institutions substantially less.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Before Left Behind",
        "10.7%"
    )

    c2.metric(
        "After Left Behind",
        "27.6%"
    )

    c3.metric(
        "Increase",
        "+16.9 pp"
    )

    st.markdown("""
The model explains much more of the differences in Institutional Trust
after Feeling Left Behind is included.

This relationship remains after accounting for income, education,
age, East/West Germany, migration background, political interest and
Subjective Social Class.
""")

    st.info("""
**Household Income is not statistically significant in the final model.**

This suggests that income alone does not capture the same information
as people's subjective experience of social recognition and inclusion.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "27.6%")
        c2.metric("Standardized β", "−0.459")
        c3.metric("p-value", "< .001")

        st.caption(
            "Higher Left Behind scores are associated with lower "
            "Institutional Trust."
        )

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab4:

    st.header("🗳️ Democratic Satisfaction")

    st.markdown("""
## Are people satisfied with how democracy works in Germany?
""")

    st.subheader("What was measured?")

    st.markdown("""
Respondents were asked:

> **“How satisfied are you with the way democracy works in Germany?”**
""")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("1", "Very satisfied")
    c2.metric("2", "Fairly satisfied")
    c3.metric("3", "Not very satisfied")
    c4.metric("4", "Not at all satisfied")

    st.info("""
Higher values therefore mean **greater dissatisfaction**.
""")

    st.caption("GLES variable: q119.")

    st.divider()

    st.success("""
## Finding

### People who feel more left behind tend to be less satisfied with how democracy works.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Before Left Behind",
        "9.6%"
    )

    c2.metric(
        "After Left Behind",
        "22.2%"
    )

    c3.metric(
        "Increase",
        "+12.6 pp"
    )

    st.markdown("""
Adding Subjective Social Class increases explanatory power only from
**8.5% to 9.6%**.

Adding Feeling Left Behind then increases it to **22.2%**.

The subjective experience of social disconnection therefore provides
substantial additional information about democratic dissatisfaction.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "22.2%")
        c2.metric("Standardized β", "0.395")
        c3.metric("p-value", "< .001")

        st.caption("""
The coefficient is positive because larger values on the original
survey scale represent greater dissatisfaction.
""")

# ============================================================
# PARTY REPRESENTATION
# ============================================================

with tab5:

    st.header("👥 Party Representation")

    st.markdown("""
## Does any political party represent the respondent's views well?
""")

    st.subheader("What was measured?")

    st.markdown("""
Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**
""")

    c1, c2 = st.columns(2)

    c1.metric("1", "Yes")
    c2.metric("2", "No")

    st.caption("GLES variable: q141.")

    st.divider()

    st.success("""
## Finding

### Feeling Left Behind is related to lower Party Representation,
### but the relationship is much weaker.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Before Left Behind",
        "3.9%"
    )

    c2.metric(
        "After Left Behind",
        "5.3%"
    )

    c3.metric(
        "Increase",
        "+1.4 pp"
    )

    st.markdown("""
Compare the additional explanatory power:

**Institutional Trust:** +16.9 pp  
**Democratic Satisfaction:** +12.6 pp  
**Party Representation:** +1.4 pp

This is an important boundary to the findings:

### Feeling Left Behind does not explain every dimension of democratic
### disconnection equally.
""")

    st.info("""
Political Interest is the strongest predictor in this model.

The final model explains only 5.3% of differences in Party Representation,
suggesting that most of those differences depend on factors outside the
variables studied here.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "5.3%")
        c2.metric("Standardized β", "0.128")
        c3.metric("p-value", "< .001")

# ============================================================
# BIG PICTURE
# ============================================================

st.divider()

st.header("Five things we learned")

with st.container(border=True):
    st.markdown("""
### 1. Feeling Left Behind contains information beyond income.

Economic position alone does not capture how recognized, included or
overlooked people feel.
""")

with st.container(border=True):
    st.markdown("""
### 2. Feeling Left Behind is not simply another name for social class.

Adding Subjective Social Class changes the models relatively little.
Adding the Left Behind Index changes two of them substantially.
""")

with st.container(border=True):
    st.markdown("""
### 3. Institutional Trust shows the strongest relationship.

The model's explanatory power rises from **10.7% to 27.6%**.
""")

with st.container(border=True):
    st.markdown("""
### 4. Democratic Satisfaction shows a similar pattern.

The model rises from **9.6% to 22.2%** after Feeling Left Behind is added.
""")

with st.container(border=True):
    st.markdown("""
### 5. Party Representation is different.

Feeling Left Behind adds only **1.4 percentage points** of explanatory power,
showing that democratic disconnection has different dimensions.
""")

st.warning("""
### What we cannot say

These data are cross-sectional.

The analysis shows **associations**, not proof that Feeling Left Behind
causes distrust or democratic dissatisfaction.
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