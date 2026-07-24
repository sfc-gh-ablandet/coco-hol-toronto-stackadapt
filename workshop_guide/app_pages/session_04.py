import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(4, "Cortex Agents", "2:10 PM", "20 min", "Cortex Agent with Analyst + Search + custom tools")

render_technologies_used([
    {"name": "Cortex Agent (CREATE AGENT)", "description": "An orchestrating AI that plans tasks, selects tools, executes them, reflects on results, and generates responses.", "icon": "smart_toy"},
    {"name": "Tool Orchestration", "description": "The Agent automatically routes questions to the right tool: Cortex Analyst for structured data, Cortex Search for documents, custom UDFs for logic.", "icon": "route"},
    {"name": "Custom Tools (UDFs)", "description": "User-defined functions that extend Agent capabilities with custom business logic.", "icon": "build"},
])


PROMPT_4_1 = """In ADTECH_AI.REVOPS, create a Cortex Agent called REVOPS_AGENT.

It should:
- Use auto as the orchestration model
- Have two tools: the REVOPS_ANALYTICS_VIEW semantic view (for structured data queries) and the REVOPS_SEARCH Cortex Search service (for unstructured document search)
- Include instructions defining it as the StackAdapt RevOps Assistant — helping revenue operations teams analyze campaign performance, monitor client health, forecast revenue, and find operational best practices, guiding it to use structured data for campaign metrics (CTR, CPA, ROAS), revenue analysis (take rate, platform fees), client health (engagement scores, retention risk), pipeline forecasting (deal amounts, probabilities), audience reach and search for optimization best practices, incident resolution history, campaign playbooks, client retention strategies, platform troubleshooting
- Mention domain context: Programmatic advertising DSP platform. Revenue = take-rate on advertiser media spend. Key metrics: CTR, CPA, ROAS, take rate, client health scores. Advertisers run campaigns across display, native, video, and CTV channels.
- Include 3-4 sample questions spanning both tools

Execute and show confirmation."""

render_prompt("Prompt 4.1", "Create the Cortex Agent", PROMPT_4_1)

render_explanation("What this prompt does", """
Creates a **Cortex Agent** combining structured analytics with document search:

- **Structured questions** → routed to Cortex Analyst via the semantic view
- **Unstructured questions** → routed to Cortex Search
- **Mixed questions** → Agent uses both tools and synthesizes
""")


PROMPT_4_2 = """Test our REVOPS_AGENT with these queries:

1. "What's our total platform revenue this quarter and which tier is growing fastest?" (structured — Analyst)
2. "What best practices should we follow for CTV campaign optimization?" (unstructured — Search)
3. "We have a Gold tier client with declining engagement — what's their revenue trend and what retention playbook should we use?" (mixed — both tools)
4. "Show me the pipeline weighted value by stage and tell me about any recent incidents that could affect deal closures" (mixed — both tools)


Show the responses and note which tools the agent selected."""

render_prompt("Prompt 4.2", "Test the Agent", PROMPT_4_2)

render_explanation("What this prompt does", """
Tests the agent with structured, unstructured, and mixed queries to validate tool routing.
""")


PROMPT_4_3 = """In ADTECH_AI.REVOPS, add a custom tool to the agent:

1. Create a UDF:

```sql
CREATE OR REPLACE FUNCTION ADTECH_AI.REVOPS.CALCULATE_CAMPAIGN_HEALTH(
    ctr FLOAT, viewability FLOAT, cpa FLOAT, target_cpa FLOAT
)
RETURNS VARIANT
LANGUAGE SQL
AS
$$
    SELECT OBJECT_CONSTRUCT(
        'ctr_score', LEAST(100, GREATEST(0, ctr * 5000)),
        'viewability_score', LEAST(100, GREATEST(0, viewability * 100)),
        'efficiency_score', CASE 
            WHEN cpa <= target_cpa * 0.8 THEN 100
            WHEN cpa <= target_cpa THEN 80
            WHEN cpa <= target_cpa * 1.2 THEN 60
            WHEN cpa <= target_cpa * 1.5 THEN 40
            ELSE 20
        END,
        'overall_health', ROUND(
            (LEAST(100, GREATEST(0, ctr * 5000)) * 0.3) +
            (LEAST(100, GREATEST(0, viewability * 100)) * 0.3) +
            (CASE 
                WHEN cpa <= target_cpa * 0.8 THEN 100
                WHEN cpa <= target_cpa THEN 80
                WHEN cpa <= target_cpa * 1.2 THEN 60
                WHEN cpa <= target_cpa * 1.5 THEN 40
                ELSE 20
            END * 0.4)
        , 1),
        'status', CASE
            WHEN (LEAST(100, GREATEST(0, ctr * 5000)) * 0.3 + LEAST(100, GREATEST(0, viewability * 100)) * 0.3 + (CASE WHEN cpa <= target_cpa * 0.8 THEN 100 WHEN cpa <= target_cpa THEN 80 WHEN cpa <= target_cpa * 1.2 THEN 60 WHEN cpa <= target_cpa * 1.5 THEN 40 ELSE 20 END * 0.4)) >= 75 THEN 'healthy'
            WHEN (LEAST(100, GREATEST(0, ctr * 5000)) * 0.3 + LEAST(100, GREATEST(0, viewability * 100)) * 0.3 + (CASE WHEN cpa <= target_cpa * 0.8 THEN 100 WHEN cpa <= target_cpa THEN 80 WHEN cpa <= target_cpa * 1.2 THEN 60 WHEN cpa <= target_cpa * 1.5 THEN 40 ELSE 20 END * 0.4)) >= 50 THEN 'needs_attention'
            ELSE 'critical'
        END
    )
$$;
```

2. Recreate REVOPS_AGENT with CALCULATE_CAMPAIGN_HEALTH as an additional tool.

3. Test with: "Calculate the campaign health for our top 5 campaigns by spend, assuming a target CPA of $25"

Execute all SQL."""

render_prompt("Prompt 4.3", "Agent with Custom Tool", PROMPT_4_3)

render_explanation("What this prompt does", """
Adds a **custom UDF tool** for domain-specific calculations. The Agent can now query data, search documents, AND run custom business logic.
""")


render_key_concepts([
    {"term": "Cortex Agent", "definition": "A Snowflake object that orchestrates LLMs, Analyst, Search, and custom tools to answer complex questions."},
    {"term": "Tool Routing", "definition": "The Agent selects the right tool for each question based on the question type and tool descriptions."},
    {"term": "Custom Tools", "definition": "SQL UDFs registered as Agent tools. Enable domain-specific calculations and business logic."},
])

render_what_you_built([
    "REVOPS_AGENT — Cortex Agent with Analyst + Search tools",
    "Tested structured, unstructured, and mixed queries",
    "CALCULATE_CAMPAIGN_HEALTH as a custom tool",
    "Enhanced agent with three tool types",
])
