import streamlit as st
import pandas as pd


# ============================================================
# PAGE
# ============================================================

st.title("🔬 Methodology")

st.subheader(
    "How survey responses become the Left Behind Index, adjusted models and robustness tests"
)

st.info("""
### Methodological sequence

**Survey responses → index construction → outcome-specific samples → adjusted models → held-out evaluation → robustness checks → cautious interpretation**
""")

st.divider()


# ============================================================
# DATA
# ============================================================

st.header("1. Data")

st.markdown("""
The project uses the **German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0**.
""")

c1, c2 = st.columns(2)

c1.metric("Original respondents", "7,336")
c2.metric("Complete four-item LBI", "6,831")

st.markdown("""
The analyses use **complete-case samples** for the variables required by
each model comparison. Within a given comparison, the specifications are
estimated on the same respondents whenever possible so that changes in
model fit are not driven simply by a different sample.
""")

sample_df = pd.DataFrame({
    "Analysis": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation",
        "Seven-party choice",
        "Left-right matched robustness"
    ],
    "N": [5444, 5571, 5008, 4879, 4757]
})

st.dataframe(sample_df, width="stretch", hide_index=True)

st.divider()


# ============================================================
# LBI
# ============================================================

st.header("2. Constructing the Left Behind Index")

st.markdown("""
The LBI is a **project-constructed index**, not an official GLES scale.
It uses four GLES items:

1. Economic attention (`q46a`)
2. Social recognition (`q46b`)
3. Infrastructure and basic services (`q46c`)
4. Perceived freedom of public expression (`q46d`)

The original items run from **1 = strongly agree** to **5 = strongly
disagree**. Because agreement with the negative statements indicates
stronger Feeling Left Behind, each item is reversed:
""")

st.code("reversed_score = 6 - original_score", language="python")

st.markdown("""
The four reversed items are then averaged:

### LBI = (economic + recognition + services + public expression) / 4

All four items therefore have **equal arithmetic weight**.
""")

st.warning("""
A stronger statistical relationship between one component and an outcome
does not mean that the component is weighted more heavily in the LBI.
""")

st.divider()


# ============================================================
# MEASUREMENT
# ============================================================

st.header("3. Measurement checks")

c1, c2 = st.columns(2)

c1.metric("Cronbach's α: four items", "0.753")
c2.metric("Cronbach's α without public expression", "0.757")

st.markdown("""
The four-item alpha indicates acceptable internal consistency. Removing
the public-expression item increases alpha by only about **0.004**.

The public-expression item is somewhat distinct, but the reliability
check does not provide a strong reason to remove it from the index.
""")

st.divider()


# ============================================================
# CONTROLS
# ============================================================

st.header("4. Conventional characteristics")

controls = pd.DataFrame({
    "Variable": [
        "Household Income",
        "Education",
        "Age",
        "East / West Germany",
        "Migration Background",
        "Political Interest"
    ],
    "Role": [
        "Socioeconomic control",
        "Socioeconomic control",
        "Demographic control",
        "Geographic control",
        "Demographic control",
        "Political control"
    ]
})

st.dataframe(controls, width="stretch", hide_index=True)

st.caption(
    "Age is also modeled with a squared term in the national democratic-attitudes analyses."
)

st.divider()


# ============================================================
# DEMOCRATIC ATTITUDES
# ============================================================

st.header("5. Democratic-attitudes models")

st.markdown("""
Three outcomes are examined:

- **Institutional Trust**: mean of eight GLES trust items, with higher values meaning more trust;
- **Democratic Satisfaction**: the GLES satisfaction item reversed so higher values mean greater satisfaction;
- **Party Representation**: whether respondents say a party represents their political views well.

Institutional Trust and Democratic Satisfaction use adjusted linear
regression. Party Representation uses binary logistic regression.
""")

st.markdown("""
For each outcome, the updated comparison considers:

**Controls only**

→ **Controls + overall LBI**

→ **Controls + four LBI components**
""")

st.info("""
### Why standardize the component models?

For Trust and Satisfaction, the four LBI components are standardized so
that their adjusted coefficients can be compared on a common scale.

For Party Representation, the component results are expressed as odds
ratios for a one-standard-deviation increase.
""")

st.divider()


# ============================================================
# PARTY CHOICE
# ============================================================

st.header("6. Party-choice model")

st.markdown("""
Party choice is a **seven-category outcome**, so the project uses
multinomial logistic regression.

The common analytical sample includes confirmed second-vote choices for:

**CDU/CSU · SPD · FDP · Greens · Die Linke · AfD · BSW**
""")

party_models = pd.DataFrame({
    "Specification": [
        "Conventional profile",
        "Conventional profile + overall LBI",
        "Conventional profile + four LBI components"
    ],
    "Mean held-out accuracy": ["35.8%", "38.2%", "39.9%"]
})

st.dataframe(party_models, width="stretch", hide_index=True)

st.divider()


# ============================================================
# CROSS VALIDATION
# ============================================================

st.header("7. Repeated cross-validation")

st.markdown("""
The party-choice models are evaluated using **RepeatedStratifiedKFold**:

### 5 folds × 10 repetitions = 50 held-out evaluations

Each fitted model learns from one part of the sample and is evaluated on
respondents not used in that fit. Repeating the procedure reduces the
chance that the conclusion depends on one favorable train-test split.
""")

st.success("""
The four-component model beats the overall-LBI model in all **50/50**
evaluations on accuracy and macro-F1, and has lower log loss in all 50.
""")

st.divider()


# ============================================================
# SCENARIO PROBABILITIES
# ============================================================

st.header("8. Component probability scenarios")

st.markdown("""
To make the multinomial model easier to interpret, each LBI component is
examined using the same scenario:

1. Fit the full four-component party-choice model.
2. Keep each respondent's other modeled characteristics unchanged.
3. Set one LBI component to **1** and calculate party probabilities.
4. Set the same component to **4** and calculate probabilities again.
5. Average the predicted probabilities across respondents.
6. Report the difference in **percentage points**.
""")

st.warning("""
### Interpretation

This is an **adjusted model-implied association**.

It does not show what would causally happen if a person's perception were
changed from 1 to 4.
""")

st.divider()


# ============================================================
# BOOTSTRAP
# ============================================================

st.header("9. Bootstrap uncertainty checks")

st.markdown("""
The component-party probability scenarios are also checked using
**500 bootstrap resamples** for the main parties and components.

The bootstrap repeatedly resamples respondents, refits the model and
recalculates the scenario differences. This provides an empirical check
on whether the most prominent relationships are stable across resampled
versions of the data.
""")

st.info("""
The strongest public-expression relationships, especially the AfD
contrast, remain stable in the bootstrap checks. The economic-attention
relationships are generally smaller.
""")

st.divider()


# ============================================================
# LEFT-RIGHT
# ============================================================

st.header("10. Left-right robustness")

st.markdown("""
A plausible alternative explanation is that the public-expression item
simply reflects respondents' existing ideological position.

The GLES asks respondents to place themselves on a scale from:

**1 = Left · 6 = Centre · 11 = Right**

The party models are therefore repeated while adding this self-reported
left-right position.
""")

st.markdown("""
For the key comparison, models with and without ideology are estimated on
the **same matched sample of 4,757 respondents**.

The AfD public-expression coefficient becomes about **14.4% smaller**, but
remains strong. The Greens and SPD patterns also remain, while the Die
Linke and FDP patterns largely disappear.
""")

st.success("""
### Methodological interpretation

Left-right self-placement accounts for part of the relationship, but not
most of the strongest AfD association.
""")

st.divider()


# ============================================================
# GEOGRAPHY
# ============================================================

st.header("11. Geographic comparisons")

st.markdown("""
East-West and state-level LBI averages are used **descriptively**.

These comparisons describe where average Feeling Left Behind is higher or
lower in the analytical sample. They are not treated as causal regional
effects.
""")

st.warning("""
State samples vary substantially in size. Small-state estimates should be
interpreted cautiously, particularly when used for descriptive ranking.
""")

st.divider()


# ============================================================
# LIMITATIONS
# ============================================================

st.header("12. What the methods cannot establish")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### The analyses can estimate")
        st.markdown("""
- adjusted statistical associations;
- changes in model fit;
- held-out predictive performance;
- model-implied probability contrasts;
- robustness to alternative specifications;
- descriptive geographic differences.
""")

with c2:
    with st.container(border=True):
        st.markdown("### The analyses cannot establish")
        st.markdown("""
- causal effects of Feeling Left Behind;
- the causal direction between attitudes and political outcomes;
- objective restriction of freedom of expression;
- the content of opinions respondents have in mind;
- exact individual vote prediction;
- a causal explanation for party support.
""")

st.divider()

st.caption("""
Primary source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

The Left Behind Index is constructed for this project and is not an
official GLES scale.
""")
