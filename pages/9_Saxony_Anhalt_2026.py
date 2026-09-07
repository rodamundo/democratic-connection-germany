import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE
# ============================================================

st.title("🗳️ Saxony-Anhalt 2026: The Post-Election Comparison")

st.subheader(
    "How the historical LBI-only benchmark and the frozen pre-election "
    "polling benchmark compare with the official state result"
)

st.markdown("""
Saxony-Anhalt held its state election on **6 September 2026**. This page
compares the official Land-level (state-wide) result against the two
benchmarks the project built before election day:

- a **historical LBI-only benchmark**, built by training a model on GLES
  2025 respondents in Saxony-Anhalt's East/West regional category
  (excluding Saxony-Anhalt itself) and applying it to the Saxony-Anhalt
  respondents;
- a **frozen 26 August 2026 polling benchmark**, the mean of three polls
  (INSA, pollytix, Infratest dimap) published before the election.

Both benchmarks were fixed before the election and were not updated
afterwards.
""")

st.info("""
### Why compare two very different things

The LBI-only benchmark was never meant to be a vote-share forecast — it
was built to test how far a purely historical, individual-level
relationship travels into a new state and a new election, without any
campaign-period information. The polling benchmark, by contrast, is a
conventional pre-election estimate. Comparing both against the same real
result shows what each kind of evidence does, and does not, capture.
""")

st.divider()


# ============================================================
# 1. OFFICIAL RESULT
# ============================================================

st.header("1. Official result (Zweitstimmen, Land-level)")

st.markdown("""
Source: Landeswahlleiterin Sachsen-Anhalt, state-wide (`Satzart == "LAN"`)
total of Urnenwahl + Briefwahl, second vote (Zweitstimmen) — the vote that
determines proportional seat allocation.
""")

c1, c2, c3 = st.columns(3)
c1.metric("AfD", "43.79%")
c2.metric("CDU", "17.23%")
c3.metric("Die Linke", "8.56%")

c4, c5, c6 = st.columns(3)
c4.metric("SPD", "9.30%")
c5.metric("Greens", "8.93%")
c6.metric("BSW", "5.27%")

st.caption(
    "FDP: 2.58%. These seven parties together account for 95.66% of the "
    "valid Zweitstimmen; the remainder went to smaller parties "
    "(FREIE WÄHLER, dieBasis, Tierschutzpartei and others)."
)

st.divider()


# ============================================================
# 2. THREE-WAY COMPARISON
# ============================================================

st.header("2. Three-way comparison")

comparison = pd.DataFrame({
    "Party": ["AfD", "CDU", "SPD", "Greens", "Die Linke", "BSW", "FDP"],
    "LBI benchmark": [21.8, 20.3, 13.8, 12.1, 17.9, 10.5, 3.6],
    "Polling benchmark": [42.3, 22.3, 7.0, 5.0, 12.3, 4.3, 3.0],
    "Real result": [43.79, 17.23, 9.30, 8.93, 8.56, 5.27, 2.58],
})

comparison["LBI error"] = (
    comparison["LBI benchmark"] - comparison["Real result"]
).round(2)
comparison["Polling error"] = (
    comparison["Polling benchmark"] - comparison["Real result"]
).round(2)

st.dataframe(
    comparison.set_index("Party"),
    width="stretch"
)

fig = px.bar(
    comparison.melt(
        id_vars="Party",
        value_vars=["LBI benchmark", "Polling benchmark", "Real result"],
        var_name="Series",
        value_name="Share (%)"
    ),
    x="Party",
    y="Share (%)",
    color="Series",
    barmode="group",
    category_orders={
        "Party": comparison.sort_values(
            "Real result", ascending=False
        )["Party"].tolist()
    },
    title="LBI benchmark vs. polling benchmark vs. real result, by party"
)
fig.update_layout(height=500, legend_title_text="")
st.plotly_chart(fig, width="stretch")

st.divider()


# ============================================================
# 3. RANK CORRELATION AND ERROR
# ============================================================

st.header("3. How close was each benchmark?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("#### LBI-only benchmark")
        st.metric("Spearman rank correlation", "0.893")
        st.metric("Mean absolute error", "6.90 pp")
        st.caption(
            "Driven mainly by AfD: the LBI-only benchmark (21.8%) "
            "undershot the real AfD result (43.79%) by about 22 pp."
        )

with c2:
    with st.container(border=True):
        st.markdown("#### Polling benchmark")
        st.metric("Spearman rank correlation", "0.893")
        st.metric("Mean absolute error", "2.56 pp")
        st.caption(
            "Closer on every party's level, with the largest single "
            "miss on CDU (+5.07 pp)."
        )

st.markdown("""
Both benchmarks land on the **same Spearman rank correlation** (0.893):
neither correctly ranked Die Linke below SPD and the Greens. Where they
differ sharply is on **magnitude** — the polling benchmark's error is less
than half the LBI-only benchmark's.
""")

st.warning("""
### What this comparison is not

This page reports numbers, not conclusions. It does not yet assess *why*
the LBI-only benchmark undershot AfD by so much, or what that implies for
how the Left Behind Index should be used going forward — that
interpretation is a separate step.
""")

st.divider()

st.caption("""
Official result: Landeswahlleiterin Sachsen-Anhalt, 6 September 2026 state
election (Zweitstimmen, Land-level, preliminary/"vorläufig" result as
published).

LBI-only benchmark and polling benchmark: this project's Saxony-Anhalt
prospective extension (German Longitudinal Election Study, GLES 2025,
Post-Election Cross-Section, ZA10100 Version 3.0.0; and INSA/pollytix/
Infratest dimap polls, frozen 26 August 2026).

The seven-party real-result shares are of the full valid Zweitstimmen; the
LBI-only benchmark is a seven-class model that sums to 100% by
construction. The two are not on an identical denominator.
""")
