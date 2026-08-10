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
    "Traditional Factors": [0.088, 0.085, 0.039],
    "+ Social Class": [0.107, 0.096, 0.039],
    "+ Feeling Left Behind": [0.276, 0.222, 0.053]
})

gain_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Before Feeling Left Behind": [0.107, 0.096, 0.039],
    "After Feeling Left Behind": [0.276, 0.222, 0.053]
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

Feeling Left Behind is much more strongly connected to
**Institutional Trust** and **Democratic Satisfaction** than to
**Party Representation**.
""")

st.success("""
### Central finding

Adding Feeling Left Behind substantially increases how much the models
can explain about **trust in institutions** and **satisfaction with democracy**.

The improvement for Party Representation is much smaller.
""")

st.divider()

# ============================================================
# RESULT CARDS
# ============================================================

st.header("The result at a glance")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.metric(
            "Additional explanation",
            "+16.9 pp"
        )

        st.markdown("""
**Before:** 10.7%  
**After:** **27.6%**
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.metric(
            "Additional explanation",
            "+12.6 pp"
        )

        st.markdown("""
**Before:** 9.6%  
**After:** **22.2%**
""")

with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.metric(
            "Additional explanation",
            "+1.4 pp"
        )

        st.markdown("""
**Before:** 3.9%  
**After:** **5.3%**
""")

st.warning("""
### Important: what do these percentages mean?

They are **not** percentages of people who trust institutions or are
satisfied with democracy.

They show how much of the **differences between respondents** can be
statistically explained by the variables included in the model.
""")

st.divider()

# ============================================================
# BEFORE / AFTER GRAPH
# ============================================================

st.header(
    "How much of the differences between people can each model explain?"
)

gain_long = gain_data.melt(
    id_vars="Outcome",
    value_vars=[
        "Before Feeling Left Behind",
        "After Feeling Left Behind"
    ],
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
        "%{fullData.name}<br>"
        "Variation explained: %{x:.1%}"
        "<extra></extra>"
    )
)

gain_fig.update_layout(
    height=480,
    xaxis_title="Variation between respondents explained",
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
The large gaps for **Institutional Trust** and **Democratic Satisfaction**
show that Feeling Left Behind adds substantial information.

The much smaller gap for **Party Representation** shows that the pattern
is not equally strong for every democratic attitude.
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

    st.header("How do the three stages compare?")

    st.markdown("""
The analysis progressively adds more information:
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("### Traditional Factors")
            st.caption(
                "Income, education, age, region, migration background "
                "and political interest."
            )

    with c2:
        with st.container(border=True):
            st.markdown("### + Social Class")
            st.caption(
                "Adds respondents' perceived position in society."
            )

    with c3:
        with st.container(border=True):
            st.markdown("### + Feeling Left Behind")
            st.caption(
                "Adds perceived attention, recognition, services and voice."
            )

    st.dataframe(
        comparison.style.format({
            "Traditional Factors": "{:.1%}",
            "+ Social Class": "{:.1%}",
            "+ Feeling Left Behind": "{:.1%}"
        }),
        hide_index=True,
        width="stretch"
    )

    chart_data = comparison.melt(
        id_vars="Outcome",
        var_name="Stage",
        value_name="R²"
    )

    fig = px.bar(
        chart_data,
        x="Outcome",
        y="R²",
        color="Stage",
        barmode="group",
        text="R²",
        title="How Explanatory Power Changes as Information Is Added"
    )

    fig.update_traces(
        texttemplate="%{text:.1%}",
        textposition="outside"
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

Adding **Subjective Social Class** improves the models only slightly.

The much larger improvement appears when **Feeling Left Behind**
is introduced.

This suggests that Feeling Left Behind captures information that is
not simply another expression of income or perceived social class.
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
            yaxis=dict(
                range=[-0.55, 0.5]
            )
        )

        st.plotly_chart(
            beta_fig,
            width="stretch"
        )

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("🏛️ Institutional Trust")

    st.markdown("""
## Do people trust important institutions?
""")

    st.subheader("What was actually measured?")

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
Respondents rated each from:

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
## Finding

### People who feel more left behind tend to trust institutions substantially less.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric("Before Left Behind", "10.7%")
    c2.metric("After Left Behind", "27.6%")
    c3.metric("Increase", "+16.9 pp")

    st.markdown("""
The model explains much more of the differences in Institutional Trust
after Feeling Left Behind is included.

The relationship remains after accounting for:

- income;
- education;
- age;
- East / West Germany;
- migration background;
- political interest;
- Subjective Social Class.
""")

    st.info("""
**Household Income is not statistically significant in the final model.**

This suggests that income alone does not capture the same information
as people's subjective experience of recognition and social inclusion.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "27.6%")
        c2.metric("Standardized β", "−0.459")
        c3.metric("p-value", "< .001")

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab3:

    st.header("🗳️ Democratic Satisfaction")

    st.markdown("""
## Are people satisfied with how democracy works in Germany?
""")

    st.subheader("What was actually measured?")

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

    st.caption(
        "GLES variable: q119."
    )

    st.divider()

    st.success("""
## Finding

### People who feel more left behind tend to be less satisfied with how democracy works.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric("Before Left Behind", "9.6%")
    c2.metric("After Left Behind", "22.2%")
    c3.metric("Increase", "+12.6 pp")

    st.markdown("""
Adding Subjective Social Class increases explanatory power from
**8.5% to 9.6%**.

Adding Feeling Left Behind then increases it to **22.2%**.

This suggests that perceived social disconnection provides information
about democratic dissatisfaction that socioeconomic position alone
does not fully capture.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "22.2%")
        c2.metric("Standardized β", "0.395")
        c3.metric("p-value", "< .001")

        st.caption("""
The positive sign reflects the original coding of q119:
higher values mean greater dissatisfaction.
""")

# ============================================================
# PARTY REPRESENTATION
# ============================================================

with tab4:

    st.header("👥 Party Representation")

    st.markdown("""
## Does any political party represent the respondent's views well?
""")

    st.subheader("What was actually measured?")

    st.markdown("""
Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**
""")

    c1, c2 = st.columns(2)

    c1.metric("1", "Yes")
    c2.metric("2", "No")

    st.caption(
        "GLES variable: q141."
    )

    st.divider()

    st.success("""
## Finding

### Feeling Left Behind is related to lower Party Representation,
### but the relationship is much weaker.
""")

    c1, c2, c3 = st.columns(3)

    c1.metric("Before Left Behind", "3.9%")
    c2.metric("After Left Behind", "5.3%")
    c3.metric("Increase", "+1.4 pp")

    st.markdown("""
Compare the additional explanatory power:

- **Institutional Trust:** +16.9 pp
- **Democratic Satisfaction:** +12.6 pp
- **Party Representation:** +1.4 pp

This sets an important boundary on the findings:

### Feeling Left Behind does not explain every dimension of democratic
### disconnection equally.
""")

    st.info("""
Political Interest is the strongest predictor in this model.

The final model explains only **5.3%** of the differences in Party
Representation, meaning that most of those differences depend on
other factors not captured here.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric("Final R²", "5.3%")
        c2.metric("Standardized β", "0.128")
        c3.metric("p-value", "< .001")

# ============================================================
# CONCLUSIONS
# ============================================================

st.divider()

st.header("What did we learn?")

with st.container(border=True):
    st.markdown("""
### 1. Economic position is not the whole story

Feeling socially recognized and included provides information about
democratic attitudes beyond household income and education.
""")

with st.container(border=True):
    st.markdown("""
### 2. Feeling Left Behind is not simply another name for social class

Adding Subjective Social Class changes the models relatively little.

Adding Feeling Left Behind changes two of them substantially.
""")

with st.container(border=True):
    st.markdown("""
### 3. Institutional Trust shows the strongest relationship

Adding Feeling Left Behind increases explained variation from
**10.7% to 27.6%**.
""")

with st.container(border=True):
    st.markdown("""
### 4. Democratic Satisfaction follows a similar pattern

Explained variation increases from **9.6% to 22.2%**.
""")

with st.container(border=True):
    st.markdown("""
### 5. Party Representation behaves differently

The increase is only **1.4 percentage points**, suggesting that
democratic disconnection has different dimensions.
""")

st.warning("""
The analysis identifies **statistical associations**.

Because the survey is cross-sectional, it cannot demonstrate that
Feeling Left Behind causes lower trust or democratic satisfaction.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")