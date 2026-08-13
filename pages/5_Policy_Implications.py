import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.title("💡 Policy Implications")

st.subheader(
    "What might these findings mean for how democratic disconnection is understood?"
)

st.markdown("""
This page moves carefully from **statistical evidence** to
**possible policy interpretation**.

The analysis does **not** show that any specific intervention
will increase trust, satisfaction or representation.
""")

st.warning("""
### Association ≠ causation

The study identifies statistical associations in cross-sectional
survey data.

It does **not** demonstrate that Feeling Left Behind causes
lower trust, greater dissatisfaction or lower party representation.
""")

st.divider()


# ============================================================
# 1. START WITH THE EVIDENCE
# ============================================================

st.header("1. Start with what the data actually show")

st.markdown("""
The strongest results concern **Institutional Trust** and
**Democratic Satisfaction**.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("""
### 🏛️ Institutional Trust

🧩 Feeling Left Behind

# ↑

# ↓

🏛️ Institutional Trust

**Higher Feeling Left Behind is associated with lower trust.**
""")

with c2:
    with st.container(border=True):
        st.markdown("""
### 🗳️ Democratic Satisfaction

🧩 Feeling Left Behind

# ↑

# ↓

🗳️ Democratic Satisfaction

**Higher Feeling Left Behind is associated with greater
democratic dissatisfaction.**
""")

with c3:
    with st.container(border=True):
        st.markdown("""
### 👥 Party Representation

🧩 Feeling Left Behind

# ↑

# ↓

👥 Party Representation

**Higher Feeling Left Behind is associated with lower odds
of feeling represented by a party.**
""")

st.info("""
These relationships remain after accounting for socioeconomic,
demographic and political characteristics included in the models.
""")

st.divider()


# ============================================================
# 2. WHAT CHANGES WHEN FLB IS ADDED?
# ============================================================

st.header("2. What changes when Feeling Left Behind is added?")

st.markdown("""
The models already contain information such as income, education,
age, region, migration background, political interest and
Subjective Social Class.

The question is whether Feeling Left Behind adds information
beyond these characteristics.
""")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.markdown("""
Before Feeling Left Behind:

# **10.7%**

After Feeling Left Behind:

# **27.6%**
""")

        st.metric(
            "Increase in OLS R²",
            "+16.9 pp"
        )

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.markdown("""
Before Feeling Left Behind:

# **9.6%**

After Feeling Left Behind:

# **22.2%**
""")

        st.metric(
            "Increase in OLS R²",
            "+12.6 pp"
        )

st.success("""
### Interpretation

For Trust and Democratic Satisfaction, Feeling Left Behind
adds substantial explanatory information beyond the variables
already included in the models.
""")

st.divider()


# ============================================================
# 3. FROM DATA TO INTERPRETATION
# ============================================================

st.header("3. From evidence to interpretation")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):

        st.markdown("""
### 📊 What the analysis shows

- Feeling Left Behind is associated with lower Institutional Trust.
- Feeling Left Behind is associated with greater Democratic Dissatisfaction.
- Feeling Left Behind is also associated with lower Party Representation.
- The increase in model fit is much larger for Trust and Satisfaction.
""")

with c2:
    with st.container(border=True):

        st.markdown("""
### 💡 What this may suggest

Understanding democratic disconnection may require attention to
more than objective socioeconomic position.

People's perceptions of whether they are **seen, recognized,
served and heard** may contain information that income and
social class alone do not capture.
""")

st.warning("""
The second column is an **interpretation of the findings**.

It should not be read as evidence that recognition, services or
voice individually cause democratic trust.
""")

st.divider()


# ============================================================
# 4. FOUR DIMENSIONS
# ============================================================

st.header("4. Four dimensions for further investigation")

st.markdown("""
The Feeling Left Behind Index combines four dimensions from the
GLES survey.

These dimensions can help organize future research and policy
questions.
""")

st.info("""
### Important methodological point

The current analysis tests the **combined Feeling Left Behind Index**.

It does **not** estimate the independent causal effect of each of
the four dimensions below.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("""
### 💶 Economic attention

One part of the index asks whether respondents feel that the
economic situation of people like them receives too little
attention from society.

### Question for further investigation

Could perceptions of economic neglect contribute to broader
democratic disconnection?
""")

    with st.container(border=True):

        st.markdown("""
### 🏥 Access to services

Another component concerns whether people like the respondent
have adequate access to basic infrastructure and services.

Examples include:

- doctors;
- public transportation;
- schools;
- banks;
- post offices;
- Internet access.

### Question for further investigation

Can unequal or perceived unequal access to services contribute
to a sense of being overlooked?
""")

with c2:

    with st.container(border=True):

        st.markdown("""
### 👏 Social recognition

The index also captures whether people feel that people like them
receive sufficient recognition for the work they do.

### Question for further investigation

Could perceived lack of recognition be connected to democratic
distrust or dissatisfaction?
""")

    with st.container(border=True):

        st.markdown("""
### 🗣️ Voice

The fourth dimension concerns whether respondents feel that
people like them can freely express their views.

### Question for further investigation

How does perceived voice relate to broader feelings of social
and democratic inclusion?
""")

st.divider()


# ============================================================
# 5. NOT ONLY MATERIAL CONDITIONS
# ============================================================

st.header("5. Material conditions may not tell the whole story")

st.markdown("""
Income and education remain important indicators of social position.

But this analysis suggests that they do not capture all the
information associated with democratic trust and satisfaction.
""")

with st.container(border=True):

    st.markdown("""
### Two people can look similar socioeconomically...

They may have:

- similar income;
- similar education;
- similar age;
- similar region;
- similar social class.

### ...but still feel differently about society

One may feel:

- recognized;
- included;
- adequately served;
- able to express their views.

The other may feel the opposite.

The Feeling Left Behind Index attempts to capture this difference.
""")

st.success("""
### Possible implication

Social and democratic disconnection may not be identifiable using
economic indicators alone.

Subjective perceptions may also be useful signals for understanding
where disconnection is concentrated.
""")

st.divider()


# ============================================================
# 6. TRUST VS REPRESENTATION
# ============================================================

st.header("6. Democratic disconnection is not one single problem")

st.markdown("""
One of the most important findings is that Feeling Left Behind
does not improve all models equally.
""")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):

        st.markdown("### 🏛️ Institutional Trust")

        st.metric(
            "Increase in OLS R²",
            "+16.9 pp"
        )

        st.markdown("""
Large improvement after Feeling Left Behind is added.
""")

with c2:
    with st.container(border=True):

        st.markdown("### 🗳️ Democratic Satisfaction")

        st.metric(
            "Increase in OLS R²",
            "+12.6 pp"
        )

        st.markdown("""
Large improvement after Feeling Left Behind is added.
""")

with c3:
    with st.container(border=True):

        st.markdown("### 👥 Party Representation")

        st.metric(
            "Increase in Pseudo R²",
            "+1.2 pp"
        )

        st.markdown("""
Much smaller model-fit improvement.
""")

st.caption("""
The Party Representation value is McFadden Pseudo R² from logistic
regression and is not on the same numeric scale as the OLS R² values.
""")

st.success("""
### Possible implication

Distrust, dissatisfaction and lack of political representation
should not automatically be treated as the same problem.

Different dimensions of democratic disconnection may require
different explanations and different responses.
""")

st.divider()


# ============================================================
# 7. PARTY REPRESENTATION
# ============================================================

st.header("7. Party Representation requires particular caution")

st.markdown("""
Feeling Left Behind is still associated with whether people say
that a political party represents their views well.

However, the improvement in the Party Representation model is
much smaller than for Trust or Democratic Satisfaction.
""")

with st.container(border=True):

    st.markdown("""
### What this may mean

Feeling socially left behind and feeling politically unrepresented
are related, but they are **not the same phenomenon**.

Other political factors may be more important for explaining
party representation.
""")

st.info("""
In the current analysis, Political Interest is an important predictor
in the Party Representation model.

This reinforces the idea that political representation may depend
on mechanisms that differ from those behind institutional distrust
or democratic dissatisfaction.
""")

st.divider()


# ============================================================
# 8. WHAT POLICYMAKERS COULD MEASURE
# ============================================================

st.header("8. What could policymakers and researchers measure?")

st.markdown("""
A practical implication is not necessarily to launch a specific
intervention immediately.

A first step could be to improve **measurement and diagnosis**.
""")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("""
### Traditional indicators

💰 Income

🎓 Education

📍 Region

🎂 Age

🌍 Migration background

These remain useful for identifying socioeconomic differences.
""")

with c2:

    with st.container(border=True):

        st.markdown("""
### Possible complementary indicators

💶 Perceived economic attention

👏 Social recognition

🏥 Access to services

🗣️ Perceived voice

These could complement material indicators when studying
democratic disconnection.
""")

st.success("""
### Key idea

Instead of asking only:

**“What resources do people have?”**

researchers and policymakers could also ask:

**“Do people feel that people like them are seen, recognized,
served and heard?”**
""")

st.divider()


# ============================================================
# 9. WHAT NOT TO CLAIM
# ============================================================

st.header("9. What should not be concluded from this study?")

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.markdown("""
### ❌ The study does NOT show

- that Feeling Left Behind causes distrust;
- that improving services automatically increases trust;
- that recognition directly produces democratic satisfaction;
- that one policy can solve all forms of democratic disconnection;
- that the four components of the index have equal independent effects.
""")

with c2:

    with st.container(border=True):

        st.markdown("""
### ✅ The study DOES show

- systematic statistical associations;
- additional explanatory information from Feeling Left Behind;
- stronger model improvement for Trust and Satisfaction;
- a weaker model-fit improvement for Party Representation;
- a reason to investigate subjective social disconnection further.
""")

st.divider()


# ============================================================
# 10. QUESTIONS
# ============================================================

st.header("10. Questions raised by the findings")

st.markdown("""
The current analysis opens several questions that would require
additional research.
""")

st.info("""
### For researchers and policymakers

**Are economic indicators alone sufficient to identify people
experiencing democratic disconnection?**

**Can perceptions of recognition, inclusion, services and voice
improve how democratic disconnection is diagnosed?**

**Which of the four Feeling Left Behind dimensions are most strongly
associated with Institutional Trust and Democratic Satisfaction?**

**Do these relationships differ across regions, income groups or
social classes?**

**Why does Feeling Left Behind add much more explanatory information
for Trust and Satisfaction than for Party Representation?**

**Would longitudinal data show that changes in Feeling Left Behind
precede changes in democratic attitudes?**
""")

st.divider()


# ============================================================
# 11. NEXT RESEARCH STEP
# ============================================================

st.header("11. A logical next research step")

st.markdown("""
The current project treats Feeling Left Behind as one combined index.

A natural extension would be to test the four dimensions separately:
""")

with st.container(border=True):

    st.markdown("""
### Economic attention

### Recognition

### Services

### Voice

# ↓

### Which dimension is most strongly associated with each
### democratic outcome?
""")

st.info("""
This would help distinguish whether the observed relationship is
mainly associated with one dimension or whether the four dimensions
work together as a broader experience of social disconnection.
""")

st.divider()


# ============================================================
# FINAL TAKEAWAY
# ============================================================

st.header("Final takeaway")

st.success("""
# What people have matters.

# How people feel treated by society may matter too.

The results suggest that understanding democratic disconnection
may require looking at both **objective socioeconomic position**
and **subjective social experience**.

But identifying effective policy responses requires additional
causal and longitudinal research.
""")

st.caption("""
Source: German Longitudinal Election Study (GLES 2025),
Post-Election Cross-Section, ZA10100.

These policy implications are interpretations of statistical
associations and should not be treated as causal policy estimates.
""")