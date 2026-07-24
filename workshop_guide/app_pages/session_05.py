import streamlit as st
from components import render_session_header, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(5, "CoWork", "2:30 PM", "15 min", "Collaborative AI analysis with CoWork")

render_technologies_used([
    {"name": "Snowflake CoWork", "description": "An AI-powered collaborative workspace inside Snowsight where you can analyze data, generate insights, and share findings.", "icon": "group"},
    {"name": "Data Analysis", "description": "CoWork can query your Snowflake data, generate visualizations, and provide insights without writing SQL.", "icon": "analytics"},
    {"name": "Sharing & Collaboration", "description": "CoWork sessions can be shared with team members for collaborative data exploration.", "icon": "share"},
])

st.markdown("---")

st.markdown("#### :material/open_in_new: Open CoWork")
with st.container(border=True):
    st.markdown("""
In Snowsight, click **CoWork** in the left navigation panel. Start a new conversation.

CoWork discovers your tables in `ADTECH_AI.REVOPS` automatically. Paste each question below one at a time.
""")

st.space("small")

st.markdown("#### :material/chat: Questions to ask CoWork")
st.caption("Copy and paste each question into CoWork individually.")

questions = [
    ("Revenue Trend Analysis", "Analyze our monthly platform revenue trend over the past 6 months. Break it down by advertiser tier (Gold, Silver, Bronze). Are there any concerning trends? Which tier is driving the most growth?"),
    ("Campaign Channel Performance", "Compare campaign performance across our four channels (display, native, video, CTV). Which channel delivers the best ROAS? Which has the highest CTR? Create a visualization showing the comparison."),
    ("At-Risk Client Identification", "Identify advertisers with high retention risk. For each, show their current engagement score, performance score, monthly revenue, and how their metrics have changed over the past 3 months. Which ones should the AM team prioritize?"),
    ("Pipeline & Revenue Forecast", "Using our sales pipeline data, calculate the weighted pipeline value by stage. Combined with current revenue run-rate from our top 10 advertisers, what does our revenue outlook look like for the next quarter?"),
    ("Audience Optimization Opportunity", "Which audience segment categories are most used in our top-performing campaigns (highest ROAS)? Are there segment types that are underutilized but available? Suggest 3 audience strategy recommendations.")
]

for title, question in questions:
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.code(question, language="text", wrap_lines=True)

st.space("small")

render_explanation("How CoWork works", """
**CoWork** is Snowflake's collaborative AI workspace — different from Cortex Code:

| Tool | Best for |
|------|----------|
| Cortex Code | Building infrastructure, creating objects, writing SQL |
| CoWork | Exploring data, generating insights, team collaboration |
| Cortex Agent | End-user Q&A interface (deployed as a product) |
""")

render_key_concepts([
    {"term": "CoWork", "definition": "Snowflake's collaborative AI workspace. Conversational interface that queries data, creates visualizations, and generates insights."},
    {"term": "Context Maintenance", "definition": "CoWork maintains conversation history so follow-up questions build on previous analysis."},
])

render_what_you_built([
    "Explored operations data through conversational AI",
    "Generated visualizations and cross-table analysis",
    "Demonstrated the CoWork collaborative analysis pattern",
])
