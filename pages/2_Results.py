import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Results",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================

st.title("📊 Results")

st.markdown("""
## What did we find?

People who feel more **left behind** tend to have:

- **lower trust in institutions**;
- **lower satisfaction with how democracy works in Germany**;
- and, to a much smaller extent, **a lower sense of being represented by a political party**.

The important point is that these relationships remain even after taking
into account people's **income, education, age, region, migration background,
political interest and perceived social class**.
""")

st.success("""
### Main takeaway

**Feeling left behind adds much more explanatory power for Institutional Trust
and Democratic Satisfaction than for Party Representation.**

In other words, social disconnection appears to be particularly relevant to
how people **trust and evaluate democracy**, rather than simply whether they
feel represented by a political party.
""")

st.divider()

# ============================================================
# DATA
# ============================================================

comparison = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Model 1": [0.088, 0.085, 0.039],
    "Model 2": [0.107, 0.096, 0.039],
    "Model 3": [0.276, 0.222, 0.053]
})

standardized_results = pd.DataFrame({
    "Outcome": [
        "Institutional Trust",
        "Democratic Satisfaction",
        "Party Representation"
    ],
    "Left Behind β": [-0.459, 0.395, 0.128],
    "Final R²": [0.276, 0.222, 0.053]
})

# ============================================================
# QUICK RESULT
# ============================================================

st.header("The result in one view")

st.markdown("""
The charts below compare how much of the differences between respondents
can be statistically explained **before and after adding the Left Behind Index**.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### 🏛️ Do people trust institutions?

**10.7% → 27.6%**

after adding Feeling Left Behind

**+16.9 percentage points**
""")

with col2:
    st.markdown("""
### 🗳️ Are people satisfied with democracy?

**9.6% → 22.2%**

after adding Feeling Left Behind

**+12.6 percentage points**
""")

with col3:
    st.markdown("""
### 👥 Do people feel represented by a party?

**3.9% → 5.3%**

after adding Feeling Left Behind

**+1.4 percentage points**
""")

st.info("""
### How should I read these percentages?

They show how much of the differences between respondents the statistical
model can explain.

For example, the final model explains **27.6% of the observed differences
in Institutional Trust**.

The important information is not only the final percentage, but also
**how much the model improves when Feeling Left Behind is added**.
""")

st.divider()

# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Institutional Trust",
    "Democratic Satisfaction",
    "Party Representation"
])

# ============================================================
# OVERVIEW
# ============================================================

with tab1:

    st.header("Understanding the analysis")

    # --------------------------------------------------------
    # LEFT BEHIND
    # --------------------------------------------------------

    st.subheader("What does 'Feeling Left Behind' mean?")

    st.markdown("""
**Feeling left behind does not simply mean having a low income.**

The GLES survey asked whether respondents felt that people like them
receive enough **economic attention, social recognition, access to basic
services and freedom to express their opinions**.

The project combines four survey questions into one **Left Behind Index**.
""")

    st.info("""
### The four questions

**1. Economic attention**

“The economic situation of people like me receives too little attention
from society.”

**2. Social recognition**

“People like me receive too little recognition from society for the work
they do.”

**3. Infrastructure and basic services**

“Society pays too little attention to ensuring that people like me have
access to basic infrastructures and services.”

Examples in the questionnaire include doctors, banks, public transportation,
schools, post offices and Internet access.

**4. Freedom of expression**

“People like me are no longer allowed to freely express their opinions
in public.”
""")

    st.markdown("""
Respondents originally answered from:

**1 = Strongly agree**  
to  
**5 = Strongly disagree**

Because agreement means a stronger feeling of being left behind, the scale
was reversed for the analysis.

The final index therefore runs conceptually from:

**1 = lower feeling of being left behind**  
to  
**5 = higher feeling of being left behind**

The final score is the **average of the four reversed answers**.
""")

    st.caption(
        "GLES variables: q46a, q46b, q46c and q46d."
    )

    st.divider()

    # --------------------------------------------------------
    # OUTCOMES
    # --------------------------------------------------------

    st.subheader("What are we trying to explain?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
### 🏛️ Institutional Trust

**Simple question:**

Do people trust important institutions?

The analysis combines respondents' trust in **eight political and public
institutions**.
""")

    with c2:
        st.markdown("""
### 🗳️ Democratic Satisfaction

**Simple question:**

Are people satisfied with how democracy works in Germany?

This comes from **one direct survey question**.
""")

    with c3:
        st.markdown("""
### 👥 Party Representation

**Simple question:**

Do people feel that a political party represents their views?

This also comes from **one direct survey question**.
""")

    st.divider()

    # --------------------------------------------------------
    # MODELS
    # --------------------------------------------------------

    st.subheader("Why are there three models?")

    st.markdown("""
Instead of putting every variable into the analysis at once, the project
adds information in stages.

This allows us to see whether **Feeling Left Behind adds something that
income, education and social class do not already explain**.
""")

    st.info("""
### Model 1 — Traditional characteristics

Includes:

- household income;
- education;
- age;
- East/West Germany;
- migration background;
- political interest.

### Model 2 — Adds Subjective Social Class

Adds how respondents see their own position in society.

### Model 3 — Adds Feeling Left Behind

Adds the Left Behind Index.

If Model 3 explains much more than Model 2, this means Feeling Left Behind
provides important additional information.
""")

    st.divider()

    st.subheader("What happens when Feeling Left Behind is added?")

    st.dataframe(
        comparison.style.format({
            "Model 1": "{:.1%}",
            "Model 2": "{:.1%}",
            "Model 3": "{:.1%}"
        }),
        hide_index=True,
        width="stretch"
    )

    chart_data = comparison.melt(
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
        title="How Much of Each Outcome Can the Models Explain?",
        color_discrete_map={
            "Model 1": "#1f77b4",
            "Model 2": "#ff7f0e",
            "Model 3": "#2ca02c"
        }
    )

    fig.update_traces(
        texttemplate="%{text:.1%}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "%{fullData.name}<br>"
            "Variation explained: %{y:.1%}<extra></extra>"
        )
    )

    fig.update_layout(
        height=550,
        xaxis_title="",
        yaxis_title="Variation explained",
        legend_title="",
        yaxis=dict(
            range=[0, 0.35],
            tickformat=".0%"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.success("""
### What does this graph tell us?

Adding **Subjective Social Class** changes the models only slightly.

The large change happens when **Feeling Left Behind** is introduced:

- Institutional Trust: **10.7% → 27.6%**
- Democratic Satisfaction: **9.6% → 22.2%**
- Party Representation: **3.9% → 5.3%**

So Feeling Left Behind adds substantial information about **trust and
democratic satisfaction**, but much less about **party representation**.
""")

    # --------------------------------------------------------
    # BETA
    # --------------------------------------------------------

    with st.expander("Technical evidence: standardized coefficients"):

        st.markdown("""
The chart below shows the standardized coefficient of the Left Behind Index.

The **larger the absolute value**, the stronger the relationship.

The positive or negative sign depends on how each original survey response
was coded.
""")

        beta_fig = px.bar(
            standardized_results,
            x="Outcome",
            y="Left Behind β",
            text="Left Behind β",
            title="Standardized Association of the Left Behind Index"
        )

        beta_fig.update_traces(
            texttemplate="%{text:.3f}",
            textposition="outside",
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Standardized β = %{y:.3f}<extra></extra>"
            )
        )

        beta_fig.add_hline(
            y=0,
            line_width=1
        )

        beta_fig.update_layout(
            height=480,
            xaxis_title="",
            yaxis_title="Standardized coefficient (β)",
            yaxis=dict(range=[-0.55, 0.5])
        )

        st.plotly_chart(
            beta_fig,
            width="stretch"
        )

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("🏛️ Institutional Trust")

    st.markdown("""
### In simple terms

**Do people trust the institutions around them?**
""")

    st.subheader("What was actually asked?")

    st.markdown("""
Respondents were asked:

> **“For each of the following public institutions, organizations,
> or groups of people, please indicate how much you personally trust them.”**

The analysis combines responses for **eight institutions or groups**:
""")

    st.info("""
- **Federal Government**
- **Bundestag**
- **Political Parties**
- **Politicians**
- **Police**
- **Justice**
- **Science**
- **Public-Service Broadcasting**
""")

    st.markdown("""
For every item, respondents used an 11-point scale:

**1 = Do not trust at all**  
**11 = Trust completely**

The eight answers were averaged into a single **Institutional Trust Index**.

The questionnaire also asks about trust in Social Media (`q79h`), but this
item was excluded because it was treated as conceptually different from
the public and political institutions used in this index.
""")

    st.caption(
        "GLES variables used: q79a–q79g and q79i."
    )

    st.divider()

    # --------------------------------------------------------
    # FINDING
    # --------------------------------------------------------

    st.subheader("What did we find?")

    st.success("""
## People who feel more left behind tend to trust institutions substantially less.

This is the strongest relationship with Feeling Left Behind among the
three democratic outcomes studied.
""")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Before adding Feeling Left Behind",
            "10.7%",
            help="Variation explained by Model 2."
        )

    with c2:
        st.metric(
            "After adding Feeling Left Behind",
            "27.6%",
            delta="+16.9 percentage points",
            help="Variation explained by Model 3."
        )

    st.markdown("""
### What does this mean?

Before Feeling Left Behind is considered, the model explains **10.7%**
of the differences in Institutional Trust.

After it is added, the model explains **27.6%**.

That is a very substantial increase.

The relationship remains even after accounting for:

- household income;
- education;
- age;
- East/West Germany;
- migration background;
- political interest;
- Subjective Social Class.

Importantly, **Household Income is not statistically significant in the
final model**.

This suggests that knowing someone's income alone does not tell us as much
about institutional trust as knowing whether that person feels socially
overlooked, unrecognized or left behind.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final R²",
            "27.6%"
        )

        c2.metric(
            "Standardized β",
            "−0.459"
        )

        c3.metric(
            "Statistical significance",
            "p < .001"
        )

        st.markdown("""
The negative coefficient means that higher scores on the Left Behind Index
are associated with lower Institutional Trust.

The standardized coefficient of **−0.459** indicates a comparatively strong
relationship within this model.
""")

    st.info("""
These results describe a statistical association. They do not demonstrate
that feeling left behind causes lower institutional trust.
""")

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab3:

    st.header("🗳️ Democratic Satisfaction")

    st.markdown("""
### In simple terms

**Are people satisfied with how democracy works in Germany?**
""")

    st.subheader("What was actually asked?")

    st.markdown("""
Respondents were asked one direct question:

> **“How satisfied are you with the way democracy works in Germany?”**
""")

    st.info("""
**1 = Very satisfied**

**2 = Fairly satisfied**

**3 = Not very satisfied**

**4 = Not at all satisfied**
""")

    st.markdown("""
This is important for interpreting the results:

**higher numbers mean greater dissatisfaction.**
""")

    st.caption(
        "GLES variable: q119 — Democracy: Satisfaction."
    )

    st.divider()

    # --------------------------------------------------------
    # FINDING
    # --------------------------------------------------------

    st.subheader("What did we find?")

    st.success("""
## People who feel more left behind tend to be less satisfied with how democracy works.

Again, the relationship remains after accounting for socioeconomic,
demographic and political characteristics.
""")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Before adding Feeling Left Behind",
            "9.6%",
            help="Variation explained by Model 2."
        )

    with c2:
        st.metric(
            "After adding Feeling Left Behind",
            "22.2%",
            delta="+12.6 percentage points",
            help="Variation explained by Model 3."
        )

    st.markdown("""
### What does this mean?

Before Feeling Left Behind is introduced, the model explains **9.6%**
of the differences in Democratic Satisfaction.

After adding it, the model explains **22.2%**.

That is an increase of **12.6 percentage points**.

By comparison, simply adding people's perceived social class increased
the model only from **8.5% to 9.6%**.

This suggests that the experience of feeling overlooked or left behind
contains information about democratic dissatisfaction that is not captured
simply by **income or social class**.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final R²",
            "22.2%"
        )

        c2.metric(
            "Standardized β",
            "0.395"
        )

        c3.metric(
            "Statistical significance",
            "p < .001"
        )

        st.markdown("""
The coefficient is positive because the original survey scale is coded so
that higher values mean **greater dissatisfaction**.

Therefore, β = **0.395** means that stronger feelings of being left behind
are associated with less satisfaction with democracy.
""")

    st.info("""
The analysis identifies an association. It does not establish that feeling
left behind causes democratic dissatisfaction.
""")

# ============================================================
# PARTY REPRESENTATION
# ============================================================

with tab4:

    st.header("👥 Party Representation")

    st.markdown("""
### In simple terms

**Do people feel that a political party represents their views?**
""")

    st.subheader("What was actually asked?")

    st.markdown("""
Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**
""")

    st.info("""
**1 = Yes**

**2 = No**
""")

    st.markdown("""
“Don't know” and missing responses were treated as missing values.

Because **2 means No**, higher values indicate a greater lack of perceived
party representation.
""")

    st.caption(
        "GLES variable: q141 — Political Parties: Representation of Interests."
    )

    st.divider()

    # --------------------------------------------------------
    # FINDING
    # --------------------------------------------------------

    st.subheader("What did we find?")

    st.success("""
## Feeling left behind is related to feeling less represented by political parties — but only weakly.

This relationship is much smaller than the relationships found for
Institutional Trust and Democratic Satisfaction.
""")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Before adding Feeling Left Behind",
            "3.9%",
            help="Variation explained by Model 2."
        )

    with c2:
        st.metric(
            "After adding Feeling Left Behind",
            "5.3%",
            delta="+1.4 percentage points",
            help="Variation explained by Model 3."
        )

    st.markdown("""
### What does this mean?

Adding Feeling Left Behind improves the model only from **3.9% to 5.3%**.

Compare that with:

- **+16.9 percentage points** for Institutional Trust;
- **+12.6 percentage points** for Democratic Satisfaction;
- only **+1.4 percentage points** here.

**Political Interest**, rather than Feeling Left Behind, is the strongest
predictor in this model.

This tells us something important:

**Feeling left behind is not a general explanation for every type of
democratic disconnection.**

It appears much more closely related to how people **trust institutions
and evaluate democracy** than to whether a political party represents
their views.
""")

    with st.expander("Technical evidence"):

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final R²",
            "5.3%"
        )

        c2.metric(
            "Standardized β",
            "0.128"
        )

        c3.metric(
            "Statistical significance",
            "p < .001"
        )

        st.markdown("""
Because higher values on q141 mean answering “No”, the positive coefficient
indicates that stronger feelings of being left behind are associated with a
greater likelihood of reporting that no political party represents one's
views well.

The standardized coefficient (**0.128**) is much smaller than for the
other two outcomes.
""")

    st.info("""
The final model explains only a small proportion of differences in Party
Representation. Most of those differences are therefore related to factors
not captured by the variables included in this analysis.
""")

# ============================================================
# BIG PICTURE
# ============================================================

st.divider()

st.header("What does this tell us?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### 1. Economic position is not the whole story

Income and education matter, but people's **perceptions of recognition,
attention and social inclusion** provide substantial additional information
about their democratic attitudes.
""")

with col2:
    st.markdown("""
### 2. Feeling left behind is not simply social class

Adding Subjective Social Class changes the models only slightly.

The much larger change happens when the **Left Behind Index** is introduced.
""")

with col3:
    st.markdown("""
### 3. Democratic disconnection has different dimensions

Feeling left behind is strongly connected to **institutional trust and
democratic satisfaction**, but much less to **party representation**.
""")

st.warning("""
### What we cannot conclude

These data were collected at one point in time.

The analysis can show that Feeling Left Behind and democratic attitudes
are related, but it **cannot prove that one causes the other**.
""")

# ============================================================
# METHODOLOGICAL CONFIDENCE
# ============================================================

st.divider()

with st.expander("Methodological confidence and diagnostics"):

    st.markdown("""
This section contains the technical checks supporting the analysis.
It is not necessary to understand these statistics in order to interpret
the substantive findings above.
""")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Analytical sample",
        "5,039"
    )

    c2.metric(
        "Left Behind α",
        "0.753"
    )

    c3.metric(
        "Institutional Trust α",
        "0.889"
    )

    c4.metric(
        "Predictor VIF",
        "< 2"
    )

    st.markdown("""
- The four Left Behind items showed acceptable internal consistency.
- The Institutional Trust Index showed high internal consistency.
- Factor analysis supported a clear one-factor structure for the Left Behind Index.
- No meaningful multicollinearity was detected.
- HC3 robust standard errors were used because regression diagnostics
  indicated heteroscedasticity.
""")

# ============================================================
# SOURCE
# ============================================================

st.divider()

st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

**Variables used**

Left Behind Index: q46a–q46d  
Institutional Trust Index: q79a–q79g and q79i  
Democratic Satisfaction: q119  
Party Representation: q141

The analyses use cross-sectional observational data. Results describe
statistical associations and should not be interpreted as evidence of
cause and effect.
""")