import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.title("💡 Policy Implications")

st.subheader(
    "What might these findings mean for policy and future research?"
)

st.markdown("""
The goal of this page is not to repeat the statistical results.

Instead, it asks:

### If Feeling Left Behind adds information beyond traditional
### socioeconomic, demographic and political characteristics,
### what might policymakers and researchers learn from that?
""")

st.warning("""
### Association ≠ causation

This study identifies statistical associations in cross-sectional
survey data.

It does **not** show that a specific policy intervention will
automatically increase trust, satisfaction or representation.
""")

st.divider()


# ============================================================
# 1. MAIN POLICY MESSAGE
# ============================================================

st.header("1. The main policy message")

st.markdown("""
Traditional indicators such as income, education, age and region
remain important.

But the results suggest that they may not capture the whole picture.

People's **subjective experience of how society treats people like them**
may provide additional information about democratic disconnection.
""")

st.success("""
# A useful policy question may therefore be:

### Not only:

**“What resources do people have?”**

### But also:

**“Do people feel that people like them are seen, recognized,
served and heard?”**
""")

st.divider()


# ============================================================
# 2. WHAT COULD BE MEASURED?
# ============================================================

st.header("2. What could policymakers monitor?")

st.markdown("""
The Feeling Left Behind Index combines four dimensions.

The current study does **not** estimate the independent causal effect
of each one, but they offer a useful framework for further diagnosis.
""")

c1, c2, c3, c4 = st.columns(4)


with c1:
    with st.container(border=True):

        st.markdown("### 💶 Economic attention")

        st.markdown("""
Do people feel that the economic situation of
**people like them** receives enough attention?
""")


with c2:
    with st.container(border=True):

        st.markdown("### 👏 Recognition")

        st.markdown("""
Do people feel that the work and contribution of
**people like them** is sufficiently recognized?
""")


with c3:
    with st.container(border=True):

        st.markdown("### 🏥 Services")

        st.markdown("""
Do people feel that **people like them** have adequate
access to basic services and infrastructure?
""")


with c4:
    with st.container(border=True):

        st.markdown("### 🗣️ Voice")

        st.markdown("""
Do people feel that **people like them** can freely
express their views and be heard?
""")


st.info("""
These four dimensions are components of the **combined LBI**.

This project does not show that any one of them independently
causes higher or lower democratic trust.
""")

st.divider()


# ============================================================
# 3. WHY SUBJECTIVE EXPERIENCE MATTERS
# ============================================================

st.header("3. Why might subjective experience matter?")

st.markdown("""
Two people can look very similar in traditional socioeconomic terms
and still have very different relationships with democracy.
""")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("### Person A")

        st.markdown("""
Similar income

Similar education

Similar age

Similar region

### But feels:

✅ recognized

✅ included

✅ adequately served

✅ heard
""")


with c2:
    with st.container(border=True):

        st.markdown("### Person B")

        st.markdown("""
Similar income

Similar education

Similar age

Similar region

### But feels:

❌ overlooked

❌ unrecognized

❌ underserved

❌ unheard
""")


st.success("""
### Possible implication

Traditional indicators may be useful for identifying
**material and demographic differences**.

Subjective indicators may add information about
**social and democratic disconnection**.
""")

st.divider()


# ============================================================
# 4. DIFFERENT DEMOCRATIC OUTCOMES
# ============================================================

st.header("4. Democratic disconnection is not one single problem")

st.markdown("""
Feeling Left Behind does not improve model fit equally
for every democratic outcome.
""")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.metric(
            "R² gain after LBI",
            "+17.83 pp"
        )

        st.markdown("""
A large increase in model fit appears after
Feeling Left Behind is added.
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.metric(
            "R² gain after LBI",
            "+13.23 pp"
        )

        st.markdown("""
A substantial increase also appears for
Democratic Satisfaction.
""")


with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.metric(
            "Pseudo R² gain",
            "+1.32 pp"
        )

        st.markdown("""
The improvement in logistic model fit is much smaller.
""")


st.caption("""
Party Representation uses McFadden Pseudo R² and is not
on the same numeric scale as OLS R².
""")


st.success("""
### Possible implication

Distrust, dissatisfaction and lack of party representation
should not automatically be treated as the same problem.

Different forms of democratic disconnection may require
different explanations and different responses.
""")

st.divider()


# ============================================================
# 5. PRACTICAL NEXT STEPS
# ============================================================

st.header("5. What should happen next?")

st.markdown("""
The current results are better suited to **diagnosis and further research**
than to prescribing a specific intervention.
""")

c1, c2, c3 = st.columns(3)


with c1:
    with st.container(border=True):

        st.markdown("### 🔎 Measure")

        st.markdown("""
Complement traditional indicators with questions about:

- recognition;
- services;
- economic attention;
- perceived voice.
""")


with c2:
    with st.container(border=True):

        st.markdown("### 🧪 Test")

        st.markdown("""
Analyze the four Feeling Left Behind dimensions separately.

Ask:

**Which dimension is most strongly associated with each outcome?**
""")


with c3:
    with st.container(border=True):

        st.markdown("### ⏳ Follow over time")

        st.markdown("""
Use longitudinal data to test whether changes in Feeling Left Behind
come **before** changes in trust, satisfaction or representation.
""")


st.info("""
Other useful extensions include comparing:

- regions;
- income groups;
- age groups;
- social classes;
- migration-background groups.
""")

st.divider()


# ============================================================
# 6. WHAT TO CONCLUDE
# ============================================================

st.header("6. What should we conclude?")

c1, c2 = st.columns(2)


with c1:
    with st.container(border=True):

        st.markdown("### ✅ The study supports")

        st.markdown("""
- Feeling Left Behind is statistically associated with democratic attitudes.
- LBI adds explanatory information beyond traditional factors.
- The strongest model improvement appears for Trust and Satisfaction.
- Subjective social experience deserves further investigation.
""")


with c2:
    with st.container(border=True):

        st.markdown("### ❌ The study does not prove")

        st.markdown("""
- that Feeling Left Behind causes distrust;
- that one intervention will solve democratic disconnection;
- that all four LBI dimensions have the same independent effect;
- that improving one dimension will automatically improve democratic attitudes.
""")


st.divider()


# ============================================================
# FINAL TAKEAWAY
# ============================================================

st.header("Final takeaway")

st.success("""
# What people have matters.

# How people feel treated by society may matter too.

Understanding democratic disconnection may require looking at both:

**traditional socioeconomic and demographic characteristics**

and

**subjective social experience**.

The next step is to identify which mechanisms matter most
and whether they have causal effects over time.
""")

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

These policy implications are interpretations of statistical
associations and should not be treated as causal policy estimates.
""")