import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(2, "Cortex Analyst & Semantic Views", "1:25 PM", "20 min", "Semantic view with relationships, metrics, and natural language queries")

render_technologies_used([
    {"name": "Cortex Analyst", "description": "Snowflake's text-to-SQL engine that converts natural language questions into SQL queries using a semantic view to understand your data's business meaning.", "icon": "chat"},
    {"name": "Semantic View", "description": "A first-class Snowflake object (CREATE SEMANTIC VIEW) that describes your data in business terms: tables, relationships, facts, dimensions, metrics, and synonyms.", "icon": "description"},
    {"name": "AI_SQL_GENERATION", "description": "Custom instructions embedded in the semantic view that guide how Cortex Analyst generates SQL — providing domain context and disambiguation hints.", "icon": "auto_fix_high"},
])


PROMPT_2_1 = """/semantic_studio In ADTECH_AI.REVOPS, create a semantic view called REVOPS_ANALYTICS_VIEW for use with Cortex Analyst. It should cover these tables: ADVERTISERS, CAMPAIGNS, CAMPAIGN_PERFORMANCE, REVENUE_MONTHLY, CLIENT_HEALTH, SALES_PIPELINE.

Include:
- Relationships between the tables following these rules:
  - Do NOT specify join_type — omit it entirely (the proto enum doesn't accept string values like many_to_one)
  - Convention: left_table = fact/many side, right_table = dimension/one side (put the table with many rows as left_table)
  - Define primary_key.columns on dimension tables (ADVERTISERS, AUDIENCE_SEGMENTS) so the engine knows the "one" side
  - Use this template for each relationship:
    relationships:
      - name: <descriptive_name>
        left_table: <FACT_TABLE>
        right_table: <DIMENSION_TABLE>
        relationship_columns:
          - left_column: <FK_COLUMN>
            right_column: <PK_COLUMN>
  - Relationships needed: - CAMPAIGNS → ADVERTISERS on advertiser_id
  - CAMPAIGN_PERFORMANCE → CAMPAIGNS on campaign_id
  - REVENUE_MONTHLY → ADVERTISERS on advertiser_id
  - CLIENT_HEALTH → ADVERTISERS on advertiser_id
  - SALES_PIPELINE → ADVERTISERS on advertiser_id
- Facts for key numeric columns: impressions, clicks, conversions, spend, revenue, viewability_rate, media_spend, platform_fee, take_rate_pct, net_revenue, engagement_score, performance_score, deal amount, probability
- Dimensions for categorical columns: advertiser name, industry, tier, region, account_manager, campaign name, objective, channel, status, retention_risk, pipeline stage
- Add useful SYNONYMS ("CTR" for click-through rate (clicks/impressions), "CPA" for cost per acquisition (spend/conversions), "ROAS" for return on ad spend (revenue/spend), "client" or "customer" for advertiser, "take rate" for platform_fee/media_spend)
- Metrics: - CTR = clicks / impressions (click-through rate)
  - CPA = spend / conversions (cost per acquisition)
  - ROAS = revenue / spend (return on ad spend)
  - eCPM = (spend / impressions) * 1000 (effective cost per thousand impressions)
  - Platform Take Rate = platform_fee / media_spend
- An AI_SQL_GENERATION instruction with domain context: This is a programmatic advertising (AdTech) RevOps dataset for StackAdapt, a demand-side platform (DSP). 'Spend' refers to advertiser media spend flowing through the platform. 'Revenue' or 'net_revenue' is StackAdapt's platform fee (take-rate on media spend). Campaigns have objectives (awareness/consideration/conversion) and run across channels (display/native/video/CTV). Client health combines engagement, performance, and retention risk. When asked about 'revenue' without qualification, assume platform revenue (net_revenue). When asked about 'performance', consider both campaign metrics (CTR, CPA, ROAS) and client health scores.

Execute the SQL and confirm with DESCRIBE SEMANTIC VIEW."""

render_prompt("Prompt 2.1", "Create the Semantic View", PROMPT_2_1)

render_explanation("What this prompt does", """
Creates a **semantic view** — a first-class Snowflake object that enables natural language to SQL.

The semantic view encodes AdTech RevOps domain knowledge:

- **Relationships**: Campaigns belong to Advertisers. Daily performance metrics link to campaigns. Revenue and health scores track at the advertiser-month level. The pipeline shows future revenue opportunities.
- **Facts vs Dimensions**: Numeric measures (impressions, spend, revenue) are facts. Categorical attributes (industry, channel, tier) are dimensions that enable grouping and filtering.
- **Metrics**: Pre-calculated KPIs like CTR, CPA, and ROAS that Cortex Analyst can compute on-the-fly from raw facts.
- **AI Instructions**: Domain context so the engine knows that "revenue" means platform fees, "clients" means advertisers, and "performance" spans both campaign metrics and health scores.
""")


PROMPT_2_2 = """Ask Cortex Analyst these questions using ADTECH_AI.REVOPS.REVOPS_ANALYTICS_VIEW:

1. "What is our total platform revenue by advertiser tier for the last 3 months?"
2. "Which campaigns have the best ROAS (revenue/spend) and what channels are they on?"
3. "Show me advertisers with high retention risk — what's their average engagement score?"
4. "What's the average CTR by campaign objective and channel?"


Show the generated SQL and results for each."""

render_prompt("Prompt 2.2", "Test with Natural Language Queries", PROMPT_2_2)

st.info("""
:material/lightbulb: **You can also test these in the Cortex Analyst UI!**

In Snowsight, navigate to **AI & ML → Cortex Analyst** in the left sidebar. Select your `REVOPS_ANALYTICS_VIEW` semantic view, and you'll see a playground where you can type natural language questions interactively.
""")

render_explanation("What this prompt does", """
Tests Cortex Analyst across different question types to validate the semantic view definitions.

These test different semantic view capabilities:
1. **Aggregation with dimension grouping** — tests the revenue metrics and tier dimension
2. **Calculated metrics across tables** — tests ROAS computation and cross-table joins (performance → campaigns)
3. **Filtering with health data** — tests client health table joins and conditional filtering
4. **Multi-dimensional breakdown** — tests objective × channel cross-tabulation
""")


PROMPT_2_3 = """Now expand our REVOPS_ANALYTICS_VIEW in ADTECH_AI.REVOPS:

Add these calculated metrics to the semantic view:

1. **weighted_ctr** — A metric that calculates CTR weighted by impressions (to avoid small-sample bias): SUM(clicks) / SUM(impressions)
2. **revenue_at_risk** — Join revenue with client health to show net_revenue for advertisers where retention_risk = 'high'
3. **pipeline_weighted_value** — amount * probability / 100 for the sales pipeline

Also add these synonyms:
- "high risk clients" → retention_risk = 'high'
- "top tier" → tier = 'Gold'
- "programmatic spend" → media_spend

Then test with: "What is our total revenue at risk from high-retention-risk clients?"


Execute all SQL."""

render_prompt("Prompt 2.3", "Expand the Semantic View", PROMPT_2_3)

render_explanation("What this prompt does", """
Demonstrates iterative semantic view development — adding calculated metrics.

This expansion demonstrates iterative development of semantic views:

- **Weighted metrics** prevent misleading averages from small-sample campaigns
- **Cross-table metrics** combine data from multiple tables (revenue + health) into actionable KPIs
- **Business synonyms** map natural language to specific filter conditions, making the system more intuitive for RevOps users
""")


render_key_concepts([
    {"term": "Cortex Analyst", "definition": "Snowflake's text-to-SQL engine. Converts natural language to SQL using a semantic view for context."},
    {"term": "Semantic View", "definition": "A first-class Snowflake object mapping tables to business concepts. Contains relationships, facts, dimensions, metrics, synonyms, and AI instructions."},
    {"term": "AI_SQL_GENERATION", "definition": "Custom instructions guiding SQL generation. Essential for domain-specific terminology."},
])

render_what_you_built([
    "REVOPS_ANALYTICS_VIEW semantic view with domain-specific metrics",
    "Natural language queries validated against the view",
    "Expanded view with calculated metrics",
])
