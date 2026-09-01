import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.title("🔎 Research")

st.subheader(
    "How the project develops from an overall index to a more precise political diagnosis"
)

st.markdown("""
The project is organized around one broader question:

### What happens when people feel unseen, insufficiently recognized, poorly served or unable to speak openly?

The research does not treat Feeling Left Behind as a single endpoint.
Instead, it tests the concept across different democratic and electoral
outcomes and then asks whether the four parts of the index carry the same
political information.
""")

st.info("""
### Research logic

**Construct the Left Behind Index**

↓

**Test whether it adds information beyond conventional characteristics**

↓

**Compare democratic attitudes and party choice**

↓

**Open the index and test its four components separately**

↓

**Test plausible alternative explanations and robustness**
""")

st.divider()


# ============================================================
# SHARED CONCEPT
# ============================================================

st.header("1. The shared concept")

st.markdown("""
The **Left Behind Index (LBI)** combines four equally weighted perceptions:

- economic attention;
- social recognition;
- access to infrastructure and basic services;
- perceived ability of people like the respondent to express opinions freely in public.

The final index runs from **1 to 5**.

**Lower values** indicate lower Feeling Left Behind.

**Higher values** indicate stronger Feeling Left Behind.
""")

st.caption(
    "The Feeling Left Behind page explains the exact GLES items, scale reversal, "
    "equal weighting and measurement checks."
)

st.divider()


# ============================================================
# SHARED CONTROLS
# ============================================================

st.header("2. What information is already taken into account?")

st.markdown("""
The central model comparisons ask whether Feeling Left Behind adds
information beyond a conventional socioeconomic, demographic and
political profile.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 💰 Socioeconomic")
        st.markdown("""
- Household Income
- Education
""")

with c2:
    with st.container(border=True):
        st.markdown("### 👥 Demographic")
        st.markdown("""
- Age
- East / West Germany
- Migration Background
""")

with c3:
    with st.container(border=True):
        st.markdown("### 🗳️ Political")
        st.markdown("""
- Political Interest
""")

st.success("""
### The recurring test

If we already know these characteristics, **does knowing how left behind
someone feels add useful information?**
""")

st.divider()


# ============================================================
# STAGE 1
# ============================================================

st.header("3. Stage 1 — Democratic attitudes")

st.info("""
### Question

**Does the overall Left Behind Index add information about Institutional
Trust, Democratic Satisfaction and Party Representation beyond the
conventional profile?**
""")

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
The GLES democratic-satisfaction item is reversed for analysis.

**Higher score = greater satisfaction**
""")
        st.metric("Analytical N", "5,571")

with c3:
    with st.container(border=True):
        st.markdown("### 👥 Party Representation")
        st.markdown("""
Whether respondents say any party represents their political views well.

**Yes / No**
""")
        st.metric("Analytical N", "5,008")

st.markdown("""
The updated analysis compares three specifications:

**Controls only → controls + overall LBI → controls + four LBI components**

This allows the project to test not only whether the overall index adds
information, but whether opening it reveals additional structure.
""")

st.divider()


# ============================================================
# STAGE 2
# ============================================================

st.header("4. Stage 2 — Party choice")

st.info("""
### Question

**Does Feeling Left Behind add useful information about reported second-vote
choice across the seven major parties in the 2025 federal election?**
""")

st.markdown("""
The analysis covers:

**CDU/CSU · SPD · FDP · Greens · Die Linke · AfD · BSW**

The common seven-party analytical sample contains **4,879 respondents**.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### Model A")
        st.markdown("""
**Conventional voter profile**

Income · Education · Age · Region · Migration Background · Political Interest
""")

with c2:
    with st.container(border=True):
        st.markdown("### Model B")
        st.markdown("""
**Conventional profile + overall LBI**

Tests whether the combined index adds predictive information.
""")

with c3:
    with st.container(border=True):
        st.markdown("### Model C")
        st.markdown("""
**Conventional profile + four LBI components**

Tests whether the four items are more informative when kept separate.
""")

st.markdown("""
### Testing on unseen voters

The models use **repeated stratified cross-validation**:

**5 folds × 10 repetitions = 50 held-out evaluations**

The model learns from one part of the data and is evaluated on respondents
it did not use for fitting.
""")

st.success("""
The four-component model outperformed the overall-LBI model in **all 50
repeated evaluations** on accuracy and macro-F1, and also produced lower
log loss in all 50 evaluations.
""")

st.divider()


# ============================================================
# STAGE 3
# ============================================================

st.header("5. Stage 3 — Opening the Left Behind Index")

st.info("""
### Question

**Do the four equally weighted LBI components show equally strong
relationships with political outcomes?**
""")

st.markdown("""
For party choice, the fitted multiclass model is converted into an easier
comparison. Each component is moved from **1 to 4** while the other
modeled characteristics remain unchanged, and the change in average
estimated party probability is calculated.

For Institutional Trust and Democratic Satisfaction, the four components
are compared in adjusted regression models using standardized coefficients.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric("AfD: public expression", "+34.1 pp")
        st.caption("Estimated probability change when the item moves 1 → 4.")

with c2:
    with st.container(border=True):
        st.metric("Trust: public expression", "β = −0.37")
        st.caption("Standardized adjusted association.")

with c3:
    with st.container(border=True):
        st.metric("Satisfaction: public expression", "β = −0.36")
        st.caption("Standardized adjusted association.")

st.warning("""
These numbers describe **model-based associations**, not causal effects.
The four components still have exactly the same arithmetic weight in the
Left Behind Index.
""")

st.divider()


# ============================================================
# ALTERNATIVE EXPLANATION
# ============================================================

st.header("6. Is the public-expression result simply left-right ideology?")

st.markdown("""
The GLES asks respondents to place themselves on a left-right scale from
**1 = Left** to **11 = Right**, with **6 = Centre**.

The party analysis is repeated while taking that self-placement into account.
""")

st.metric(
    "AfD public-expression association after left-right adjustment",
    "about 14% smaller"
)

st.markdown("""
The AfD relationship remains strong. The negative patterns for Greens and
SPD also remain substantial. By contrast, the earlier public-expression
patterns for Die Linke and FDP largely disappear after left-right position
is included.
""")

st.success("""
### Interpretation

Political position accounts for **part** of the strongest public-expression
relationship, but not most of it.
""")

st.divider()


# ============================================================
# PROSPECTIVE EXTENSION
# ============================================================

st.header("7. Prospective extension — Saxony-Anhalt")

st.markdown("""
Saxony-Anhalt remains a separate extension of the project.

The historical GLES relationship is compared with the political context
before the 2026 state election. The external polling benchmark is **not**
used to fit the historical model.
""")

st.warning("""
### What this exercise is not

It is not an opinion poll.

It is not a formal vote-share forecast.

It is not evidence that Feeling Left Behind alone explains
Saxony-Anhalt's party landscape.
""")

st.divider()


# ============================================================
# CLAIMS
# ============================================================

st.header("8. What can the research claim?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### ✅ Supported")
        st.markdown("""
- Feeling Left Behind is associated with democratic attitudes.
- The overall LBI adds information beyond the conventional profile.
- The four components contain additional information for some outcomes.
- Public expression stands out especially for AfD support, Institutional Trust and Democratic Satisfaction.
- The AfD public-expression relationship remains strong after left-right self-placement is included.
- Component patterns differ across party electorates.
""")

with c2:
    with st.container(border=True):
        st.markdown("### ❌ Not established")
        st.markdown("""
- Causal effects of Feeling Left Behind.
- That Germany objectively restricts freedom of expression.
- What opinions respondents have in mind when answering the public-expression item.
- Exact individual vote prediction.
- A causal explanation for AfD, Green or SPD support.
- A precise 2026 Saxony-Anhalt vote-share forecast.
""")

st.divider()

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

The analyses use observational survey data and should be interpreted as
associational rather than causal.
""")
