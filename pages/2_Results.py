import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Results",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Results")

st.markdown("""
The analysis compares three versions of the same regression model.

- **Model 1 — Traditional factors:** household income, education, age,
  East/West Germany, migration background and political interest.

- **Model 2 — Subjective Social Class:** adds how respondents perceive
  their own position in society, beyond their objective income.

- **Model 3 — Left Behind Index:** adds an index created from four survey
  questions measuring whether respondents feel that people like them are
  being left behind by society.

The four questions cover perceived economic neglect, lack of recognition,
insufficient attention to basic infrastructure and services, and restrictions
on freely expressing opinions.

Each model adds one new layer of information. Comparing them shows whether
the additional variable improves our understanding of democratic attitudes.
""")

st.divider()

# ============================================================
# DATA
# ============================================================

comparison = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Political Representation"
    ],
    "Model 1": [0.088, 0.085, 0.039],
    "Model 2": [0.107, 0.096, 0.039],
    "Model 3": [0.276, 0.222, 0.053]
})

# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Institutional Trust",
    "Democratic Satisfaction",
    "Political Representation"
])

# ============================================================
# OVERVIEW
# ============================================================

with tab1:

    st.header("Overview")

    st.subheader("Model comparison")

    st.info("""
### How to read this chart

🔵 **Model 1 — Traditional factors**  
Household income, education, age, East/West Germany,
migration background and political interest.

🟠 **Model 2 — Subjective Social Class**  
Adds how respondents perceive their own position in society.

🟢 **Model 3 — Left Behind Index**  
Adds an index created from four survey questions measuring whether respondents
feel that people like them are being left behind by society.

The four questions cover:

- economic neglect;
- lack of social recognition;
- insufficient attention to infrastructure and basic services;
- reduced freedom to express opinions.

The higher the bar, the more of the outcome the model is able to explain.
""")

    st.dataframe(
        comparison,
        hide_index=True,
        use_container_width=True
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
        title="Comparing the Three Models",
        color_discrete_map={
            "Model 1": "#1f77b4",
            "Model 2": "#ff7f0e",
            "Model 3": "#2ca02c"
        }
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    fig.update_layout(
        height=550,
        xaxis_title="",
        yaxis_title="How well each model explains the outcome",
        legend_title="",
        yaxis=dict(range=[0, 0.35])
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success("""
### What does this graph tell us?

Traditional socioeconomic and demographic variables explain part of the
differences in democratic attitudes.

Adding Subjective Social Class produces only a small improvement.

The largest improvement occurs when the Left Behind Index is added in Model 3.

For Institutional Trust, the explanatory power increases from approximately
10.7% in Model 2 to 27.6% in Model 3.

For Democratic Satisfaction, it increases from approximately 9.6% to 22.2%.

The improvement is much smaller for Political Representation, where the
explanatory power increases from approximately 3.9% to 5.3%.

This suggests that feeling left behind captures an important dimension that
is not fully represented by income, education and the other traditional
variables included in the analysis.
""")

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("Institutional Trust")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final explanatory power", "27.6%")
    c2.metric("Left Behind Index β", "−0.459")
    c3.metric("Statistical significance", "p < .001")

    st.markdown("""
### What this means

The Left Behind Index has the largest standardized coefficient among the
variables included in the final model.

Its negative coefficient means that stronger feelings of being left behind
are associated with lower Institutional Trust.

This relationship remains after accounting for household income, education,
age, East/West Germany, migration background, political interest and
Subjective Social Class.

Household Income is not statistically significant in the final model.
""")

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab3:

    st.header("Democratic Satisfaction")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final explanatory power", "22.2%")
    c2.metric("Left Behind Index β", "0.395")
    c3.metric("Statistical significance", "p < .001")

    st.markdown("""
### What this means

The Left Behind Index also has the largest standardized coefficient
in the final Democratic Satisfaction model.

Its positive coefficient reflects the direction of the outcome scale used
in the dataset. In practical terms, stronger feelings of being left behind
are associated with less favorable evaluations of democracy.

After the Left Behind Index is included, Household Income and Subjective
Social Class contribute much less to the model.
""")

# ============================================================
# POLITICAL REPRESENTATION
# ============================================================

with tab4:

    st.header("Political Representation")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final explanatory power", "5.3%")
    c2.metric("Left Behind Index β", "0.128")
    c3.metric("Statistical significance", "p < .001")

    st.markdown("""
### What this means

The Left Behind Index remains statistically associated with Political
Representation, but the relationship is considerably weaker than for
Institutional Trust and Democratic Satisfaction.

Political Interest has the largest standardized coefficient in this model.

The relatively low final explanatory power of 5.3% indicates that important
factors related to Political Representation are not captured by the variables
included here.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025), Post-Election
Cross-Section, ZA10100.

The Left Behind Index was created from Q46a–Q46d. These questions measure
whether respondents feel that people like them receive too little economic
attention, too little recognition, insufficient access to infrastructure and
basic services, and reduced freedom to express their opinions.

The four responses were reverse-coded and averaged into a single score, where
higher values represent stronger feelings of being left behind.

Results are based on cross-sectional OLS regression models. They describe
statistical associations and should not be interpreted as proof of cause
and effect.
""")