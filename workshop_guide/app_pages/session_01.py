import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(1, "Data Prep", "1:10 PM", "15 min", "Database, schema, warehouse, and 9 operational tables loaded from CSV")

render_technologies_used([
    {"name": "Database & Schema", "description": "Snowflake's organizational hierarchy for objects. A database contains schemas, and schemas contain tables, views, and other objects.", "icon": "database"},
    {"name": "CSV File Format", "description": "Snowflake can infer schema and load data directly from CSV files using file formats and COPY INTO commands.", "icon": "table_chart"},
    {"name": "Virtual Warehouse", "description": "Snowflake's compute engine. A warehouse provides the CPU and memory to execute queries and load data.", "icon": "memory"},
])


PROMPT_1_1 = """Create the following Snowflake objects for our StackAdapt RevOps AI workshop:

1. A database called ADTECH_AI
2. A schema called REVOPS inside that database
3. A stage called DATA in the schema REVOPS with a directory table and server side encryption
3. A warehouse called ADTECH_WH (size MEDIUM, auto-suspend after 60 seconds, auto-resume enabled)
4. Set the session context to use these objects

Execute all SQL and confirm each object was created."""

render_prompt("Prompt 1.1", "Create Database, Schema & Warehouse", PROMPT_1_1)

render_explanation("What this prompt does", """
Creates the foundational Snowflake objects:

```sql
CREATE DATABASE ADTECH_AI;
CREATE SCHEMA ADTECH_AI.REVOPS;
CREATE WAREHOUSE ADTECH_WH
  WAREHOUSE_SIZE = 'MEDIUM'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

USE DATABASE ADTECH_AI;
USE SCHEMA REVOPS;
USE WAREHOUSE ADTECH_WH;
```
""")


PROMPT_1_2 = """In ADTECH_AI.REVOPS, the 9 CSV files have been uploaded to an internal stage called DATA.

For all 9 tables (ADVERTISERS, CAMPAIGNS, CAMPAIGN_PERFORMANCE, AUDIENCE_SEGMENTS, REVENUE_MONTHLY, CLIENT_HEALTH, SALES_PIPELINE, OPTIMIZATION_GUIDES, INCIDENT_REPORTS):

1. Create a file format (CSV with PARSE_HEADER=TRUE, FIELD_OPTIONALLY_ENCLOSED_BY='"')
2. Create the tables with appropriate column types inferred from the data. Ensure to convert the column names to uppercase.
3. Load the data

Use CREATE TABLE with INFER_SCHEMA from a stage and then COPY INTO them. The key requirement is that all 9 tables are created and populated.

Execute all SQL."""

st.markdown("""
**Before running the prompt below, download the CSV files and upload them to the `DATA` stage:**

1. Download the zip file containing all CSVs: [stackadapt_revops_data.zip](https://github.com/sfc-gh-ablandet/coco-hol-toronto-stackadapt/raw/main/workshop_guide/data/stackadapt_revops_data.zip)
2. Unzip the file on your computer to get the individual CSV files.
3. Using Snowsight, use the Horizon Catalog to browse to the `ADTECH_AI.REVOPS.DATA` stage and upload all CSV files.
4. Then copy the prompt below into Cortex Code and execute.
""")

render_prompt("Prompt 1.2", "Load and Create Tables from CSV", PROMPT_1_2)

render_explanation("What this prompt does", """
Loads all operational data tables from CSV files uploaded to the internal stage `DATA`:

```sql
CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = CSV
  PARSE_HEADER = TRUE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"';

CREATE OR REPLACE TABLE CAMPAIGNS
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    FROM TABLE(INFER_SCHEMA(
      LOCATION => '@ADTECH_AI.REVOPS.DATA/campaigns.csv',
      FILE_FORMAT => 'csv_format'
    ))
  );

COPY INTO CAMPAIGNS
  FROM @ADTECH_AI.REVOPS.DATA/campaigns.csv
  FILE_FORMAT = csv_format;
```

**The tables**:
- **ADVERTISERS** (30 rows) — Advertiser accounts with tier, industry, region, and monthly commitment
- **CAMPAIGNS** (120 rows) — Ad campaigns with objective, channel, status, and daily budget
- **CAMPAIGN_PERFORMANCE** (900 rows) — Daily metrics: impressions, clicks, conversions, spend, revenue, viewability
- **AUDIENCE_SEGMENTS** (25 rows) — Targeting segments with category, reach, and CPM
- **REVENUE_MONTHLY** (180 rows) — Monthly revenue by advertiser: media spend, platform fee, take rate
- **CLIENT_HEALTH** (180 rows) — Monthly health scores: engagement, performance, retention risk, NPS
- **SALES_PIPELINE** (40 rows) — Sales opportunities with stage, amount, and probability
- **OPTIMIZATION_GUIDES** (20 rows) — Best practices and playbooks for campaign optimization
- **INCIDENT_REPORTS** (15 rows) — Platform incident reports with root cause and resolution
""")


PROMPT_1_3 = """Run a query in ADTECH_AI.REVOPS that shows every table name and its row count, ordered by row count descending. Format it nicely."""

render_prompt("Prompt 1.3", "Verify All Data Tables", PROMPT_1_3)

render_explanation("What this prompt does", """
A quick verification query. You should see approximately **1,510 total rows** across 9 tables.
""")


render_key_concepts([
    {"term": "Internal Stage", "definition": "A named Snowflake stage that stores files within Snowflake's managed storage. Files are uploaded via Snowsight UI or PUT command."},
    {"term": "INFER_SCHEMA", "definition": "A Snowflake table function that automatically detects column names and types from files in a stage."},
    {"term": "File Format", "definition": "A named object specifying how to parse files (CSV delimiters, headers, quoting). Created once and reused across multiple COPY INTO operations."},
])

render_what_you_built([
    "ADTECH_AI database and REVOPS schema",
    "ADTECH_WH warehouse (Medium, auto-suspend 60s)",
    "9 operational data tables loaded from CSV (~1,510 total rows)",
])
