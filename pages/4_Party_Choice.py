import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE
# ============================================================

st.title("🗳️ Feeling Left Behind and Party Choice")

st.subheader(
    "What the overall index adds, and what changes when the four components are kept separate"
)

st.markdown("""
The party-choice analysis focuses on respondents' reported **second vote
in the 2025 federal election** across seven parties.

The main result is not that Feeling Left Behind predicts everyone's vote.
The overall gain is modest. The more interesting question is **where the
additional information is concentrated**.
""")

st.info("""
### Main question

**Does Feeling Left Behind add useful information about party choice
beyond age, income, education, region, migration background and political
interest?**
""")

st.divider()


# ============================================================
# SAMPLE AND DESIGN
# ============================================================

st.header("1. Analytical design")

st.markdown("""
The common analytical sample contains **4,879 confirmed voters** with a
valid second-vote choice among:

**CDU/CSU · SPD · FDP · Greens · Die Linke · AfD · BSW**
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### Model A")
        st.markdown("""
**Conventional profile**

Income · Education · Age · East/West · Migration Background · Political Interest
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

Tests whether the four items are more informative when modeled separately.
""")

st.markdown("""
The models are evaluated using **repeated stratified cross-validation**:

### 5 folds × 10 repetitions = 50 held-out evaluations

In each evaluation, predictions are assessed on respondents who were not
used to fit that version of the model.
""")

st.divider()


# ============================================================
# PERFORMANCE
# ============================================================

st.header("2. How much predictive information is added?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric("Conventional profile", "35.8%")
        st.caption("Mean held-out accuracy")

with c2:
    with st.container(border=True):
        st.metric("+ overall LBI", "38.2%", "+2.3 pp")
        st.caption("Mean held-out accuracy")

with c3:
    with st.container(border=True):
        st.metric("+ four components", "39.9%", "+1.8 pp vs overall LBI")
        st.caption("Mean held-out accuracy")

performance_df = pd.DataFrame({
    "Model": [
        "Conventional profile",
        "+ overall LBI",
        "+ four LBI components"
    ],
    "Accuracy": [0.35835, 0.38151, 0.39941]
})

fig = px.bar(
    performance_df,
    x="Model",
    y="Accuracy",
    text="Accuracy",
    title="Held-out party-choice accuracy"
)
fig.update_traces(texttemplate="%{text:.1%}", textposition="outside")
fig.update_layout(
    height=450,
    xaxis_title="",
    yaxis_title="Accuracy",
    yaxis=dict(range=[0, 0.44], tickformat=".0%")
)
st.plotly_chart(fig, width="stretch")

st.success("""
### What the repeated tests show

The four-component model outperformed the overall-LBI model in **all 50
repeated evaluations** on accuracy and macro-F1, and had lower log loss
in all 50 evaluations.

The improvement is real but modest. The value of opening the index is
therefore mainly **diagnostic**, not a claim of high-accuracy vote prediction.
""")

st.divider()


# ============================================================
# PARTY AVERAGES
# ============================================================

st.header("3. Party electorates occupy different positions on the overall LBI")

party_lbi = pd.DataFrame({
    "Party": [
        "AfD",
        "BSW",
        "FDP",
        "Die Linke",
        "CDU/CSU",
        "SPD",
        "Greens"
    ],
    "Average LBI": [3.30, 2.87, 2.57, 2.50, 2.47, 2.35, 2.01]
}).sort_values("Average LBI", ascending=False)

fig = px.bar(
    party_lbi,
    x="Party",
    y="Average LBI",
    text="Average LBI",
    title="Average Left Behind Index by 2025 party choice"
)
fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
fig.update_layout(
    height=500,
    xaxis_title="",
    yaxis_title="Average LBI",
    yaxis=dict(range=[0, 3.7])
)
st.plotly_chart(fig, width="stretch")

c1, c2, c3 = st.columns(3)
c1.metric("AfD average", "3.30")
c2.metric("Greens average", "2.01")
c3.metric("Difference", "1.29 points")

st.caption("""
These are raw descriptive averages. They do not control for differences
in age, income, education, region or other voter characteristics.
""")

st.divider()


# ============================================================
# OVERALL LBI SCENARIO
# ============================================================

st.header("4. The broad contrast in the aggregate-LBI model")

st.markdown("""
An earlier aggregate-LBI model provides a simple way to visualize the
broad AfD-Green contrast.

For each respondent, the conventional voter characteristics are kept
unchanged while the overall LBI is moved from **1 to 4**. The model then
recalculates the estimated party probabilities.
""")

probabilities = pd.DataFrame({
    "Party": [
        "AfD",
        "Greens",
        "CDU/CSU",
        "SPD",
        "Die Linke",
        "BSW",
        "FDP"
    ],
    "LBI = 1": [1.71, 37.76, 23.70, 19.78, 12.07, 2.27, 2.71],
    "LBI = 4": [33.71, 5.01, 27.83, 9.34, 9.33, 8.48, 6.30]
})

probabilities["Change (pp)"] = probabilities["LBI = 4"] - probabilities["LBI = 1"]

prob_display = probabilities.copy()
prob_display["LBI = 1"] = prob_display["LBI = 1"].map(lambda x: f"{x:.1f}%")
prob_display["LBI = 4"] = prob_display["LBI = 4"].map(lambda x: f"{x:.1f}%")
prob_display["Change (pp)"] = prob_display["Change (pp)"].map(lambda x: f"{x:+.1f}")

st.dataframe(prob_display, width="stretch", hide_index=True)

plot_probabilities = probabilities.melt(
    id_vars="Party",
    value_vars=["LBI = 1", "LBI = 4"],
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
    title="Aggregate-LBI model: estimated party probabilities"
)
fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig.update_layout(
    height=540,
    xaxis_title="",
    yaxis_title="Estimated probability (%)",
    yaxis=dict(range=[0, 42])
)
st.plotly_chart(fig, width="stretch")

st.warning("""
### Interpretation

These are **model-based adjusted estimates**, not observed people becoming
more left behind and then switching parties.

The aggregate model also hides which of the four LBI items is associated
with the contrast. The **LBI Components** page opens that black box.
""")

st.divider()


# ============================================================
# GEOGRAPHY
# ============================================================

st.header("5. Geography: where does Saxony-Anhalt sit?")

st.markdown("""
The party-choice sample also provides a descriptive geographic comparison.
Saxony-Anhalt has a higher average LBI than the rest of Germany in this
analytical sample.
""")

c1, c2, c3 = st.columns(3)
c1.metric("Saxony-Anhalt", "2.84")
c2.metric("Rest of Germany", "2.49")
c3.metric("Difference", "+0.35")

st.caption(
    "Bootstrap 95% interval for the descriptive difference: approximately +0.24 to +0.47."
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
        2.842, 2.804, 2.756, 2.682, 2.659, 2.577, 2.485, 2.484,
        2.423, 2.423, 2.414, 2.405, 2.382, 2.308, 2.092, 2.031
    ],
    "N": [
        226, 246, 169, 300, 535, 243, 423, 170,
        139, 533, 695, 42, 771, 260, 103, 24
    ]
})

fig = px.bar(
    state_lbi,
    x="Average LBI",
    y="State",
    orientation="h",
    text="Average LBI",
    hover_data=["N"],
    title="Average Left Behind Index across the 16 German states"
)
fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
fig.update_layout(
    height=700,
    xaxis_title="Average LBI",
    yaxis_title="",
    yaxis=dict(
        categoryorder="array",
        categoryarray=list(reversed(state_lbi["State"].tolist()))
    ),
    xaxis=dict(range=[0, 3.05])
)
st.plotly_chart(fig, width="stretch")

st.caption("""
These state averages are descriptive. Small state samples, especially
Bremen and Saarland, should be interpreted cautiously.
""")

st.divider()


# ============================================================
# SAXONY-ANHALT EXTENSION
# ============================================================

st.header("6. The Saxony-Anhalt prospective extension")

st.markdown("""
The project uses the historical LBI-party relationship as a **directional
benchmark** for interpreting the political context in Saxony-Anhalt before
the 2026 state election.

The external polling benchmark is not used to fit the historical model.
""")

st.warning("""
### What this extension is not

- It is not an opinion poll.
- It is not a formal vote-share forecast.
- It is not evidence that Feeling Left Behind alone explains the state's party landscape.
""")

st.divider()


# ============================================================
# TAKEAWAY
# ============================================================

st.header("7. What should we take from the party-choice analysis?")

st.success("""
### Main takeaway

The overall LBI adds **modest but consistent** information beyond the
conventional voter profile.

Keeping the four components separate improves held-out performance
further, which motivates the next question: **which component is carrying
that additional political information for which party?**
""")

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

All party probabilities shown here are model-based associations from
observational survey data, not causal effects or forecasts.
""")
