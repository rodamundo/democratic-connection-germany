import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Feeling Left Behind and Democracy in Germany",
    page_icon="🏛️",
    layout="wide"
)


# ============================================================
# HELPERS — VISUAL EXPLAINERS FOR "MODEL FIT" / R²
# ============================================================

def build_gap_chart():
    """Illustrative scatter chart showing prediction 'gaps' shrinking
    when information is added. Uses synthetic data — NOT real GLES
    values — purely to teach the concept of model fit visually."""

    rng = np.random.default_rng(7)
    n = 22
    x = rng.uniform(1, 5, n)
    true_trend = 9 - 1.3 * x
    y = np.clip(true_trend + rng.normal(0, 1.1, n), 1, 11)
    mean_y = y.mean()
    coeffs = np.polyfit(x, y, 1)
    fit_y = np.polyval(coeffs, x)
    order = np.argsort(x)

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            "Guessing the same number for everyone",
            "Adjusting the guess per person"
        ),
        horizontal_spacing=0.12
    )

    for xi, yi in zip(x, y):
        fig.add_trace(go.Scatter(
            x=[xi, xi], y=[yi, mean_y], mode="lines",
            line=dict(color="#B7C1E0", width=1.5),
            showlegend=False, hoverinfo="skip"
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=sorted(x), y=[mean_y] * n, mode="lines",
        line=dict(color="#F96167", width=3), name="Model's guess"
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="markers",
        marker=dict(color="#1E2761", size=9), name="Actual person"
    ), row=1, col=1)

    for xi, yi, pi in zip(x, y, fit_y):
        fig.add_trace(go.Scatter(
            x=[xi, xi], y=[yi, pi], mode="lines",
            line=dict(color="#B7C1E0", width=1.5),
            showlegend=False, hoverinfo="skip"
        ), row=1, col=2)
    fig.add_trace(go.Scatter(
        x=x[order], y=fit_y[order], mode="lines",
        line=dict(color="#F96167", width=3),
        name="Model's guess", showlegend=False
    ), row=1, col=2)
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="markers",
        marker=dict(color="#1E2761", size=9),
        name="Actual person", showlegend=False
    ), row=1, col=2)

    fig.update_xaxes(title_text="Feeling Left Behind (illustrative)", row=1, col=1)
    fig.update_xaxes(title_text="Feeling Left Behind (illustrative)", row=1, col=2)
    fig.update_yaxes(title_text="Institutional Trust (1–11)", range=[0, 12], row=1, col=1)
    fig.update_yaxes(range=[0, 12], row=1, col=2)

    fig.update_layout(
        height=420,
        legend=dict(orientation="h", yanchor="bottom", y=-0.32, x=0.28),
        margin=dict(t=50, b=70, l=10, r=10),
    )
    return fig


def build_donut(pct, label, color="#1E2761"):
    """Small donut showing the identified slice vs. the unknown
    remainder — the 'slice of the pizza' metaphor, made visual."""

    fig = go.Figure(data=[go.Pie(
        labels=["Accounted for", "Not captured by this model"],
        values=[pct, 100 - pct],
        hole=0.7,
        marker=dict(colors=[color, "#E7EAF4"]),
        textinfo="none",
        sort=False,
        direction="clockwise",
        hoverinfo="skip",
    )])
    fig.update_layout(
        showlegend=False,
        height=220,
        margin=dict(t=10, b=10, l=10, r=10),
        annotations=[dict(
            text=f"<b>{pct:.1f}%</b><br><span style='font-size:11px;color:#5B6B9C'>{label}</span>",
            x=0.5, y=0.5, font_size=20, showarrow=False, font_color="#1E2761"
        )],
    )
    return fig


# ============================================================
# HOME
# ============================================================

def home():

    st.title("🏛️ Feeling Left Behind and Democracy in Germany")

    st.subheader(
        "What helps us understand why people relate differently to democracy?"
    )

    st.markdown("""
This project explores whether people's **social and economic position**
is enough to understand democratic disconnection in Germany, or whether
another dimension also matters:

### **How people experience their place in society.**
""")

    st.divider()


    # ========================================================
    # 1. WHAT ARE WE TRYING TO UNDERSTAND?
    # ========================================================

    st.header("1. What are we trying to understand?")

    st.markdown("""
People can relate to democracy in different ways.

This project looks at **three different outcomes**:
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.markdown("""
**Do people trust important institutions?**

Respondents rated eight institutions from:

**1 = Do not trust at all**

to

**11 = Trust completely**
""")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.markdown("""
**Are people satisfied with how democracy works in Germany?**

Responses range from:

**1 = Very satisfied**

to

**4 = Not at all satisfied**
""")

    with c3:
        with st.container(border=True):

            st.markdown("### 👥 Party Representation")

            st.markdown("""
**Does any political party represent the person's views well?**

Respondents answer:

**Yes / No**
""")

    st.divider()


    # ========================================================
    # 2. HOW IS THE QUESTION TESTED? (THREE MODELS OVERVIEW)
    # ========================================================

    st.header("2. How is the question tested?")

    st.markdown("""
To find out what helps explain these three outcomes, the analysis
builds understanding in **three stages**, adding one layer of
information at a time.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### Model 1")
            st.markdown("**Traditional Factors**")

            st.markdown("""
💰 Household Income  
🎓 Education  
🎂 Age  
📍 East / West Germany  
🌍 Migration Background  
🗳️ Political Interest
""")

    with c2:
        with st.container(border=True):

            st.markdown("### Model 2")
            st.markdown("**+ Social Class**")

            st.markdown("""
Everything in Model 1

**+**

🪜 Subjective Social Class

*Where the respondent believes they belong in the social hierarchy.*
""")

    with c3:
        with st.container(border=True):

            st.markdown("### Model 3")
            st.markdown("**+ Feeling Left Behind**")

            st.markdown("""
Everything in Model 2

**+**

🧩 Left Behind Index

*A new measure introduced in this project — explained in detail
below.*
""")

    st.info("""
Each stage adds one layer of information. The central test is simple:

> **Does the last layer — Feeling Left Behind — help us understand
> democratic attitudes beyond everything already captured by income,
> education, age, region, migration background, political interest
> and perceived social class?**

To answer that, we first need to unpack what Feeling Left Behind
actually measures.
""")

    st.divider()


    # ========================================================
    # 3. WHAT IS FEELING LEFT BEHIND?
    # ========================================================

    st.header("3. What is Feeling Left Behind?")

    st.markdown("""
Even after knowing someone's income, education and perceived social
class, we may still know very little about **how that person feels
society treats people like them**. That is what this index tries to
capture.
""")

    st.success("""
# 🧩 Feeling Left Behind

Feeling Left Behind captures whether people feel that **people like them**
are overlooked, insufficiently recognized, underserved or unable to
freely express their views.
""")

    st.markdown("""
The GLES survey contains four questions covering:
""")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):

            st.markdown("### 💶 Economic attention")

            st.write(
                "Are the economic concerns of people like me being overlooked?"
            )

    with c2:
        with st.container(border=True):

            st.markdown("### 👏 Recognition")

            st.write(
                "Is the contribution of people like me recognized?"
            )

    with c3:
        with st.container(border=True):

            st.markdown("### 🏥 Services")

            st.write(
                "Do people like me receive adequate access to essential services?"
            )

    with c4:
        with st.container(border=True):

            st.markdown("### 🗣️ Voice")

            st.write(
                "Do people like me feel free to express their opinions?"
            )

    st.markdown("""
The four answers are combined into a single score for each respondent:
""")

    c1, c2, c3 = st.columns([1, 1.4, 1])

    with c1:
        st.metric(
            "Lower Feeling Left Behind",
            "1"
        )

    with c2:
        st.markdown("""
### 4 answers

### ↓

### Average

### ↓

## Left Behind Index
""")

    with c3:
        st.metric(
            "Higher Feeling Left Behind",
            "5"
        )

    st.info("""
There is **no cut-off** separating people into “left behind” and
“not left behind”.

The index measures **degrees of Feeling Left Behind**, from lower to higher.
""")

    st.markdown("""
So the central test from Model 3 becomes:

> ### Does knowing how left behind someone feels help us understand
> ### their democratic attitudes beyond everything already included
> ### in Models 1 and 2?
""")

    st.divider()


    # ========================================================
    # 3B. WHAT DOES "MODEL FIT" ACTUALLY MEAN?
    # ========================================================

    st.header("Before the numbers: what does \"model fit\" mean?")

    st.markdown("""
Imagine trying to guess how much each of the **5,039 people** in this
survey trusts institutions, using only what you know about them.
You won't guess perfectly — but some information helps more than
others. The chart below shows this idea: dots are people, the red
line is the model's guess, and the **gray lines are the gaps** —
how far off each guess is.
""")

    st.plotly_chart(build_gap_chart(), width="stretch")

    st.info("""
**"Model fit" (R²) measures how much smaller those gray gaps get**
when information is added — from guessing the same number for
everyone, to adjusting the guess per person.

*(Illustrative example with made-up numbers, used only to explain the
idea — not real survey data. The actual model uses 7 variables at
once, which can't be drawn on a simple chart like this.)*
""")

    st.markdown("""
Here is what that looks like for the real results. Each circle shows:
of all the differences between real respondents, what share can the
final model account for?
""")

    d1, d2, d3 = st.columns(3)

    with d1:
        st.plotly_chart(build_donut(27.6, "Institutional Trust"), width="stretch")

    with d2:
        st.plotly_chart(build_donut(22.2, "Democratic Satisfaction"), width="stretch")

    with d3:
        st.plotly_chart(
            build_donut(4.6, "Party Representation", color="#F96167"),
            width="stretch"
        )

    st.caption("""
The colored slice is what the model accounts for; the gray slice is
everything else — reasons not captured by this survey. Party
Representation uses a different statistic (Pseudo R²) — see the
Results page for details.
""")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.markdown("### ❌ It does NOT mean")
            st.markdown("""
**"27.6% of people trust institutions."**

It is not a share of people, and not a level of trust.
""")

    with c2:
        with st.container(border=True):
            st.markdown("### ✅ It DOES mean")
            st.markdown("""
**"We can account for 27.6% of the differences between
people in how much they trust institutions."**

The remaining ~72% comes from things not measured here —
personality, specific experiences, events not captured by this survey.
""")

    st.divider()


    # ========================================================
    # 4. MAIN RESULTS
    # ========================================================

    st.header("4. What happens when Feeling Left Behind is added?")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):

            st.markdown("### 🏛️ Institutional Trust")

            st.metric(
                "Model fit",
                "27.6%",
                delta="+16.9 pp"
            )

            st.markdown("""
**Before:** 10.7%

**After adding Feeling Left Behind:** 27.6%
""")

            st.caption("OLS R²")

    with c2:
        with st.container(border=True):

            st.markdown("### 🗳️ Democratic Satisfaction")

            st.metric(
                "Model fit",
                "22.2%",
                delta="+12.6 pp"
            )

            st.markdown("""
**Before:** 9.6%

**After adding Feeling Left Behind:** 22.2%
""")

            st.caption("OLS R²")

    with c3:
        with st.container(border=True):

            st.markdown("### 👥 Party Representation")

            st.metric(
                "Model fit",
                "4.6%",
                delta="+1.2 pp"
            )

            st.markdown("""
**Before:** 3.4%

**After adding Feeling Left Behind:** 4.6%
""")

            st.caption(
                "McFadden Pseudo R² · Logistic regression"
            )

    st.info("""
### How should these percentages be read?

They are **not percentages of people who trust institutions or are
satisfied with democracy**.

For example, the **27.6%** means that the final model can account for
27.6% of the differences in Institutional Trust between respondents.

Party Representation uses a different statistic, Pseudo R², because
the outcome is Yes/No. Its numerical value should not be directly
compared with the two OLS R² values.
""")

    st.divider()


    # ========================================================
    # 5. MAIN MESSAGE
    # ========================================================

    st.header("5. What does this tell us?")

    st.success("""
### Socioeconomic position does not tell the whole story.

Income, education, age, region and social class provide useful information.

But for **Institutional Trust** and **Democratic Satisfaction**, knowing
how left behind people feel adds substantially more information.

The pattern is much weaker for **Party Representation**, suggesting that
democratic disconnection has different dimensions.
""")

    st.markdown("""
In simple terms:

> ## What people have matters.
>
> ## But how people feel seen, recognized, served and heard may matter too.
""")

    st.warning("""
The analysis identifies **statistical associations**, not cause and effect.

It cannot establish whether Feeling Left Behind causes lower trust or
democratic dissatisfaction, or whether people who already distrust
institutions are more likely to report feeling left behind.
""")

    st.divider()


    # ========================================================
    # PROJECT
    # ========================================================

    st.header("About the analysis")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Survey respondents", "7,336")
    c2.metric("Analytical sample", "5,039")
    c3.metric("Democratic outcomes", "3")
    c4.metric("Regression models", "9")

    st.caption("""
**Source:** German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.
""")


# ============================================================
# NAVIGATION
# ============================================================

home_page = st.Page(
    home,
    title="Home",
    icon="🏠",
    default=True
)

left_behind_page = st.Page(
    "pages/1_Feeling_Left_Behind.py",
    title="Feeling Left Behind",
    icon="🧩"
)

research_page = st.Page(
    "pages/2_Research.py",
    title="Research",
    icon="📚"
)

results_page = st.Page(
    "pages/3_Results.py",
    title="Results",
    icon="📊"
)

methodology_page = st.Page(
    "pages/4_Methodology.py",
    title="Methodology",
    icon="🔬"
)

policy_page = st.Page(
    "pages/5_Policy_Implications.py",
    title="Policy Implications",
    icon="💡"
)

about_page = st.Page(
    "pages/6_About.py",
    title="About",
    icon="👤"
)

pg = st.navigation([
    home_page,
    left_behind_page,
    research_page,
    results_page,
    methodology_page,
    policy_page,
    about_page
])

pg.run()