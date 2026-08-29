import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.title("🔎 Research")

st.subheader(
    "How the Feeling Left Behind research develops from "
    "democratic attitudes to party choice"
)

st.markdown("""
The project is built around one broader question:

### What happens when people feel unseen, unheard or poorly served by politics?

Rather than treating this as a single outcome, the research examines
different parts of the relationship between citizens and politics.
""")

st.info("""
### Research logic

**Measure Feeling Left Behind**

↓

**Ask whether it adds information beyond conventional characteristics**

↓

**Test that question across different democratic and electoral outcomes**
""")

st.divider()


# ============================================================
# SHARED CONCEPT
# ============================================================

st.header("1. The shared concept")

st.markdown("""
The **Left Behind Index** combines four perceptions:

- economic attention;
- social recognition;
- access to services and infrastructure;
- voice and freedom to express views.

The index runs from **1 to 5**.

**Lower values** indicate lower Feeling Left Behind.

**Higher values** indicate stronger Feeling Left Behind.
""")

st.caption(
    "The construction and validation of the index are explained "
    "in the Feeling Left Behind page."
)

st.divider()


# ============================================================
# SHARED CONVENTIONAL PROFILE
# ============================================================

st.header("2. What information is already taken into account?")

st.markdown("""
Both studies ask whether Feeling Left Behind adds information beyond
a conventional socioeconomic, demographic and political profile.
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
The recurring question is simple:

### If we already know these characteristics, does knowing how left behind
### someone feels add useful information?
""")

st.divider()


# ============================================================
# STUDY 1
# ============================================================

st.header("3. Study 1 - Democratic attitudes")

st.markdown("""
The first study asks whether Feeling Left Behind helps us understand
three different aspects of people's relationship with democracy.
""")

st.info("""
### Study 1 research question

**Does Feeling Left Behind help us understand Institutional Trust,
Democratic Satisfaction and Party Representation beyond conventional
socioeconomic, demographic and political characteristics?**
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Average trust across eight institutions.

**Scale: 1 to 11**

Higher values mean higher trust.
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
Satisfaction with how democracy works in Germany.

**Scale: 1 to 4**

Higher values mean greater dissatisfaction.
""")

with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.markdown("""
Whether any political party represents the respondent's
political views well.

**Yes / No**
""")

st.markdown("""
### Study 1 model design

For each outcome, the analysis compares:

**Model 1**

Conventional characteristics

versus

**Model 2**

Conventional characteristics + Left Behind Index
""")

st.caption(
    "Institutional Trust and Democratic Satisfaction use multiple OLS "
    "regression. Party Representation uses binary logistic regression."
)

st.divider()


# ============================================================
# STUDY 2
# ============================================================

st.header("4. Study 2 - Party choice")

st.markdown("""
The second study moves from the broad question of whether someone feels
represented by any party to the party they reported choosing in the
2025 federal election.
""")

st.info("""
### Study 2 research question

**Can Feeling Left Behind improve our understanding of party choice
beyond conventional voter characteristics?**
""")

st.markdown("""
The analysis covers seven parties:

**CDU/CSU · SPD · FDP · Greens · The Left · AfD · BSW**
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### Model A")

        st.markdown("""
**LBI only**

How much information does Feeling Left Behind contain on its own?
""")

with c2:
    with st.container(border=True):

        st.markdown("### Model B")

        st.markdown("""
**Conventional voter profile**

Income · Education · Age · Region ·
Migration Background · Political Interest
""")

with c3:
    with st.container(border=True):

        st.markdown("### Model C")

        st.markdown("""
**Conventional profile + LBI**

Does Feeling Left Behind add information beyond the baseline profile?
""")

st.markdown("""
### Testing on unseen voters

The party-choice model is evaluated using repeated cross-validation:

**5 folds × 10 repetitions = 50 held-out model evaluations**

In each fold, the model learns from four groups of voters and is tested
on the fifth group, which it did not see during training.
""")

st.success("""
### Why this matters

The test asks whether Feeling Left Behind helps with voters the model
did not already know, rather than only improving the fit to the data
used for training.
""")

st.divider()


# ============================================================
# STANDARDIZED PROBABILITIES
# ============================================================

st.header("5. A second question inside the party-choice study")

st.markdown("""
Party averages can be influenced by differences in age, income,
education, region and other characteristics.

The analysis therefore performs an additional model-based calculation.

For every respondent:

1. Keep the conventional voter characteristics unchanged.
2. Set the Left Behind Index to **1**.
3. Calculate party probabilities.
4. Set the Left Behind Index to **4**.
5. Calculate the probabilities again.
6. Average the estimated probabilities across voters.
""")

st.warning("""
### Interpretation

This is an **adjusted model-based association**.

It does not show that making a person feel more left behind would
cause them to change their vote.
""")

st.divider()


# ============================================================
# SAXONY-ANHALT
# ============================================================

st.header("6. The prospective Saxony-Anhalt extension")

st.markdown("""
The final stage asks whether a relationship learned from historical
individual-level data can help interpret a new electoral context
before the result is known.
""")

st.info("""
### Prospective question

**Do party-choice patterns identified in historical individual-level
data help interpret the changing party landscape in Saxony-Anhalt
before the 2026 state-election result is known?**
""")

st.markdown("""
The comparison uses:

- a historical LBI-only benchmark learned from voters in the same
  East German regional category, excluding Saxony-Anhalt;
- a descriptive 2026 polling benchmark for Saxony-Anhalt;
- the same seven parties used in the historical party-choice analysis.

The polling benchmark is external. It is **not used to train the model**.
""")

st.warning("""
### What this prospective exercise is not

It is not an opinion poll.

It is not a formal vote-share forecast.

It is not evidence that Feeling Left Behind alone explains
Saxony-Anhalt's political landscape.
""")

st.divider()


# ============================================================
# CLAIMS
# ============================================================

st.header("7. What can each study claim?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### ✅ Supported")

        st.markdown("""
- Statistical associations between Feeling Left Behind and democratic attitudes.
- Additional explanatory information beyond the conventional profile.
- Modest overall improvement in party-choice prediction.
- A particularly strong AfD-Green contrast in the party-choice model.
- A descriptive historical comparison with the 2026 Saxony-Anhalt context.
""")

with c2:
    with st.container(border=True):

        st.markdown("### ❌ Not established")

        st.markdown("""
- Causal effects of Feeling Left Behind.
- Exact individual vote prediction.
- A causal explanation for AfD or Green support.
- A precise 2026 Saxony-Anhalt vote-share forecast.
- Proof that one policy intervention would change trust or voting behaviour.
""")

st.divider()

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The studies use observational survey data and should be interpreted
as associational rather than causal.
""")
