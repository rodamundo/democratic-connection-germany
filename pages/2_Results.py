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
The analysis estimates three nested regression models for each democratic outcome.

- **Model 1:** Socioeconomic and demographic controls
- **Model 2:** Adds Subjective Social Class
- **Model 3:** Adds Social Disconnection
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
        title="Explanatory Power Across Regression Models"
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    fig.update_layout(
        height=550,
        xaxis_title="",
        yaxis_title="R²",
        legend_title="",
        yaxis=dict(range=[0,0.35])
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success("""
**Main finding**

Adding Social Disconnection substantially increases the explanatory power
for Institutional Trust and Democratic Satisfaction, whereas the improvement
is much smaller for Political Representation.
""")

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("Institutional Trust")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final R²","0.276")
    c2.metric("β Social Disconnection","−0.459")
    c3.metric("p-value","< .001")

    st.markdown("""
### Interpretation

Social Disconnection is the strongest standardized predictor of
Institutional Trust.

After controlling for household income, education, migration background,
age, political interest and region, Social Disconnection remains highly
significant.

Household Income is not statistically significant in the final model.
""")

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab3:

    st.header("Democratic Satisfaction")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final R²","0.222")
    c2.metric("β Social Disconnection","0.395")
    c3.metric("p-value","< .001")

    st.markdown("""
### Interpretation

The same pattern appears for Democratic Satisfaction.

Social Disconnection remains the strongest predictor after all controls are
introduced.

Subjective Social Class loses most of its explanatory power once Social
Disconnection enters the model.
""")

# ============================================================
# POLITICAL REPRESENTATION
# ============================================================

with tab4:

    st.header("Political Representation")

    c1, c2, c3 = st.columns(3)

    c1.metric("Final R²","0.053")
    c2.metric("β Social Disconnection","0.128")
    c3.metric("p-value","< .001")

    st.markdown("""
### Interpretation

Political Representation behaves differently.

Although Social Disconnection remains statistically significant,
its explanatory power is considerably smaller.

Political Interest is the strongest predictor in this model.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025).

Results are based on cross-sectional OLS regression models and describe
statistical associations rather than causal relationships.
""")