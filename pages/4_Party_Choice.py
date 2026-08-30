import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE
# ============================================================

st.title("🗳️ Feeling Left Behind and Party Choice")

st.subheader(
    "Where the Left Behind Index adds information, and what the "
    "pattern may tell us before Saxony-Anhalt votes"
)

st.markdown("""
The main finding is not that Feeling Left Behind predicts everyone's vote.

Across the seven-party system, the overall improvement is modest.

But **AfD and Green voters stand out**.
""")

st.info("""
### Main question

**Can Feeling Left Behind improve our understanding of party choice
beyond conventional voter characteristics?**
""")

st.divider()


# ============================================================
# 1. ANALYTICAL DESIGN
# ============================================================

st.header("1. What is being predicted?")

st.markdown("""
The target is respondents' reported **second vote in the 2025 federal election**.

The analysis includes seven parties:

**CDU/CSU · SPD · FDP · Greens · The Left · AfD · BSW**
""")

st.markdown("""
Three models are compared:
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### Model 1")
        st.markdown("""
**LBI only**

Feeling Left Behind as the only predictor.
""")

with c2:
    with st.container(border=True):
        st.markdown("### Model 2")
        st.markdown("""
**Conventional profile**

Income · Education · Age · East/West ·
Migration Background · Political Interest
""")

with c3:
    with st.container(border=True):
        st.markdown("### Model 3")
        st.markdown("""
**Conventional profile + LBI**

The same voter profile plus Feeling Left Behind.
""")

st.markdown("""
### Testing on unseen voters

The models use repeated stratified cross-validation:

**5 folds × 10 repetitions = 50 held-out evaluations**
""")

st.caption(
    "The model learns from four groups and is tested on the fifth. "
    "The groups rotate, the sample is reshuffled and the procedure repeats."
)

st.divider()


# ============================================================
# 2. OVERALL GAIN
# ============================================================

st.header("2. The overall improvement is modest")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric(
            "Conventional profile",
            "35.8%"
        )
        st.caption("Correct party classifications")

with c2:
    with st.container(border=True):
        st.metric(
            "Conventional + LBI",
            "38.2%"
        )
        st.caption("Correct party classifications")

with c3:
    with st.container(border=True):
        st.metric(
            "Improvement",
            "+2.3 pp"
        )
        st.caption("About a 6.5% relative increase in correct classifications")

st.markdown("""
The improvement is highly consistent across the repeated tests.
Accuracy improved in **49 of 50 held-out evaluations**, while
**macro F1 and log loss improved in all 50**.

The Left Behind Index therefore adds information beyond the conventional
voter profile, although the size of the overall gain remains modest.
""")

st.success("""
### This changes the question

The interesting result is not that Feeling Left Behind transforms
prediction across the whole party system.

The interesting question is **where that additional information is strongest**.
""")

st.divider()


# ============================================================
# 3. PARTY AVERAGES
# ============================================================

st.header("3. AfD and Green voters occupy opposite ends of the index")

party_lbi = pd.DataFrame({
    "Party": [
        "AfD",
        "BSW",
        "FDP",
        "The Left",
        "CDU/CSU",
        "SPD",
        "Greens"
    ],
    "Average LBI": [
        3.30,
        2.87,
        2.57,
        2.50,
        2.47,
        2.35,
        2.01
    ]
})

party_lbi = party_lbi.sort_values(
    "Average LBI",
    ascending=False
)

fig = px.bar(
    party_lbi,
    x="Party",
    y="Average LBI",
    text="Average LBI",
    title="Average Left Behind Index by 2025 Party Choice"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig.update_layout(
    height=500,
    xaxis_title="",
    yaxis_title="Average Left Behind Index",
    yaxis=dict(range=[0, 3.7])
)

st.plotly_chart(
    fig,
    width="stretch"
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "AfD average",
    "3.30"
)

c2.metric(
    "Greens average",
    "2.01"
)

c3.metric(
    "Difference",
    "1.29 points"
)

st.caption("""
These are raw descriptive averages. They do not control for differences
in age, income, education, region or other voter characteristics.
""")

st.divider()


# ============================================================
# 4. STANDARDIZED PROBABILITIES
# ============================================================

st.header("4. What happens when only Feeling Left Behind changes?")

st.markdown("""
To separate the LBI contrast from the conventional voter profile,
the fitted model is used for one additional calculation.

For each respondent, age, income, education, East/West region,
migration background and political interest are kept unchanged.

Only the Left Behind Index is changed:

**LBI = 1**

versus

**LBI = 4**
""")

probabilities = pd.DataFrame({
    "Party": [
        "AfD",
        "Greens",
        "CDU/CSU",
        "SPD",
        "The Left",
        "BSW",
        "FDP"
    ],
    "LBI 1": [
        1.71,
        37.76,
        23.70,
        19.78,
        12.07,
        2.27,
        2.71
    ],
    "LBI 4": [
        33.71,
        5.01,
        27.83,
        9.34,
        9.33,
        8.48,
        6.30
    ]
})

probabilities["Change (pp)"] = (
    probabilities["LBI 4"]
    - probabilities["LBI 1"]
)

display_probabilities = probabilities.copy()

display_probabilities["LBI 1"] = display_probabilities["LBI 1"].map(
    lambda x: f"{x:.1f}%"
)

display_probabilities["LBI 4"] = display_probabilities["LBI 4"].map(
    lambda x: f"{x:.1f}%"
)

display_probabilities["Change (pp)"] = display_probabilities[
    "Change (pp)"
].map(
    lambda x: f"{x:+.1f}"
)

st.dataframe(
    display_probabilities,
    width="stretch",
    hide_index=True
)

plot_probabilities = probabilities.melt(
    id_vars="Party",
    value_vars=["LBI 1", "LBI 4"],
    var_name="Scenario",
    value_name="Estimated probability"
)

fig = px.bar(
    plot_probabilities,
    x="Party",
    y="Estimated probability",
    color="Scenario",
    barmode="group",
    text="Estimated probability",
    title="Estimated Party Probabilities When Only the LBI Changes"
)

fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig.update_layout(
    height=540,
    xaxis_title="",
    yaxis_title="Estimated probability (%)",
    yaxis=dict(range=[0, 42])
)

st.plotly_chart(
    fig,
    width="stretch"
)

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric(
            "AfD",
            "1.7% → 33.7%",
            "+32.0 pp"
        )

with c2:
    with st.container(border=True):
        st.metric(
            "Greens",
            "37.8% → 5.0%",
            "-32.8 pp"
        )

st.warning("""
### Important

These are **model-based adjusted estimates**.

They are not real people observed becoming more left behind and
then changing parties.

The calculation isolates how estimated party probabilities differ
when Feeling Left Behind changes while the conventional voter profile
is held fixed.
""")

st.divider()


# ============================================================
# 5. SAXONY-ANHALT
# ============================================================

st.header("5. Why Saxony-Anhalt matters")

st.markdown("""
In the party-choice analytical sample, Saxony-Anhalt has a higher
average Left Behind Index than the rest of Germany.
""")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Saxony-Anhalt",
    "2.84"
)

c2.metric(
    "Rest of Germany",
    "2.49"
)

c3.metric(
    "Difference",
    "+0.35"
)

st.caption(
    "Bootstrap 95% interval for the difference: approximately +0.24 to +0.47."
)

state_lbi = pd.DataFrame({
    "State": [
        "Saxony-Anhalt",
        "Thuringia",
        "Mecklenburg-Western Pomerania",
        "Brandenburg",
        "Saxony",
        "Hesse",
        "Lower Saxony",
        "Rhineland-Palatinate",
        "Schleswig-Holstein",
        "Baden-Wuerttemberg",
        "Bavaria",
        "Saarland",
        "North Rhine-Westphalia",
        "Berlin",
        "Hamburg",
        "Bremen"
    ],
    "Average LBI": [
        2.842,
        2.804,
        2.756,
        2.682,
        2.659,
        2.577,
        2.485,
        2.484,
        2.423,
        2.423,
        2.414,
        2.405,
        2.382,
        2.308,
        2.092,
        2.031
    ],
    "N": [
        226,
        246,
        169,
        300,
        535,
        243,
        423,
        170,
        139,
        533,
        695,
        42,
        771,
        260,
        103,
        24
    ]
})

fig = px.bar(
    state_lbi,
    x="Average LBI",
    y="State",
    orientation="h",
    text="Average LBI",
    title="Average Left Behind Index Across the 16 German States"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig.update_layout(
    height=700,
    xaxis_title="Average Left Behind Index",
    yaxis_title="",
    yaxis=dict(
        categoryorder="array",
        categoryarray=list(reversed(state_lbi["State"].tolist()))
    ),
    xaxis=dict(range=[0, 3.05])
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.info("""
### Interpretation

This is a **descriptive state comparison**.

Sample sizes vary across states, and the ranking should not be treated
as a precise estimate of the population mean in every state.
""")

st.divider()


# ============================================================
# 6. PROSPECTIVE BENCHMARK
# ============================================================

st.header("6. Historical benchmark versus 2026 polling")

st.markdown("""
The prospective exercise uses the historical relationship between
LBI and party choice among voters in the same East German regional
category, excluding Saxony-Anhalt, as a directional benchmark.

The 2026 polling benchmark is external and is not used to train
the machine-learning model.
""")

historical_polling = pd.DataFrame({
    "Party": [
        "AfD",
        "CDU",
        "The Left",
        "SPD",
        "Greens",
        "BSW",
        "FDP"
    ],
    "Historical LBI-only benchmark": [
        21.8,
        20.3,
        17.9,
        13.8,
        12.1,
        10.5,
        3.6
    ],
    "2026 polling benchmark": [
        42.3,
        22.3,
        12.3,
        7.0,
        5.0,
        4.3,
        3.0
    ]
})

display_benchmark = historical_polling.copy()

display_benchmark["Historical LBI-only benchmark"] = display_benchmark[
    "Historical LBI-only benchmark"
].map(
    lambda x: f"{x:.1f}%"
)

display_benchmark["2026 polling benchmark"] = display_benchmark[
    "2026 polling benchmark"
].map(
    lambda x: f"{x:.1f}%"
)

st.dataframe(
    display_benchmark,
    width="stretch",
    hide_index=True
)

plot_benchmark = historical_polling.melt(
    id_vars="Party",
    value_vars=[
        "Historical LBI-only benchmark",
        "2026 polling benchmark"
    ],
    var_name="Benchmark",
    value_name="Share"
)

fig = px.bar(
    plot_benchmark,
    x="Party",
    y="Share",
    color="Benchmark",
    barmode="group",
    text="Share",
    title="Same Party Order, Very Different Magnitude"
)

fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig.update_layout(
    height=540,
    xaxis_title="",
    yaxis_title="Share (%)",
    yaxis=dict(range=[0, 47])
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.success("""
### What the comparison shows

Both benchmarks place the seven parties in the same order:

**AfD → CDU → The Left → SPD → Greens → BSW → FDP**

But the magnitude is very different.

The polling benchmark shows a much larger AfD advantage than the
historical LBI-only benchmark.
""")

st.warning("""
### What the comparison does not show

The historical LBI-only benchmark is **not a vote-share forecast**.

It should not be evaluated as if it were an opinion poll.

Its role is to ask whether the broader historical pattern associated
with Feeling Left Behind remains recognizable in a new electoral context.
""")

st.caption("""
Benchmark frozen on 26 August 2026.

Equal-weight descriptive mean of three selected polls:
INSA, 10 August 2026;
pollytix, 12 August 2026;
Infratest dimap, 26 August 2026.
""")

st.divider()


# ============================================================
# 7. FINAL INTERPRETATION
# ============================================================

st.header("7. What is the main conclusion?")

st.markdown("""
Feeling Left Behind is **not a universal predictor of party choice**.

Its overall predictive contribution is modest.

But the association is not equally strong across the party system.
The clearest contrast appears between AfD and Green voters, including
when the conventional voter characteristics in the model are held fixed.

Saxony-Anhalt then provides a prospective test of whether the historical
political pattern associated with Feeling Left Behind remains visible
in a new electoral context.
""")

st.success("""
# The election is the test.

# The bigger question is representation.

The broader value of the Left Behind Index is not that it replaces
polling. It is that it may help diagnose part of the political terrain
beneath the polling numbers.
""")

st.divider()


# ============================================================
# 8. METHODOLOGICAL NOTES
# ============================================================

with st.expander("Technical notes"):

    st.markdown("""
### Historical individual-level analysis

- Data: GLES 2025 Post-Election Cross-Section
- Analytical sample: 4,879 respondents across the seven parties
- Target: reported second vote
- Parties: CDU/CSU, SPD, FDP, Greens, The Left, AfD, BSW
- Model: multinomial `LogisticRegression(max_iter=1000)`
- Evaluation: `RepeatedStratifiedKFold`, 5 folds × 10 repetitions
- Random state: 42
- Total held-out evaluations: 50

### Conventional voter profile

- Household Income
- Education
- Age
- East / West Germany (`ostwest`: 0 = East, 1 = West)
- Migration Background
- Political Interest

### Standardized probability exercise

The same fitted model is used.

Observed conventional characteristics are kept unchanged for every
respondent. Only the Left Behind Index is set to 1 and then to 4.

The resulting probabilities are averaged across respondents.

### Prospective Saxony-Anhalt exercise

The historical LBI-only benchmark is learned from the same East German
regional category, excluding Saxony-Anhalt.

The 2026 polling benchmark is an external descriptive comparison
and is not training data.
""")

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

All relationships should be interpreted as model-based associations,
not causal effects.
""")

