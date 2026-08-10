import streamlit as st

st.title("💡 Policy Implications")

st.subheader(
    "What might these findings mean beyond the statistical analysis?"
)

st.markdown("""
The findings suggest that understanding democratic disconnection may
require looking not only at **what resources people have**, but also at
**how people believe they are treated, recognized and included by society**.
""")

st.warning("""
These are **possible implications**, not causal conclusions.

The study identifies associations. It does not demonstrate that any
particular policy intervention would increase democratic trust or
satisfaction.
""")

st.divider()

# ============================================================
# DATA VS INTERPRETATION
# ============================================================

st.header("From evidence to interpretation")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 📊 What the data show")

        st.markdown("""
Feeling Left Behind is strongly associated with:

- lower Institutional Trust;
- lower Democratic Satisfaction.

These relationships remain after accounting for socioeconomic,
demographic and political characteristics.
""")

with c2:
    with st.container(border=True):

        st.markdown("### 💡 What this may suggest")

        st.markdown("""
Understanding democratic trust may require attention not only to
income and education, but also to perceptions of:

- recognition;
- inclusion;
- access to services;
- social and political voice.
""")

st.divider()

# ============================================================
# FOUR DIMENSIONS
# ============================================================

st.header("Four areas that deserve attention")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown(
            "### 💶 Material conditions are not the whole story"
        )

        st.markdown("""
Income and education remain important indicators.

But the results suggest that they do not capture the full relationship
between people's social position and democratic attitudes.
""")

    with st.container(border=True):

        st.markdown(
            "### 🏥 Access to services may also communicate inclusion"
        )

        st.markdown("""
One component of Feeling Left Behind concerns access to basic
infrastructure and services.

Perceived neglect in these areas may form part of a broader sense
that some people or places receive less attention.
""")

with c2:

    with st.container(border=True):

        st.markdown(
            "### 👏 Recognition may matter"
        )

        st.markdown("""
People may evaluate society not only through material resources,
but also through whether their work, experiences and contributions
are seen and respected.
""")

    with st.container(border=True):

        st.markdown(
            "### 🗣️ Voice is part of the picture"
        )

        st.markdown("""
Feeling Left Behind also includes whether people feel able to express
their views publicly.

Perceived voice may therefore be another dimension of social and
democratic connection.
""")

st.divider()

# ============================================================
# DIFFERENT OUTCOMES
# ============================================================

st.header("Trust and representation are not the same problem")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Institutional Trust",
    "+16.9 pp"
)

c2.metric(
    "Democratic Satisfaction",
    "+12.6 pp"
)

c3.metric(
    "Party Representation",
    "+1.2 pp"
)

st.caption("""
First two values are OLS R² gains; Party Representation is a Pseudo R²
gain from logistic regression and is not on the same numeric scale.
""")

st.markdown("""
Feeling Left Behind adds far more explanatory power for
**Institutional Trust** and **Democratic Satisfaction** than for
**Party Representation**.

This suggests that democratic disconnection has **different dimensions**.

Distrust, dissatisfaction and poor political representation should not
automatically be treated as the same phenomenon.
""")

st.divider()

# ============================================================
# QUESTIONS
# ============================================================

st.header("Questions raised by the findings")

st.info("""
### For policymakers and researchers

**Are economic indicators alone sufficient to identify people
experiencing democratic disconnection?**

**How can recognition and perceived social inclusion be measured
alongside material conditions?**

**Could unequal access to basic services contribute to perceptions
of being overlooked?**

**Why is Feeling Left Behind much more strongly connected to trust
and democratic satisfaction than to party representation?**
""")

st.divider()

st.caption("""
These interpretations are based on statistical associations observed
in the GLES 2025 data.

Further research would be required to identify causal mechanisms or
evaluate specific policy interventions.
""")