import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE
# ============================================================

st.title("🧭 LBI Components")

st.subheader(
    "What changes when the Left Behind Index is opened into four separate perceptions?"
)

st.markdown("""
The overall Left Behind Index gives each of its four items **equal
arithmetic weight**.

That does not mean the four items must show equally strong relationships
with political outcomes.

This page compares the components separately and asks where the clearest
patterns appear.
""")

st.info("""
### The four components

**Economic attention · Social recognition · Infrastructure / services · Perceived freedom of public expression**
""")

st.divider()


# ============================================================
# MODEL COMPARISON
# ============================================================

st.header("1. Does opening the index add information for party choice?")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric("Conventional profile", "35.8%")
        st.caption("Mean held-out accuracy")

with c2:
    with st.container(border=True):
        st.metric("+ overall LBI", "38.2%")
        st.caption("Mean held-out accuracy")

with c3:
    with st.container(border=True):
        st.metric("+ four components", "39.9%")
        st.caption("Mean held-out accuracy")

st.markdown("""
Moving from the overall LBI to the four separate components improves
accuracy by about **1.8 percentage points** and macro-F1 by about **0.022**,
while also reducing log loss.
""")

st.success("""
### Repeated evaluation

The four-component model outperformed the overall-LBI model in **all 50
held-out evaluations** on accuracy and macro-F1, and had lower log loss in
all 50 evaluations.
""")

st.caption(
    "This is supporting evidence that the components contain distinct information. "
    "It is not the headline finding and it does not imply high individual-level predictability."
)

st.divider()


# ============================================================
# PARTY SCENARIOS
# ============================================================

st.header("2. Which components stand out across parties?")

st.markdown("""
The fitted seven-party model is translated into a common scenario.

For each component, the score is moved from **1 to 4** while the other
characteristics included in the model remain at their observed values.
The table reports the resulting change in the average estimated party
probability.
""")

party_component = pd.DataFrame({
    "Party": [
        "CDU/CSU", "CDU/CSU", "CDU/CSU", "CDU/CSU",
        "SPD", "SPD", "SPD", "SPD",
        "FDP", "FDP", "FDP", "FDP",
        "Greens", "Greens", "Greens", "Greens",
        "Die Linke", "Die Linke", "Die Linke", "Die Linke",
        "AfD", "AfD", "AfD", "AfD",
        "BSW", "BSW", "BSW", "BSW"
    ],
    "Component": [
        "Economic attention", "Social recognition", "Infrastructure / services", "Public expression",
        "Economic attention", "Social recognition", "Infrastructure / services", "Public expression",
        "Economic attention", "Social recognition", "Infrastructure / services", "Public expression",
        "Economic attention", "Social recognition", "Infrastructure / services", "Public expression",
        "Economic attention", "Social recognition", "Infrastructure / services", "Public expression",
        "Economic attention", "Social recognition", "Infrastructure / services", "Public expression",
        "Economic attention", "Social recognition", "Infrastructure / services", "Public expression"
    ],
    "Change (pp)": [
        3.27, -0.63, -0.41, 2.46,
        -4.39, 4.33, -0.20, -12.24,
        1.93, -0.36, -0.52, 3.08,
        -10.44, -0.97, -0.32, -22.42,
        3.23, -0.46, 3.10, -9.61,
        3.58, -1.03, -1.90, 34.11,
        2.82, -0.88, 0.25, 4.61
    ]
})

selected_party = st.selectbox(
    "Choose a party",
    ["AfD", "Greens", "SPD", "BSW", "CDU/CSU", "Die Linke", "FDP"]
)

selected = party_component[party_component["Party"] == selected_party].copy()
selected["Label"] = selected["Change (pp)"].map(lambda x: f"{x:+.1f} pp")

fig = px.bar(
    selected,
    x="Change (pp)",
    y="Component",
    orientation="h",
    text="Label",
    title=f"{selected_party}: estimated probability change when each component moves 1 → 4"
)
fig.update_traces(textposition="outside")
fig.update_layout(
    height=430,
    xaxis_title="Change in estimated party probability (percentage points)",
    yaxis_title=""
)
fig.add_vline(x=0, line_width=1)
st.plotly_chart(fig, width="stretch")

with st.expander("Show the full seven-party table"):
    full_table = party_component.pivot(
        index="Party",
        columns="Component",
        values="Change (pp)"
    ).reset_index()

    ordered_columns = [
        "Party",
        "Economic attention",
        "Social recognition",
        "Infrastructure / services",
        "Public expression"
    ]
    full_table = full_table[ordered_columns]

    for col in ordered_columns[1:]:
        full_table[col] = full_table[col].map(lambda x: f"{x:+.2f}")

    st.dataframe(full_table, width="stretch", hide_index=True)

st.caption("""
These are adjusted model-based associations from the full multiclass
model. They do not show what would causally happen if a person's survey
response were changed.
""")

st.divider()


# ============================================================
# KEY PARTY PATTERNS
# ============================================================

st.header("3. Four party patterns worth noticing")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("### AfD")
        st.metric("Public expression", "+34.1 pp")
        st.metric("Economic attention", "+3.6 pp")
        st.markdown("""
The public-expression item is by far the strongest positive relationship.
Social recognition and infrastructure show no comparable positive pattern.
""")

    with st.container(border=True):
        st.markdown("### SPD")
        st.metric("Public expression", "−12.2 pp")
        st.markdown("""
The same component points strongly in the opposite direction from AfD.
""")

with c2:
    with st.container(border=True):
        st.markdown("### Greens")
        st.metric("Public expression", "−22.4 pp")
        st.metric("Economic attention", "−10.4 pp")
        st.markdown("""
Both items matter, but the public-expression relationship is more than
twice as large in absolute terms.
""")

    with st.container(border=True):
        st.markdown("### BSW")
        st.metric("Public expression", "+4.6 pp")
        st.metric("Economic attention", "+2.8 pp")
        st.markdown("""
BSW shows a more mixed profile rather than the dominance of one component.
""")

st.warning("""
### Equal weight, different political pattern

Public expression does **not** count more in the Left Behind Index.
All four items contribute equally to the index. What differs is the
strength of their relationships with political outcomes.
""")

st.divider()


# ============================================================
# LEFT-RIGHT ROBUSTNESS
# ============================================================

st.header("4. Is the public-expression pattern simply left-right ideology?")

st.markdown("""
Respondents place themselves on the GLES left-right scale:

**1 = Left · 6 = Centre · 11 = Right**

The analysis is repeated on a matched sample while adding this
self-placement to the model.
""")

ideology = pd.DataFrame({
    "Party": ["AfD", "Greens", "SPD", "Die Linke", "BSW", "FDP"],
    "OR before left-right": [3.3939, 0.4092, 0.6265, 0.6099, 1.2829, 1.2366],
    "OR after left-right": [2.8478, 0.4886, 0.6878, 0.9245, 1.4470, 1.0019],
    "Interpretation": [
        "About 14% smaller; remains strong",
        "About 20% smaller; remains",
        "About 20% smaller; remains",
        "About 84% smaller; largely disappears",
        "Remains and becomes somewhat stronger",
        "Disappears"
    ]
})

ideology_display = ideology.copy()
ideology_display["OR before left-right"] = ideology_display["OR before left-right"].map(lambda x: f"{x:.2f}")
ideology_display["OR after left-right"] = ideology_display["OR after left-right"].map(lambda x: f"{x:.2f}")

st.dataframe(ideology_display, width="stretch", hide_index=True)

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric("AfD attenuation", "14.4%")
        st.caption("Reduction in the absolute public-expression coefficient.")

with c2:
    with st.container(border=True):
        st.metric("Matched robustness sample", "4,757")
        st.caption("Same respondents used before and after adding left-right position.")

st.success("""
### Interpretation

Political position accounts for **part** of the strongest relationship,
but not most of it. The AfD association remains strong after respondents'
own left-right self-placement is included.
""")

st.divider()


# ============================================================
# TRUST AND SATISFACTION
# ============================================================

st.header("5. The same component also stands out for democratic trust")

trust = pd.DataFrame({
    "Component": [
        "Economic attention",
        "Social recognition",
        "Infrastructure / services",
        "Public expression"
    ],
    "Standardized coefficient": [-0.12945, -0.01803, -0.09243, -0.37360]
})

satisfaction = pd.DataFrame({
    "Component": [
        "Economic attention",
        "Social recognition",
        "Infrastructure / services",
        "Public expression"
    ],
    "Standardized coefficient": [-0.10997, -0.01522, -0.04592, -0.36097]
})

outcome_choice = st.radio(
    "Choose an outcome",
    ["Institutional Trust", "Democratic Satisfaction"],
    horizontal=True
)

plot_df = trust if outcome_choice == "Institutional Trust" else satisfaction

fig = px.bar(
    plot_df,
    x="Standardized coefficient",
    y="Component",
    orientation="h",
    text="Standardized coefficient",
    title=f"Adjusted component associations with {outcome_choice}"
)
fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
fig.update_layout(
    height=430,
    xaxis_title="Standardized coefficient",
    yaxis_title=""
)
fig.add_vline(x=0, line_width=1)
st.plotly_chart(fig, width="stretch")

st.markdown("""
For Institutional Trust, the public-expression relationship is almost
**three times as large** as the relationship with economic attention.
Democratic Satisfaction shows almost the same ordering.
""")

st.caption(
    "Higher component scores indicate stronger Feeling Left Behind. "
    "The outcomes are coded so higher values mean greater trust or satisfaction."
)

st.divider()


# ============================================================
# MEASUREMENT CHECK
# ============================================================

st.header("6. Does the strong public-expression result mean the item should be removed from the LBI?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.metric("Cronbach's α: four items", "0.753")

with c2:
    with st.container(border=True):
        st.metric("Cronbach's α without public expression", "0.757")

st.markdown("""
Removing the public-expression item raises alpha by only about **0.004**.
That is a very small change.

The item is somewhat distinct, but the measurement checks do not provide
a strong reason to remove it from the four-item index.
""")

st.divider()


# ============================================================
# DIAGNOSIS
# ============================================================

st.header("7. What is the diagnosis?")

st.success("""
### Main finding

Among the four forms of Feeling Left Behind measured here,
**perceived inability to express opinions freely in public stands out most
strongly in relation to AfD support, lower Institutional Trust and lower
Democratic Satisfaction**.
""")

st.markdown("""
This is not a universal pattern. The component is weaker for some parties,
and other LBI components matter more in some electorates.

The result is therefore specific: this perception is an unusually strong
**marker of political disconnection in some parts of the electorate**.
""")

st.warning("""
### Evidence boundary

The exact survey statement is:

> “People like me are no longer allowed to freely express their opinions in public.”

The analysis measures agreement with that statement. It does not identify
what opinions respondents have in mind, what they believe prevents them
from speaking, or whether an objective restriction exists.
""")

st.divider()

st.caption("""
Primary data source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100 Version 3.0.0.

All findings are observational. They describe statistical relationships
and model-based scenarios, not causal effects.
""")
