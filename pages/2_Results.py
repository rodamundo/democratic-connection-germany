import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Results",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Results")

st.markdown("""
This page presents the main findings of the analysis.

The research asks whether **feeling left behind** helps explain three
different dimensions of democratic connection in Germany:

- **Institutional Trust** — how much respondents trust key public and political institutions;
- **Democratic Satisfaction** — how satisfied respondents are with the way democracy works in Germany;
- **Party Representation** — whether respondents feel that any political party represents their views well.

For each outcome, three regression models are compared:

- **Model 1 — Traditional factors:** household income, education, age,
  East/West Germany, migration background and political interest.

- **Model 2 — Subjective Social Class:** adds how respondents perceive
  their own position in society.

- **Model 3 — Left Behind Index:** adds respondents' subjective feeling
  of being left behind.
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

    st.header("Overview")

    # --------------------------------------------------------
    # LEFT BEHIND INDEX
    # --------------------------------------------------------

    st.subheader("What does 'Feeling Left Behind' mean?")

    st.markdown("""
The **Left Behind Index** was constructed from four questions in the
GLES 2025 survey.

Respondents were asked to what extent they agreed or disagreed with
the following statements:
""")

    st.info("""
**1. Economic attention**

“The economic situation of people like me receives too little attention
from society.”

**2. Social recognition**

“People like me receive too little recognition from society for the work
they do.”

**3. Infrastructure and basic services**

“Society pays too little attention to ensuring that people like me have
access to basic infrastructures and services.”

Examples provided in the questionnaire included post offices, doctors,
banks, public transportation, schools and Internet access.

**4. Freedom of expression**

“People like me are no longer allowed to freely express their opinions
in public.”
""")

    st.markdown("""
The original GLES scale runs from:

**1 = Strongly agree**  
to  
**5 = Strongly disagree**

Because agreement indicates a stronger feeling of being left behind,
the scale was **reversed in the analysis**.

The final Left Behind Index therefore runs conceptually from:

**1 = Lower feeling of being left behind**  
to  
**5 = Higher feeling of being left behind**

The index is the **mean of the four reversed items**.
""")

    st.caption(
        "GLES variables: q46a–q46d — Left behind: subjective."
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

How much respondents trust key political and public institutions.

**8 survey items combined into one index.**
""")

    with c2:
        st.markdown("""
### 🗳️ Democratic Satisfaction

How satisfied respondents are with the way democracy currently works
in Germany.

**1 direct survey question.**
""")

    with c3:
        st.markdown("""
### 👥 Party Representation

Whether respondents believe that any political party in Germany
represents their personal political views well.

**1 direct Yes/No question.**
""")

    st.divider()

    # --------------------------------------------------------
    # MODELS
    # --------------------------------------------------------

    st.subheader("How the models build on each other")

    st.info("""
**Model 1 — Traditional factors**

Income, education, age, East/West Germany, migration background and
political interest.

**Model 2 — + Subjective Social Class**

Adds how respondents perceive their own position in the social hierarchy.

**Model 3 — + Left Behind Index**

Adds respondents' subjective experience of being economically,
socially and politically left behind.

Comparing these models tells us how much additional explanatory power
each new layer contributes.
""")

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
        title="How Much Variation Each Model Explains",
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
            "R² = %{y:.1%}<extra></extra>"
        )
    )

    fig.update_layout(
        height=550,
        xaxis_title="",
        yaxis_title="Variation explained (R²)",
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
### Main finding

Adding **Subjective Social Class** produces only a relatively small
improvement in explanatory power.

The major change occurs when the **Left Behind Index** is introduced:

- **Institutional Trust:** 10.7% → **27.6%**
- **Democratic Satisfaction:** 9.6% → **22.2%**
- **Party Representation:** 3.9% → **5.3%**

The increase is therefore much larger for Institutional Trust and
Democratic Satisfaction than for Party Representation.

This suggests that feeling left behind captures an important dimension
of democratic attitudes that is not fully represented by income,
education or perceived social class.
""")

    st.subheader("How strongly is Left Behind associated with each outcome?")

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

    st.caption("""
The direction of the coefficient depends on how the original outcome
was coded. The absolute size of β indicates the relative strength of
the association.
""")

# ============================================================
# INSTITUTIONAL TRUST
# ============================================================

with tab2:

    st.header("Institutional Trust")

    st.subheader("What was actually asked?")

    st.markdown("""
The GLES asked respondents:

> **“For each of the following public institutions, organizations,
> or groups of people, please indicate how much you personally trust them.”**

The original questionnaire contains nine items. The analysis uses
**eight of them**:
""")

    st.info("""
**q79a** — Federal Government  
**q79b** — Bundestag  
**q79c** — Political Parties  
**q79d** — Politicians  
**q79e** — Police  
**q79f** — Justice  
**q79g** — Science  
**q79i** — Public-Service Broadcasting
""")

    st.markdown("""
Each item was measured on an **11-point scale**:

**1 = Do not trust at all**  
**11 = Trust completely**

The eight responses were averaged to create the **Institutional Trust Index**.

**q79h — Social Media** was not included in the index because the analysis
treated it as conceptually distinct from the other public and political
institutions.
""")

    st.caption(
        "GLES variables used: q79a–q79g and q79i."
    )

    st.divider()

    st.subheader("What did we find?")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final explanatory power",
        "27.6%",
        help="Model 3 explains 27.6% of the observed variation in Institutional Trust."
    )

    c2.metric(
        "Left Behind Index β",
        "−0.459",
        help="Standardized coefficient from the final model."
    )

    c3.metric(
        "Statistical significance",
        "p < .001",
        help="Based on HC3 robust standard errors."
    )

    st.success("""
### Main result

The **Left Behind Index is the strongest standardized predictor**
of Institutional Trust among the variables included in the final model.
""")

    st.markdown("""
### Interpretation

People who report stronger feelings of being left behind tend to report
**substantially lower trust in institutions**.

This relationship remains after accounting for:

- household income;
- education;
- age;
- East/West Germany;
- migration background;
- political interest;
- Subjective Social Class.

The explanatory power of the model rises from **10.7% to 27.6%**
when the Left Behind Index is introduced.

That is an increase of **16.9 percentage points**.

By contrast, adding Subjective Social Class increases explanatory power
only from **8.8% to 10.7%**.

Household Income is not statistically significant in the final model.
""")

    st.info("""
The analysis identifies a statistical association. It does not demonstrate
that feeling left behind causes lower institutional trust.
""")

# ============================================================
# DEMOCRATIC SATISFACTION
# ============================================================

with tab3:

    st.header("Democratic Satisfaction")

    st.subheader("What was actually asked?")

    st.markdown("""
Unlike Institutional Trust, this outcome is based on **one direct
survey question**.

Respondents were asked:

> **“How satisfied are you with the way democracy works in Germany?”**
""")

    st.info("""
**q119 — Democracy: Satisfaction**

**1 = Very satisfied**  
**2 = Fairly satisfied**  
**3 = Not very satisfied**  
**4 = Not at all satisfied**
""")

    st.markdown("""
Because higher values mean **greater dissatisfaction**, a positive
regression coefficient means that stronger feelings of being left behind
are associated with **lower democratic satisfaction**.
""")

    st.caption(
        "GLES variable: q119 — Democracy: Satisfaction (4-point scale)."
    )

    st.divider()

    st.subheader("What did we find?")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final explanatory power",
        "22.2%",
        help="Model 3 explains 22.2% of the observed variation in Democratic Satisfaction."
    )

    c2.metric(
        "Left Behind Index β",
        "0.395",
        help="Positive because higher q119 values represent greater dissatisfaction."
    )

    c3.metric(
        "Statistical significance",
        "p < .001",
        help="Based on HC3 robust standard errors."
    )

    st.success("""
### Main result

The **Left Behind Index is the strongest standardized predictor**
in the final Democratic Satisfaction model.
""")

    st.markdown("""
### Interpretation

People reporting stronger feelings of being left behind also tend to be
**less satisfied with the way democracy works in Germany**.

The explanatory power of the model increases from **9.6% to 22.2%**
when the Left Behind Index is introduced.

That is an increase of **12.6 percentage points**.

By comparison, adding Subjective Social Class increases explanatory
power only from **8.5% to 9.6%**.

This suggests that feeling economically or socially overlooked captures
something about democratic dissatisfaction that income and perceived
social class alone do not.
""")

    st.info("""
The analysis describes an association and should not be interpreted as
evidence that feeling left behind causes democratic dissatisfaction.
""")

# ============================================================
# PARTY REPRESENTATION
# ============================================================

with tab4:

    st.header("Party Representation")

    st.subheader("What was actually asked?")

    st.markdown("""
This outcome is also based on **one direct survey question**.

Respondents were asked:

> **“Do you think that any of the parties in Germany represent your
> personal political views well?”**
""")

    st.info("""
**q141 — Political Parties: Representation of Interests**

**1 = Yes**  
**2 = No**

“Don't know” and missing responses were treated as missing values
in the analysis.
""")

    st.markdown("""
Because **2 = No**, higher values represent **lack of party representation**.

Therefore, the positive Left Behind coefficient means that stronger
feelings of being left behind are associated with a greater tendency
to report that **no political party represents one's views well**.
""")

    st.caption(
        "GLES variable: q141 — Political Parties: Representation of Interests."
    )

    st.divider()

    st.subheader("What did we find?")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Final explanatory power",
        "5.3%",
        help="Model 3 explains 5.3% of the observed variation in Party Representation."
    )

    c2.metric(
        "Left Behind Index β",
        "0.128",
        help="Positive because higher q141 values mean that respondents do not feel represented by a party."
    )

    c3.metric(
        "Statistical significance",
        "p < .001",
        help="Based on HC3 robust standard errors."
    )

    st.success("""
### Main result

Feeling left behind is associated with **lower perceived party representation**,
but the relationship is much weaker than for Institutional Trust and
Democratic Satisfaction.
""")

    st.markdown("""
### Interpretation

The final model explains only **5.3%** of variation in Party Representation.

Adding the Left Behind Index increases explanatory power from
**3.9% to 5.3%** — a gain of only **1.4 percentage points**.

This is substantially smaller than the increases observed for:

- Institutional Trust: **+16.9 percentage points**
- Democratic Satisfaction: **+12.6 percentage points**

Political Interest is the strongest predictor in this model.

This is an important finding: **feeling left behind is not equally related
to every dimension of democratic connection**.

It is much more strongly associated with trust in institutions and
satisfaction with democracy than with whether a person feels represented
by a political party.
""")

    st.info("""
The low R² also indicates that most differences in Party Representation
are related to factors not captured by the variables included in these models.
""")

# ============================================================
# METHODOLOGICAL NOTE
# ============================================================

st.divider()

st.subheader("Methodological confidence")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Analytical sample", "5,039")
c2.metric("Left Behind α", "0.753")
c3.metric("Factor 1 eigenvalue", "2.323")
c4.metric("Predictor VIF", "< 2")

st.markdown("""
The four items of the Left Behind Index showed acceptable internal
consistency and a clear one-factor structure.

The Institutional Trust Index also showed high internal consistency
(**Cronbach's α ≈ 0.889**).

No meaningful multicollinearity was detected. Because the regression
diagnostics indicated heteroscedasticity, statistical significance and
confidence intervals are based on **HC3 robust standard errors**.
""")

st.divider()

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

Left Behind Index: q46a–q46d.
Institutional Trust Index: q79a–q79g and q79i.
Democratic Satisfaction: q119.
Party Representation: q141.

The analyses use cross-sectional observational data.
Results describe statistical associations and should not be interpreted
as evidence of cause and effect.
""")