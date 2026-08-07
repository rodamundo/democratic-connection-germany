[1mdiff --git a/streamlit_app.py b/streamlit_app.py[m
[1mindex e69de29..611aed2 100644[m
[1m--- a/streamlit_app.py[m
[1m+++ b/streamlit_app.py[m
[36m@@ -0,0 +1,79 @@[m
[32m+[m[32mimport streamlit as st[m
[32m+[m
[32m+[m[32mst.set_page_config([m
[32m+[m[32m    page_title="Beyond Socioeconomic Status",[m
[32m+[m[32m    page_icon="🏛️",[m
[32m+[m[32m    layout="wide"[m
[32m+[m[32m)[m
[32m+[m
[32m+[m[32mst.title("🏛️ Beyond Socioeconomic Status")[m
[32m+[m
[32m+[m[32mst.subheader([m
[32m+[m[32m    "How Feeling Left Behind Shapes Democratic Attitudes in Germany"[m
[32m+[m[32m)[m
[32m+[m
[32m+[m[32mst.divider()[m
[32m+[m
[32m+[m[32mst.markdown("""[m
[32m+[m[32m## Research Question[m
[32m+[m
[32m+[m[32m**To what extent does feeling left behind explain democratic attitudes beyond traditional socioeconomic characteristics?**[m
[32m+[m
[32m+[m[32mThis project investigates whether people's perception of being left behind[m
[32m+[m[32mhelps explain democratic attitudes more strongly than objective socioeconomic[m
[32m+[m[32mcharacteristics such as household income and education.[m
[32m+[m
[32m+[m[32mThe analysis uses data from the **German Longitudinal Election Study (GLES 2025)**.[m
[32m+[m[32m""")[m
[32m+[m
[32m+[m[32mst.divider()[m
[32m+[m
[32m+[m[32mcol1, col2, col3, col4 = st.columns(4)[m
[32m+[m
[32m+[m[32mwith col1:[m
[32m+[m[32m    st.metric("Respondents", "7,336")[m
[32m+[m
[32m+[m[32mwith col2:[m
[32m+[m[32m    st.metric("Analytical Sample", "5,039")[m
[32m+[m
[32m+[m[32mwith col3:[m
[32m+[m[32m    st.metric("Regression Models", "9")[m
[32m+[m
[32m+[m[32mwith col4:[m
[32m+[m[32m    st.metric("Composite Indices", "2")[m
[32m+[m
[32m+[m[32mst.divider()[m
[32m+[m
[32m+[m[32mst.success("""[m
[32m+[m[32m## Key Finding[m
[32m+[m
[32m+[m[32mThe **Left Behind Index** remained the strongest predictor of[m
[32m+[m[32m**Institutional Trust** and **Democratic Satisfaction**, even after[m
[32m+[m[32mcontrolling for household income, education, age, East/West Germany,[m
[32m+[m[32mmigration background, political interest and Subjective Social Class.[m
[32m+[m
[32m+[m[32mIts association with **Political Representation** was substantially weaker.[m
[32m+[m[32m""")[m
[32m+[m
[32m+[m[32mst.divider()[m
[32m+[m
[32m+[m[32mst.markdown("""[m
[32m+[m[32m## Explore the Project[m
[32m+[m
[32m+[m[32mUse the navigation menu to explore:[m
[32m+[m
[32m+[m[32m- 📚 **Research** — research design, variables and analytical sample[m
[32m+[m[32m- 📊 **Results** — regression models and key findings[m
[32m+[m[32m- 🔬 **Methodology** — index validation and regression diagnostics[m
[32m+[m[32m- 💡 **Policy Implications** — practical interpretation of the findings[m
[32m+[m[32m- 👤 **About** — project background and author[m
[32m+[m[32m""")[m
[32m+[m
[32m+[m[32mst.divider()[m
[32m+[m
[32m+[m[32mst.caption("""[m
[32m+[m[32m**Source:** German Longitudinal Election Study (GLES 2025),[m
[32m+[m[32mPost-Election Cross-Section (ZA10100).[m
[32m+[m
[32m+[m[32mResults describe **statistical associations rather than causal relationships**.[m
[32m+[m[32m""")[m
\ No newline at end of file[m
