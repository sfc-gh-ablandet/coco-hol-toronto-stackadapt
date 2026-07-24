import streamlit as st

st.title("Workshop agenda")

AGENDA = [
    ("12:45 PM", "Arrival & Coffee", None, None),
    ("1:00 PM", "Welcome & Workshop Overview", None, None),
    ("1:10 PM", "Session 1: Data Prep", "15 min", "1"),
    ("1:25 PM", "Session 2: Cortex Analyst & Semantic Views", "20 min", "2"),
    ("1:45 PM", "Session 3: Cortex Search", "15 min", "3"),
    ("2:00 PM", ":orange-badge[BREAK]", None, None),
    ("2:10 PM", "Session 4: Cortex Agents", "20 min", "4"),
    ("2:30 PM", "Session 5: CoWork", "15 min", "5"),
    ("2:45 PM", "Session 6: Streamlit", "15 min", "6"),
]

for time, title, duration, session_num in AGENDA:
    if session_num:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/play_circle: **{title}** :gray-badge[{duration}]")
    elif "BREAK" in title:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f"{title}")
    else:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":gray[{title}]")

st.space("medium")

st.markdown("##### What you'll build by end of session")
st.markdown("""
| Object Type | Count | Examples |
|-------------|-------|---------|
| **Tables** | 9 | Campaign performance metrics, revenue pipeline, client health scores, audience segments |
| **Cortex Search Services** | 1 | REVOPS_SEARCH |
| **Semantic Views** | 1 | REVOPS_ANALYTICS_VIEW with relationships, metrics, and AI instructions |
| **Cortex Agents** | 1 | REVOPS_AGENT with Analyst + Search + custom tools |
| **Streamlit Apps** | 1 | Operations dashboard with AI chat |
""")

st.space("small")

st.markdown("##### Location")
with st.container(border=True):
    st.markdown("""
:material/location_on: **Snowflake Office, Toronto, ON**

July 30, 2026 — 1:00 PM to 3:00 PM
""")
