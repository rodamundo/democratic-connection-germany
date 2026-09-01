import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.title("💡 Political Diagnosis")

st.subheader(
    "What the evidence suggests, what it does not establish, and what political leadership can learn from the distinction"
)

st.markdown("""
The purpose of this page is **not** to turn statistical associations into
a list of policy prescriptions.

The project is more useful as a diagnostic exercise: identify where
political disconnection appears, distinguish different forms of it, test
plausible explanations and remain clear about what the evidence cannot tell us.
""")

st.warning("""
### Association is not causation

The analyses use cross-sectional observational survey data.
They do not show that changing one LBI component would automatically
change trust, democratic satisfaction or party support.
""")

st.divider()


# ============================================================
# MAIN DIAGNOSIS
# ============================================================

st.header("1. The main diagnosis")

st.markdown("""
The overall Left Behind Index is associated with democratic attitudes and
party choice. But opening the index reveals that the four components do
not carry the same political information.
""")

st.success("""
### The clearest pattern

Among the four forms of Feeling Left Behind measured here,
**perceived inability to express opinions freely in public stands out most
strongly in relation to AfD support, lower Institutional Trust and lower
Democratic Satisfaction**.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric("AfD", "+34.1 pp")
        st.caption("Public-expression scenario, item 1 → 4")

with c2:
    with st.container(border=True):
        st.metric("Institutional Trust", "β = −0.37")
        st.caption("Standardized adjusted association")

with c3:
    with st.container(border=True):
        st.metric("Democratic Satisfaction", "β = −0.36")
        st.caption("Standardized adjusted association")

st.divider()


# ============================================================
# NOT UNIVERSAL
# ============================================================

st.header("2. The diagnosis is specific, not universal")

st.markdown("""
The public-expression item does not dominate every outcome or every party.

- For the Greens and SPD, the relationship points strongly in the opposite direction from AfD.
- BSW shows a more mixed economic and public-expression profile.
- CDU/CSU and FDP show no comparably dominant LBI component in the national model.
- The public-expression item is not statistically significant in the generic Party Representation model.

This matters because **democratic disconnection is not one single problem**.
Different political outcomes can be associated with different combinations
of perceived neglect, recognition, services and public expression.
""")

st.divider()


# ============================================================
# LEFT RIGHT
# ============================================================

st.header("3. Test an obvious alternative explanation")

st.markdown("""
A straightforward explanation is that the public-expression result merely
reflects respondents who already place themselves further to the political right.

The project tests that directly using respondents' own left-right
self-placement.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric("AfD association", "~14% smaller")
        st.caption("After adding left-right self-placement")

with c2:
    with st.container(border=True):
        st.metric("Matched sample", "4,757")
        st.caption("Same respondents before and after ideology adjustment")

st.success("""
Political position accounts for **part** of the relationship, but not most
of the strongest AfD association.
""")

st.divider()


# ============================================================
# PERCEPTION BOUNDARY
# ============================================================

st.header("4. Take the perception seriously without treating it as fact")

st.markdown("""
The exact GLES statement is:

> **“People like me are no longer allowed to freely express their opinions in public.”**

The survey tells us whether people agree with this statement.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### ✅ What the survey can show")
        st.markdown("""
- whether respondents agree with the statement;
- how that perception varies with political outcomes;
- whether the relationship remains after measured controls are included;
- whether some alternative explanations reduce the relationship.
""")

with c2:
    with st.container(border=True):
        st.markdown("### ❌ What the survey cannot show")
        st.markdown("""
- what opinions respondents have in mind;
- what they believe prevents them from speaking;
- whether the perceived restriction is objectively present;
- whether the perception causes a particular political outcome.
""")

st.info("""
### Why this distinction matters

Taking a perception seriously does not require accepting it as an
objective fact. It means recognizing that the perception itself may be
politically consequential and worth understanding more precisely.
""")

st.divider()


# ============================================================
# LEADERSHIP QUESTIONS
# ============================================================

st.header("5. What questions can political leadership take from this?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 🔎 Distinguish")
        st.markdown("""
Do not assume that all forms of Feeling Left Behind are interchangeable.

Separate economic attention, recognition, services and public expression.
""")

with c2:
    with st.container(border=True):
        st.markdown("### 🧪 Test")
        st.markdown("""
Ask whether an apparent political pattern survives plausible alternative
explanations rather than beginning from a preferred interpretation.
""")

with c3:
    with st.container(border=True):
        st.markdown("### 📏 Measure")
        st.markdown("""
Track perceptions alongside material conditions so that political
responses start from a more precise diagnosis of the problem.
""")

st.markdown("""
The evidence does not identify a single intervention. It helps clarify
**which problem political leaders may actually be looking at** before a
response is chosen.
""")

st.divider()


# ============================================================
# SAXONY-ANHALT
# ============================================================

st.header("6. Why the geographic extension still matters")

st.markdown("""
Saxony-Anhalt remains useful as a prospective context because its average
LBI is high in the historical party-choice sample.

The project compares historical patterns with the political context ahead
of the 2026 state election, but treats that comparison as a **directional
benchmark**, not a formal forecast.
""")

c1, c2 = st.columns(2)

c1.metric("Saxony-Anhalt mean LBI", "2.84")
c2.metric("Rest of Germany", "2.49")

st.warning("""
The LBI does not replace polling, and the historical model should not be
used as a precise vote-share forecast.
""")

st.divider()


# ============================================================
# NEXT RESEARCH
# ============================================================

st.header("7. What should be tested next?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 💬 Understand the perception")
        st.markdown("""
Use qualitative or more detailed survey evidence to learn what respondents
mean when they say people like them cannot speak freely.
""")

with c2:
    with st.container(border=True):
        st.markdown("### ⏳ Follow change over time")
        st.markdown("""
Use longitudinal evidence to examine whether changes in these perceptions
precede or follow changes in democratic attitudes and electoral behaviour.
""")

with c3:
    with st.container(border=True):
        st.markdown("### 🗺️ Compare contexts")
        st.markdown("""
Test whether the same component patterns appear in different German
regions, elections and political environments.
""")

st.divider()


# ============================================================
# CONCLUSION
# ============================================================

st.header("8. Final takeaway")

st.success("""
Political leadership needs to know **which problem it is looking at before
deciding how to respond**.

The overall Left Behind Index tells us where perceived disconnection is
stronger. Opening the index shows that the **form of that disconnection
matters too**.

### That is a diagnosis political leaders can work with.
""")

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

All findings are observational and should not be interpreted as causal effects.
""")
