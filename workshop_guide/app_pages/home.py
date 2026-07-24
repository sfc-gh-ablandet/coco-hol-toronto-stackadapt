import streamlit as st

st.title("StackAdapt RevOps AI Workshop")
st.markdown("Building Intelligence for Programmatic Advertising Revenue Operations with Snowflake AI")

st.space("small")

col1, col2, col3 = st.columns(3)
col1.metric("Sections", "6", help="Hands-on lab sections")
col2.metric("Prompts", "16", help="Total prompts across all tools")
col3.metric("Duration", "2 hrs", help="Total workshop time")

st.space("medium")

st.markdown("#### How this workshop works")

st.markdown("""
Each section has **numbered prompts** that you copy and paste into the appropriate tool:

- **Cortex Code** — for building infrastructure, creating objects, and writing SQL/Python
- **Cortex Analyst** — for testing natural language queries against your semantic view
- **Snowflake CoWork** — for collaborative data exploration and analysis

All prompts build on each other sequentially — run them in order throughout the morning.
""")

st.space("small")

st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
StackAdapt is a leading programmatic advertising platform powering campaigns across display, native, video, and CTV channels for hundreds of advertisers globally. Their revenue operations are volume- and performance-driven: revenue scales with advertiser media spend processed through their AI-optimized DSP, campaign efficiency, and client retention.

Today we'll build an AI-powered RevOps analytics platform that combines campaign performance data, revenue pipeline insights, client health monitoring, and operational knowledge into a single intelligent system — demonstrating how Cortex Code can accelerate productivity for revenue operations, performance analytics, and audience insights.

We'll build a complete AI platform covering:

| Data type | Examples |
|-----------|---------|
| **Structured** | Campaign metrics, revenue records, client health scores, sales pipeline |
| **Unstructured** | Optimization playbooks, incident reports, best practices documentation |
| **Time series** | Daily campaign performance (impressions, clicks, conversions, spend) |
""")

st.space("small")

st.markdown("#### What we're building")

with st.container(border=True):
    st.markdown("""
In 2 hrs, we build a complete AI-powered operations platform:

**1. Data Foundation** — Load structured and unstructured operations data into Snowflake from pre-generated CSV files.

**2. Natural Language Analytics** — Create a Semantic View over operational tables and query them with plain English via Cortex Analyst.

**3. Intelligent Search** — Build a Cortex Search service over safety documents and inspection reports for hybrid semantic + keyword search.

**4. AI Agents** — Create a Cortex Agent that orchestrates structured data queries AND document search through a single conversational interface.

**5. Collaborative AI** — Use CoWork to collaboratively analyze data with AI assistance.

**6. Operations Dashboard** — Deploy a Streamlit app with live KPIs, charts, and an AI chat interface.
""")

st.space("small")

st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- Snowflake account with **ACCOUNTADMIN** role — see **Getting Started** in the sidebar to provision a free trial
- **Cortex Code** open in Snowsight and connected to your account
- Cross-region inference enabled (for Cortex LLM functions)
""")

st.space("medium")
st.caption("Built for the July 30, 2026 workshop  :material/location_on:  Snowflake Office, Toronto, ON")
