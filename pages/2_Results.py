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
The analysis compares three versions of the same model.

- **Model 1 — Traditional factors:** income, education, age, region,
  migration background and political interest.

- **Model 2 — Traditional factors + social position:** adds how people
  perceive their own social class.

- **Model 3 — Traditional factors + social position + Social Disconnection:**
  adds whether people feel socially connected, recognized and included.

Each model adds one new layer of information. This allows us to see whether
understanding how people feel about their place in society improves our
understanding of democratic attitudes.
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
Income, education, age, region, migration background and political interest.

🟠 **Model 2 — Traditional factors + Subjective Social Class**  
This adds how people perceive their own social position.

🟢 **Model 3 — Model 2 + Social Disconnection**  
This also adds whether people feel socially connected, recognized and included.

The higher the bar, the better the model helps us understand differences
in the democratic outcome.
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

When we only consider traditional factors such as income, education and age,
we can explain part of the differences in democratic attitudes.

When we also include how people perceive their own social class, the models
improve slightly.

The largest improvement happens when Social Disconnection is added.

This means that considering whether people feel socially connected, recognized
and included helps us understand Institutional Trust and Democratic Satisfaction
much better.

The improvement is much smaller for Political Representation, suggesting that
this outcome follows a different pattern.
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

Social Disconnection is the strongest predictor of Institutional Trust
among the variables included in the model.

Once we include whether people feel socially disconnected, the model becomes
much better at understanding why some people trust democratic institutions
more than others.

Household Income does not make a meaningful independent contribution in the
final model.
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

The same general pattern appears for Democratic Satisfaction.

Social Disconnection is the strongest predictor after the other characteristics
are included.

Once Social Disconnection enters the model, Subjective Social Class contributes
much less to the explanation.
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

Political Representation behaves differently.

Social Disconnection is still associated with this outcome, but the relationship
is much weaker than for Institutional Trust and Democratic Satisfaction.

Political Interest is the strongest predictor in this model.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025).

Results are based on cross-sectional OLS regression models. They describe
statistical associations and should not be interpreted as proof of cause and effect.
""")