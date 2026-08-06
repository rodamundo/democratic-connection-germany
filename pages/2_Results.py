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
This page compares three versions of the regression analysis.

- **Model 1 — Traditional factors:** household income, education, age,
  East/West Germany, migration background and political interest.

- **Model 2 — Subjective Social Class:** adds how respondents perceive
  their own position in society, beyond objective income.

- **Model 3 — Left Behind Index:** adds whether respondents feel that
  people like them are being left behind by society.

The Left Behind Index combines four questions covering economic neglect,
recognition for people's work, access to infrastructure and basic services,
and freedom to express opinions.
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

standardized_results = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Political Representation"
    ],
    "Left Behind β": [-0.459, 0.395, 0.128],
    "Final R²": [0.276, 0.222, 0.053]
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

    st.subheader("How the models build on each other")

    st.info("""
**Model 1** asks how much traditional socioeconomic and demographic
characteristics explain.

**Model 2** adds respondents' perceived social position.

**Model 3** adds the Left Behind Index.

Comparing the models shows how much additional information each new layer
contributes.
""")

    st.dataframe(
        comparison,
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
        title="How Much Variation Each Model Explains",
        color_discrete_map={
            "Model 1": "#1f77b4",
            "Model 2": "#ff7f0e",
            "Model 3": "#2ca02c"
        }
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "%{fullData.name}<br>"
            "R² = %{y:.3f}<extra></extra>"
        )
    )

    fig.update_layout(
        height=550,
        xaxis_title="",
        yaxis_title="Proportion of variation explained (R²)",
        legend_title="",
        yaxis=dict(range=[0, 0.35])
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.success("""
### Main result

Adding **Subjective Social Class** produces only a small improvement.

The largest change occurs when the **Left Behind Index** is added:

- Institutional Trust increases from **10.7% to 27.6%**
- Democratic Satisfaction increases from **9.6% to 22.2%**
- Political Representation increases only from **3.9% to 5.3%**

This suggests that feeling left behind captures information that is not
fully represented by income, education and the other traditional variables.
""")

    st.subheader("Left Behind Index across the three outcomes")

    beta_fig = px.bar(
        standardized_results,
        x="Outcome",
        y="Left Behind β",
        text="Left Behind β",
        title="Standardized Association of the Left Behind Index"
    )

    beta_fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Standardized β = %{y:.3f}<extra></extra>"
        )
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

    st.caption("""
The direction of a coefficient depends on how the outcome variable is coded.
The size of the standardized coefficient indicates the relative strength
of the association.
""")

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("Institutional Trust")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final explanatory power",
        "27.6%",
        help="Model 3 explains 27.6% of the observed variation in Institutional Trust."
    )

    c2.metric(
        "Left Behind Index β",
        "−0.459",
        help="Standardized coefficient from the final model."
    )

    c3.metric(
        "Statistical significance",
        "p < .001",
        help="Based on HC3 robust standard errors."
    )

    st.markdown("""
### Interpretation

The **Left Behind Index is the strongest standardized predictor** of
Institutional Trust among the variables included in the final model.

A higher score on the index is associated with lower trust in democratic
institutions.

This relationship remains after accounting for:

- household income;
- education;
- age;
- East/West Germany;
- migration background;
- political interest;
- Subjective Social Class.

Household Income is not statistically significant in the final model.
""")

    st.info("""
The negative coefficient does not mean that feeling left behind was experimentally
shown to cause lower trust. It indicates a strong statistical association in
this cross-sectional sample.
""")

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab3:

    st.header("Democratic Satisfaction")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final explanatory power",
        "22.2%",
        help="Model 3 explains 22.2% of the observed variation in Democratic Satisfaction."
    )

    c2.metric(
        "Left Behind Index β",
        "0.395",
        help="Standardized coefficient from the final model."
    )

    c3.metric(
        "Statistical significance",
        "p < .001",
        help="Based on HC3 robust standard errors."
    )

    st.markdown("""
### Interpretation

The Left Behind Index is also the strongest standardized predictor in the
final Democratic Satisfaction model.

The positive sign reflects the direction in which the outcome variable was
coded. In practical terms, stronger feelings of being left behind are
associated with less favorable evaluations of democracy.

Once the Left Behind Index is included, Household Income and Subjective
Social Class contribute much less to the explanation.
""")

# ============================================================
# POLITICAL REPRESENTATION
# ============================================================

with tab4:

    st.header("Political Representation")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final explanatory power",
        "5.3%",
        help="Model 3 explains 5.3% of the observed variation in Political Representation."
    )

    c2.metric(
        "Left Behind Index β",
        "0.128",
        help="Standardized coefficient from the final model."
    )

    c3.metric(
        "Statistical significance",
        "p < .001",
        help="Based on HC3 robust standard errors."
    )

    st.markdown("""
### Interpretation

The Left Behind Index remains statistically associated with Political
Representation, but the relationship is considerably weaker than for
Institutional Trust and Democratic Satisfaction.

Political Interest is the strongest predictor in this model.

The relatively low explanatory power of **5.3%** indicates that most of the
differences in Political Representation are related to factors not captured
by the variables included here.
""")

st.divider()

# ============================================================
# METHODOLOGICAL NOTE
# ============================================================

st.subheader("Methodological confidence")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Analytical sample", "5,039")
c2.metric("Cronbach's α", "0.753")
c3.metric("Factor 1 eigenvalue", "2.323")
c4.metric("Predictor VIF", "< 2")

st.markdown("""
The four items of the Left Behind Index showed acceptable internal
consistency and a clear one-factor structure.

No meaningful multicollinearity was detected. Because the regression
diagnostics indicated heteroscedasticity, statistical significance and
confidence intervals are based on **HC3 robust standard errors**.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The Left Behind Index was created from Q46a–Q46d. Higher values represent
stronger feelings that people like the respondent receive insufficient
economic attention and recognition, inadequate attention to infrastructure
and basic services, and reduced freedom to express opinions.

The analyses use cross-sectional observational data. Results describe
statistical associations and should not be interpreted as evidence of
cause and effect.
""")