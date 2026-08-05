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

- **Model 3 — Social Disconnection Index:** adds an index created from
  four survey questions: Q46a, Q46b, Q46c and Q46d.

The four responses were reverse-coded and averaged into one score.
Higher scores represent higher levels of the experience measured by
the Social Disconnection Index.

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

🟢 **Model 3 — Social Disconnection Index**  
Adds an index based on four survey questions: Q46a–Q46d.
The responses were reverse-coded and averaged into one score.

The higher the bar, the more variation in the democratic outcome
the model is able to explain.
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

The largest improvement occurs when the Social Disconnection Index is added
in Model 3.

For Institutional Trust, the explanatory power increases from approximately
10.7% in Model 2 to 27.6% in Model 3.

For Democratic Satisfaction, it increases from approximately 9.6% to 22.2%.

The improvement is much smaller for Political Representation, where the
explanatory power increases from approximately 3.9% to 5.3%.

This indicates that the information captured by the Social Disconnection
Index is particularly relevant to Institutional Trust and Democratic
Satisfaction.
""")

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("Institutional Trust")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final explanatory power", "27.6%")
    c2.metric("Social Disconnection β", "−0.459")
    c3.metric("Statistical significance", "p < .001")

    st.markdown("""
### What this means

The Social Disconnection Index has the largest standardized coefficient
among the variables included in the final model.

Its negative coefficient means that higher Social Disconnection scores
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
    c2.metric("Social Disconnection β", "0.395")
    c3.metric("Statistical significance", "p < .001")

    st.markdown("""
### What this means

The Social Disconnection Index also has the largest standardized coefficient
in the final Democratic Satisfaction model.

Its positive coefficient reflects the direction of the outcome scale used
in the dataset. The exact substantive interpretation therefore depends on
how Democratic Satisfaction was coded.

After the Social Disconnection Index is included, Household Income and
Subjective Social Class contribute much less to the model.
""")

# ============================================================
# POLITICAL REPRESENTATION
# ============================================================

with tab4:

    st.header("Political Representation")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final explanatory power", "5.3%")
    c2.metric("Social Disconnection β", "0.128")
    c3.metric("Statistical significance", "p < .001")

    st.markdown("""
### What this means

The Social Disconnection Index remains statistically associated with
Political Representation, but the relationship is considerably weaker
than for Institutional Trust and Democratic Satisfaction.

Political Interest has the largest standardized coefficient in this model.

The relatively low final explanatory power of 5.3% also indicates that
important factors related to Political Representation are not captured
by the variables included here.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025).

The Social Disconnection Index was created from Q46a–Q46d by reverse-coding
the four responses and calculating their average.

Results are based on cross-sectional OLS regression models. They describe
statistical associations and should not be interpreted as proof of cause
and effect.

The exact conceptual interpretation of Q46a–Q46d should be confirmed against
the official GLES questionnaire or codebook before the final version of the
project.
""")