import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 Results")


# ============================================================
# DATA
# ============================================================

ols_data = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction"
    ],
    "Traditional Factors": [
        0.088,
        0.085
    ],
    "+ Social Class": [
        0.107,
        0.096
    ],
    "+ Feeling Left Behind": [
        0.276,
        0.222
    ]
})


# ============================================================
# 1. START WITH THE QUESTION
# ============================================================

st.header("What are we trying to understand?")

st.markdown("""
For **Institutional Trust** and **Democratic Satisfaction**,
people have different scores.

The analysis asks:

> # Why do these scores differ from person to person?
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Eight trust ratings are averaged into one score.

**1 = very low trust**

**11 = very high trust**

There is no “trust / no trust” cut-off.
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
One question:

**1 = Very satisfied**

to

**4 = Not at all satisfied**

The full scale is used.
""")

st.divider()


# ============================================================
# 2. THE 100%
# ============================================================

st.header("What does 100% mean?")

st.markdown("""
Imagine that we take **all the differences in Institutional Trust scores**
between the 5,039 respondents.

Some people score 3.

Others score 5.

Others score 8 or 9.

### We call all of those observed differences together = 100%.

The statistical model tries to understand why those differences exist.
""")

st.info("""
### R² answers one question:

**What share of those observed differences can the information
in the model account for?**
""")

st.divider()


# ============================================================
# 3. TRUST STEP BY STEP
# ============================================================

st.header("Institutional Trust: step by step")

st.markdown("""
### Model 1

We tell the model:

**Income + Education + Age + Region + Migration Background + Political Interest**
""")

st.progress(0.088)

st.markdown("""
### **8.8%**

The model can account for **8.8% of the observed differences
in trust scores between respondents**.
""")

st.markdown("---")

st.markdown("""
### Model 2

Now we add:

**+ Subjective Social Class**
""")

st.progress(0.107)

st.markdown("""
### **10.7%**

The model can now account for **10.7% of the observed differences**.

So Social Class adds relatively little.
""")

st.markdown("---")

st.markdown("""
### Model 3

Now we add:

**+ Feeling Left Behind**
""")

st.progress(0.276)

st.markdown("""
### **27.6%**

The complete model can now account for **27.6% of the observed
differences in Institutional Trust scores between respondents**.
""")

st.success("""
# 10.7% → 27.6%

Adding Feeling Left Behind increases R² by:

# +16.9 percentage points
""")

st.warning("""
### This does NOT mean:

❌ Trust increased by 27.6%

❌ 27.6% of people trust institutions

❌ Feeling Left Behind alone explains 27.6%

### It means:

✅ The complete final model accounts for 27.6% of the observed
differences in trust scores between respondents.
""")

st.divider()


# ============================================================
# 4. SATISFACTION
# ============================================================

st.header("Does the same thing happen with Democratic Satisfaction?")

st.markdown("""
Yes. The pattern is very similar.
""")

chart_data = ols_data.melt(
    id_vars="Outcome",
    var_name="Model",
    value_name="R²"
)

fig = px.bar(
    chart_data,
    x="Outcome",
    y="R²",
    color="Model",
    barmode="group",
    text="R²",
    title="How Much of the Differences Between Respondents Can Each Model Account For?"
)

fig.update_traces(
    texttemplate="%{text:.1%}",
    textposition="outside"
)

fig.update_layout(
    height=500,
    xaxis_title="",
    yaxis_title="Share of observed differences accounted for",
    legend_title="",
    yaxis=dict(
        range=[0, 0.32],
        tickformat=".0%"
    )
)

st.plotly_chart(
    fig,
    width="stretch"
)

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
**8.8%**

↓

**10.7%**

↓

# **27.6%**
""")

        st.caption(
            "Traditional → + Social Class → + Feeling Left Behind"
        )

        st.metric(
            "Gain from Feeling Left Behind",
            "+16.9 pp"
        )

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
**8.5%**

↓

**9.6%**

↓

# **22.2%**
""")

        st.caption(
            "Traditional → + Social Class → + Feeling Left Behind"
        )

        st.metric(
            "Gain from Feeling Left Behind",
            "+12.6 pp"
        )

st.success("""
### The important pattern

Subjective Social Class adds relatively little.

Feeling Left Behind adds substantially more information
for both outcomes.
""")

st.divider()


# ============================================================
# 5. WHAT DOES FLB RELATIONSHIP LOOK LIKE?
# ============================================================

st.header("What direction is the relationship?")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
### Higher Feeling Left Behind

### ↓

### Lower Institutional Trust
""")

        st.caption(
            "Standardized β = −0.459 · p < .001"
        )

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
### Higher Feeling Left Behind

### ↓

### Greater Democratic Dissatisfaction
""")

        st.caption(
            "Standardized β = 0.395 · p < .001"
        )

st.divider()


# ============================================================
# 6. PARTY SEPARATE
# ============================================================

st.header("Party Representation is a different analysis")

st.markdown("""
For Party Representation, respondents answer:

# Yes / No

Because this is binary, the analysis uses **logistic regression**.

Its Pseudo R² does **not** have the same interpretation as the R²
used above.
""")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Traditional Factors",
    "3.4%"
)

c2.metric(
    "+ Social Class",
    "3.4%"
)

c3.metric(
    "+ Feeling Left Behind",
    "4.6%"
)

st.info("""
The safest interpretation is:

**Feeling Left Behind improves the Party Representation model,
but the improvement is much smaller.**
""")

st.markdown("""
Holding the other variables constant, each one-point increase in the
Left Behind Index is associated with approximately **29% lower odds**
of saying that a political party represents the respondent's views well.
""")

st.divider()


# ============================================================
# 7. FINAL
# ============================================================

st.header("What did we learn?")

with st.container(border=True):

    st.markdown("""
### 1. Traditional socioeconomic information explains only part of the story

Income, education, age, region and other factors help,
but much remains unexplained.
""")

with st.container(border=True):

    st.markdown("""
### 2. Subjective Social Class adds relatively little

Trust:

**8.8% → 10.7%**

Satisfaction:

**8.5% → 9.6%**
""")

with st.container(border=True):

    st.markdown("""
### 3. Feeling Left Behind adds much more

Trust:

**10.7% → 27.6%**

Satisfaction:

**9.6% → 22.2%**
""")

with st.container(border=True):

    st.markdown("""
### 4. Party Representation is different

The relationship exists, but the model improvement is much smaller.
""")

st.success("""
# Main takeaway

Socioeconomic position does not tell the whole story.

How people feel **seen, recognized, served and heard**
contains additional information about their relationship with democracy.
""")

st.warning("""
The analysis shows **associations, not causation**.
""")

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")