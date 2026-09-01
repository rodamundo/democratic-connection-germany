import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE
# ============================================================

st.title("📊 Democratic Attitudes")

st.subheader(
    "How Feeling Left Behind relates to Institutional Trust, Democratic Satisfaction and Party Representation"
)

st.markdown("""
This page focuses on three democratic outcomes and compares three model
specifications:

**Controls only**

→ **Controls + overall Left Behind Index**

→ **Controls + the four LBI components separately**

The goal is to distinguish two questions:

1. Does the overall LBI add information beyond a conventional profile?
2. Does opening the index reveal additional information that the average hides?
""")

st.divider()


# ============================================================
# OUTCOMES
# ============================================================

st.header("1. What is being measured?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 🏛️ Institutional Trust")
        st.markdown("""
Mean trust across eight GLES institutions.

**Higher score = higher trust**
""")
        st.metric("Analytical N", "5,444")

with c2:
    with st.container(border=True):
        st.markdown("### 🗳️ Democratic Satisfaction")
        st.markdown("""
The GLES satisfaction item is reversed for this analysis.

**Higher score = greater satisfaction with democracy**
""")
        st.metric("Analytical N", "5,571")

with c3:
    with st.container(border=True):
        st.markdown("### 👥 Party Representation")
        st.markdown("""
Whether respondents say any party represents their political views well.

**1 = Yes · 0 = No**
""")
        st.metric("Analytical N", "5,008")

st.caption(
    "Each outcome uses a complete common sample for the model specifications compared within that outcome."
)

st.divider()


# ============================================================
# MODEL FIT
# ============================================================

st.header("2. What changes when Feeling Left Behind is added?")

fit_df = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Controls only": [0.11134, 0.09350, 0.03736],
    "+ overall LBI": [0.28087, 0.21996, 0.04862],
    "+ four components": [0.32555, 0.26623, 0.05006]
})

fit_display = pd.DataFrame({
    "Outcome": fit_df["Outcome"],
    "Controls only": ["11.13%", "9.35%", "3.74%"],
    "+ overall LBI": ["28.09%", "22.00%", "4.86%"],
    "+ four components": ["32.56%", "26.62%", "5.01%"]
})

st.dataframe(
    fit_display,
    width="stretch",
    hide_index=True
)

st.caption("""
Institutional Trust and Democratic Satisfaction use ordinary R².
Party Representation uses McFadden Pseudo R². The meaningful comparison
is within each outcome, not across the different fit measures.
""")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### Institutional Trust")
    trust_fit = pd.DataFrame({
        "Model": ["Controls only", "+ overall LBI", "+ four components"],
        "R²": [0.11134, 0.28087, 0.32555]
    })
    fig = px.bar(
        trust_fit,
        x="Model",
        y="R²",
        text="R²",
        title="Institutional Trust: model fit"
    )
    fig.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    fig.update_layout(
        height=430,
        xaxis_title="",
        yaxis_title="R²",
        yaxis=dict(range=[0, 0.36], tickformat=".0%")
    )
    st.plotly_chart(fig, width="stretch")

with c2:
    st.markdown("### Democratic Satisfaction")
    satisfaction_fit = pd.DataFrame({
        "Model": ["Controls only", "+ overall LBI", "+ four components"],
        "R²": [0.09350, 0.21996, 0.26623]
    })
    fig = px.bar(
        satisfaction_fit,
        x="Model",
        y="R²",
        text="R²",
        title="Democratic Satisfaction: model fit"
    )
    fig.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    fig.update_layout(
        height=430,
        xaxis_title="",
        yaxis_title="R²",
        yaxis=dict(range=[0, 0.30], tickformat=".0%")
    )
    st.plotly_chart(fig, width="stretch")

st.success("""
### Main result

The overall Left Behind Index adds substantial information for
**Institutional Trust** and **Democratic Satisfaction**.

Opening the index into four components adds further information for those
two outcomes. The gain is much smaller for generic Party Representation.
""")

st.divider()


# ============================================================
# COMPONENTS
# ============================================================

st.header("3. Which LBI components stand out?")

st.markdown("""
The four components are entered together with the conventional controls.
For the two continuous outcomes, the coefficients below are standardized,
so their magnitudes can be compared within the same model.
""")

trust_components = pd.DataFrame({
    "Component": [
        "Economic attention",
        "Social recognition",
        "Infrastructure / services",
        "Public expression"
    ],
    "Standardized coefficient": [-0.12945, -0.01803, -0.09243, -0.37360]
})

satisfaction_components = pd.DataFrame({
    "Component": [
        "Economic attention",
        "Social recognition",
        "Infrastructure / services",
        "Public expression"
    ],
    "Standardized coefficient": [-0.10997, -0.01522, -0.04592, -0.36097]
})

representation_components = pd.DataFrame({
    "Component": [
        "Economic attention",
        "Social recognition",
        "Infrastructure / services",
        "Public expression"
    ],
    "Odds ratio per 1 SD": [0.80485, 0.97301, 0.92801, 0.93719]
})


tab1, tab2, tab3 = st.tabs([
    "Institutional Trust",
    "Democratic Satisfaction",
    "Party Representation"
])

with tab1:
    fig = px.bar(
        trust_components,
        x="Standardized coefficient",
        y="Component",
        orientation="h",
        text="Standardized coefficient",
        title="Adjusted component associations with Institutional Trust"
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(
        height=430,
        xaxis_title="Standardized coefficient",
        yaxis_title="",
        xaxis=dict(range=[-0.43, 0.04])
    )
    fig.add_vline(x=0, line_width=1)
    st.plotly_chart(fig, width="stretch")
    st.caption(
        "Higher component scores indicate stronger Feeling Left Behind. "
        "More negative coefficients therefore indicate lower trust."
    )

with tab2:
    fig = px.bar(
        satisfaction_components,
        x="Standardized coefficient",
        y="Component",
        orientation="h",
        text="Standardized coefficient",
        title="Adjusted component associations with Democratic Satisfaction"
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(
        height=430,
        xaxis_title="Standardized coefficient",
        yaxis_title="",
        xaxis=dict(range=[-0.41, 0.04])
    )
    fig.add_vline(x=0, line_width=1)
    st.plotly_chart(fig, width="stretch")
    st.caption(
        "The satisfaction outcome is coded so higher values mean greater satisfaction."
    )

with tab3:
    representation_display = representation_components.copy()
    representation_display["Odds ratio per 1 SD"] = representation_display[
        "Odds ratio per 1 SD"
    ].map(lambda x: f"{x:.2f}")

    st.dataframe(
        representation_display,
        width="stretch",
        hide_index=True
    )

    st.caption("""
An odds ratio below 1 indicates lower odds of saying that a party
represents the respondent's views well as the component increases.
The public-expression coefficient is not statistically significant in
this representation model.
""")

st.divider()


# ============================================================
# INTERPRETATION
# ============================================================

st.header("4. What is the clearest pattern?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric("Trust: public expression", "−0.37")
        st.caption("Standardized coefficient")

with c2:
    with st.container(border=True):
        st.metric("Trust: economic attention", "−0.13")
        st.caption("Standardized coefficient")

with c3:
    with st.container(border=True):
        st.metric("Trust: social recognition", "−0.02")
        st.caption("Not statistically significant")

st.markdown("""
For Institutional Trust, the relationship with perceived inability to
express opinions freely is **almost three times as large** as the
relationship with economic attention and considerably larger than the
relationships with infrastructure or social recognition.

Democratic Satisfaction shows almost the same ordering.
""")

st.warning("""
### What this does not mean

The public-expression item does **not** receive greater weight in the
Left Behind Index. All four items contribute equally to the LBI.

The result means that the four equally weighted components have different
statistical relationships with these political outcomes.
""")

st.divider()


# ============================================================
# REPRESENTATION BOUNDARY
# ============================================================

st.header("5. An important boundary: Party Representation")

st.markdown("""
The public-expression item does **not** dominate every outcome.

For the generic question of whether respondents feel represented by any
political party, the four-component model adds only a small amount of
additional model fit beyond the overall LBI, and the public-expression
component is not statistically significant.
""")

st.success("""
### Why this matters

The evidence points to a **specific**, not universal, diagnosis.
Public expression stands out strongly for trust and democratic
satisfaction, but not for every measure of political connection.
""")

st.divider()


# ============================================================
# CLAIMS
# ============================================================

st.header("6. Interpretation boundaries")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### ✅ The analysis supports")
        st.markdown("""
- The overall LBI adds substantial information for Trust and Satisfaction.
- The four components add further information for those two outcomes.
- Public expression has the strongest adjusted relationship with both.
- Economic attention also shows a meaningful negative relationship.
- Component patterns are weaker for generic Party Representation.
""")

with c2:
    with st.container(border=True):
        st.markdown("### ❌ The analysis does not establish")
        st.markdown("""
- That any LBI component causes lower trust or satisfaction.
- That freedom of expression is objectively restricted.
- That public expression is more heavily weighted in the index.
- That the same component dominates every political outcome.
""")

st.divider()

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

All findings are observational and should be interpreted as statistical
associations rather than causal effects.
""")
