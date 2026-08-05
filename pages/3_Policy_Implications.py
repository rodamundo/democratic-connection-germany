import streamlit as st

st.set_page_config(
    page_title="Policy Implications",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Policy Implications")

st.markdown(
    """
    The findings suggest that democratic disconnection cannot be understood
    through income or education alone.

    Citizens' subjective experiences of recognition, belonging and exclusion
    are strongly associated with how they evaluate democratic institutions.
    """
)

st.divider()

st.header("What this may mean for democratic organizations")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        ### 1. Participation is not enough

        Creating opportunities for participation may have limited impact if
        citizens still feel socially ignored, disrespected or disconnected
        from institutions.
        """
    )

    st.markdown(
        """
        ### 2. Recognition matters

        Democratic initiatives should consider whether participants feel that
        their lived experiences and contributions are genuinely recognized.
        """
    )

with col2:
    st.markdown(
        """
        ### 3. Different outcomes require different strategies

        Social Disconnection is strongly associated with Institutional Trust
        and Democratic Satisfaction, but much less with Political Representation.

        This suggests that one intervention may not influence every dimension
        of democratic connection equally.
        """
    )

    st.markdown(
        """
        ### 4. Go beyond socioeconomic targeting

        Income and education remain relevant social indicators, but they may
        not identify everyone who feels excluded from democratic life.
        """
    )

st.divider()

st.warning(
    """
    These are practical interpretations of statistical associations, not proven
    causal effects. The analysis does not demonstrate that reducing Social
    Disconnection would automatically increase democratic trust.
    """
)

st.divider()

st.header("Questions for practice")

st.markdown(
    """
    - How can democratic organizations identify people who feel socially disconnected?
    - Are participation spaces accessible beyond already engaged and highly educated groups?
    - How can lived experience be incorporated into programme design?
    - Which interventions strengthen trust, and which improve political representation?
    """
)