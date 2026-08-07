import streamlit as st

st.title("💡 Policy Implications")

st.markdown("""
## What might these findings mean beyond the statistical analysis?

The results suggest that understanding democratic disconnection may require
looking not only at **what people have**, but also at **how people believe
they are treated and recognized by society**.
""")

st.warning("""
These are **possible implications**, not causal conclusions.

The study shows associations. It does not demonstrate that any specific
policy intervention would increase democratic trust or satisfaction.
""")

st.divider()

# ============================================================
# DATA SHOW VS POSSIBLE IMPLICATION
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

The relationship remains after accounting for socioeconomic
and demographic characteristics.
""")

with c2:
    with st.container(border=True):
        st.markdown("### 💡 Possible implication")
        st.markdown("""
Understanding democratic trust may require attention not only to
income or education, but also to perceptions of:

- recognition;
- inclusion;
- access to services;
- social and political voice.
""")

st.divider()

# ============================================================
# IMPLICATION CARDS
# ============================================================

st.header("Four areas for further attention")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### 💶 1. Material conditions are not the whole story")
        st.markdown("""
Income and education remain important social indicators.

But the results suggest that they do not capture the full relationship
between social position and democratic attitudes.
""")

    with st.container(border=True):
        st.markdown("### 🏥 3. Services can also communicate inclusion")
        st.markdown("""
One part of the Left Behind Index concerns access to doctors, transport,
schools, banks, postal services and Internet.

Perceived neglect of basic services may therefore be connected not only
to service quality but also to broader feelings of social inclusion.
""")

with c2:
    with st.container(border=True):
        st.markdown("### 👏 2. Recognition may matter")
        st.markdown("""
Citizens may evaluate society not only through material resources,
but also through whether their work, contribution and concerns are
seen and respected.
""")

    with st.container(border=True):
        st.markdown("### 🗣️ 4. Voice is part of the picture")
        st.markdown("""
The Left Behind Index also captures whether respondents feel able to
express their opinions publicly.

Perceived voice and recognition may therefore be relevant dimensions
of democratic connection.
""")

st.divider()

# ============================================================
# DIFFERENT DIMENSIONS
# ============================================================

st.header("Trust and representation are not the same problem")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Trust gain",
    "+16.9 pp"
)

c2.metric(
    "Satisfaction gain",
    "+12.6 pp"
)

c3.metric(
    "Representation gain",
    "+1.4 pp"
)

st.markdown("""
Feeling Left Behind adds far more explanatory power for **Institutional Trust**
and **Democratic Satisfaction** than for **Party Representation**.

This suggests that democratic disconnection has different dimensions.

A person may distrust institutions, be dissatisfied with democracy
and feel poorly represented for **different combinations of reasons**.
""")

st.divider()

# ============================================================
# POLICY QUESTIONS
# ============================================================

st.header("Questions the findings raise")

st.info("""
### For policymakers and researchers:

**Are economic indicators enough to identify groups experiencing
democratic disconnection?**

**How can perceptions of recognition and social inclusion be measured
alongside material conditions?**

**Could geographic differences in access to basic services contribute
to feelings of being overlooked?**

**Why is Feeling Left Behind much more closely connected to trust and
democratic satisfaction than to party representation?**
""")

st.divider()

st.caption("""
These interpretations are based on associations observed in the
GLES 2025 data. Further research would be required to test causal
mechanisms and policy interventions.
""")