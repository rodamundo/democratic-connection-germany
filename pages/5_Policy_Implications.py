import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.title("💡 Policy Implications")

st.subheader(
    "What might Feeling Left Behind tell us about the quality of "
    "the relationship between citizens and politics?"
)

st.markdown("""
The goal of this page is not to turn statistical associations into
a list of policy prescriptions.

It is to ask what the findings may contribute to the diagnosis of
**democratic disconnection, representation and political responsiveness**.
""")

st.warning("""
### Association is not causation

The analyses use cross-sectional observational survey data.

They do not show that a specific intervention will automatically
increase trust, satisfaction, representation or support for a
particular political party.
""")

st.divider()


# ============================================================
# 1. MAIN MESSAGE
# ============================================================

st.header("1. The main policy message")

st.markdown("""
Traditional indicators such as income, education, age and region
remain important.

But the results suggest that these indicators may not capture the
whole relationship between citizens and politics.
""")

st.success("""
# A useful question is not only:

### “What resources do people have?”

# It is also:

### “Do people feel that people like them are seen, recognized,
### served and heard?”
""")

st.markdown("""
That distinction matters because two people with similar conventional
profiles may still experience their relationship with society and
politics very differently.
""")

st.divider()


# ============================================================
# 2. STUDY 1
# ============================================================

st.header("2. Study 1: democratic attitudes")

st.markdown("""
The first study finds that adding Feeling Left Behind to a conventional
profile produces substantial improvements in the models for
**Institutional Trust** and **Democratic Satisfaction**.

The improvement is much smaller for the broader question of whether
respondents feel represented by any political party.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Trust")

        st.metric(
            "Model fit",
            "8.46% → 26.29%",
            "+17.83 pp"
        )

        st.caption("OLS R²")

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Satisfaction")

        st.metric(
            "Model fit",
            "7.97% → 21.20%",
            "+13.23 pp"
        )

        st.caption("OLS R²")

with c3:
    with st.container(border=True):

        st.markdown("### 👥 Representation")

        st.metric(
            "Model fit",
            "3.33% → 4.65%",
            "+1.32 pp"
        )

        st.caption("McFadden Pseudo R²")

st.info("""
### Interpretation

Democratic disconnection should not automatically be treated as
one single problem.

Distrust, dissatisfaction and lack of party representation may have
overlapping causes, but they are not the same political experience.
""")

st.divider()


# ============================================================
# 3. STUDY 2
# ============================================================

st.header("3. Study 2: party choice")

st.markdown("""
The second study adds an important qualification.

Feeling Left Behind does **not** transform party-choice prediction
across the whole party system. The overall improvement is modest.

But the average hides a much stronger contrast between specific
electorates, especially AfD and Green voters.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric(
            "Conventional profile",
            "35.9%"
        )
        st.caption("Correct party classifications")

with c2:
    with st.container(border=True):
        st.metric(
            "+ Feeling Left Behind",
            "38.1%"
        )
        st.caption("Correct party classifications")

with c3:
    with st.container(border=True):
        st.metric(
            "Improvement",
            "+2.2 pp"
        )
        st.caption("Modest overall gain")

st.markdown("""
When the same conventional voter profiles are used and only the
Left Behind Index is changed from 1 to 4:

- the estimated AfD probability rises from **1.7% to 33.7%**;
- the estimated Green probability falls from **37.7% to 5.0%**.
""")

st.warning("""
These are model-based estimates.

They do not show that a person would change parties if their Feeling
Left Behind score changed.
""")

st.divider()


# ============================================================
# 4. WHAT THIS MEANS FOR POLITICAL PRACTICE
# ============================================================

st.header("4. What might this mean for political practice?")

st.markdown("""
The practical implication is **not** that political organisations
should identify and target people with a high Left Behind Index.

A more useful question is what political institutions and leaders
can change so that fewer citizens feel overlooked, unrecognized,
poorly served or unheard in the first place.
""")

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 👀 Seen")
        st.markdown(
            "Do citizens feel that their economic concerns receive attention?"
        )

with c2:
    with st.container(border=True):
        st.markdown("### 👏 Recognized")
        st.markdown(
            "Do people feel that their contribution is socially recognized?"
        )

with c3:
    with st.container(border=True):
        st.markdown("### 🏥 Served")
        st.markdown(
            "Do people feel they have adequate access to services and infrastructure?"
        )

with c4:
    with st.container(border=True):
        st.markdown("### 🗣️ Heard")
        st.markdown(
            "Do people feel able to express their views and be listened to?"
        )

st.success("""
### The broader point

Feeling Left Behind can be treated as a **diagnostic signal about the
quality of connection between citizens and politics**, rather than as
a label for a particular demographic or electorate.
""")

st.divider()


# ============================================================
# 5. SAXONY-ANHALT
# ============================================================

st.header("5. Why Saxony-Anhalt is useful as a test")

st.markdown("""
Saxony-Anhalt does not provide a causal experiment, and the Left Behind
Index is not a substitute for polling.

Its value in this project is different.

Respondents from Saxony-Anhalt have the highest average LBI among the
16 states in the party-choice analytical sample. The state therefore
offers a useful context in which to ask whether a historical pattern
associated with Feeling Left Behind remains recognizable before the
votes are counted.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric(
            "Saxony-Anhalt mean LBI",
            "2.84"
        )

with c2:
    with st.container(border=True):
        st.metric(
            "Rest of Germany",
            "2.49"
        )

st.info("""
The historical LBI-only benchmark and the frozen 2026 polling benchmark
place the seven parties in the same order, but the historical benchmark
does not reproduce the magnitude of AfD's polling advantage.

That is why the benchmark should be used for **interpretation**, not
precise vote-share forecasting.
""")

st.divider()


# ============================================================
# 6. PRACTICAL NEXT STEPS
# ============================================================

st.header("6. What should happen next?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🔎 Measure")

        st.markdown("""
Track not only material conditions, but also perceptions of:

- attention;
- recognition;
- services;
- voice.
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🧪 Diagnose")

        st.markdown("""
Test which dimensions are most strongly related to:

- trust;
- satisfaction;
- representation;
- party choice.
""")

with c3:
    with st.container(border=True):

        st.markdown("### ⏳ Follow over time")

        st.markdown("""
Use longitudinal evidence to ask whether changes in Feeling Left Behind
come before changes in democratic attitudes or electoral behaviour.
""")

st.divider()


# ============================================================
# 7. CONCLUSION
# ============================================================

st.header("7. What should we conclude?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### ✅ The evidence supports")

        st.markdown("""
- Feeling Left Behind is associated with democratic attitudes.
- It adds information beyond conventional characteristics.
- Its added value differs across political outcomes.
- AfD and Green voters show the clearest party-choice contrast.
- The concept may be useful as a diagnostic tool for political disconnection.
""")

with c2:
    with st.container(border=True):

        st.markdown("### ❌ The evidence does not prove")

        st.markdown("""
- that Feeling Left Behind causes distrust or a particular vote;
- that one intervention will solve democratic disconnection;
- that the four LBI dimensions have identical effects;
- that the LBI can replace polling;
- that the historical model precisely forecasts Saxony-Anhalt.
""")

st.divider()

st.success("""
# Final takeaway

Political systems need to understand not only **who citizens are**,
but also **how citizens experience their relationship with society
and politics**.

The most useful question is not how to target people who feel left
behind. It is what can be changed so that fewer people feel unseen,
unheard or poorly served in the first place.
""")

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

The Saxony-Anhalt polling comparison is a descriptive external benchmark.
It is not used to train the machine-learning model.
""")
