import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, "Cortex Search", "1:45 PM", "15 min", "Knowledge base, Cortex Search service, and RAG query pattern")

render_technologies_used([
    {"name": "Cortex Search Service", "description": "A managed hybrid search engine combining vector (semantic) and keyword search with automatic reranking. Created with a single SQL statement.", "icon": "search"},
    {"name": "RAG (Retrieval Augmented Generation)", "description": "A pattern that retrieves relevant documents first, then passes them as context to an LLM for grounded answer generation.", "icon": "hub"},
    {"name": "SEARCH_PREVIEW", "description": "SQL function to query a Cortex Search Service. Supports text queries, column selection, filtering, and result limits.", "icon": "preview"},
])


PROMPT_3_1 = """In ADTECH_AI.REVOPS:

1. First, create a unified text table for search called REVOPS_KNOWLEDGE_BASE that combines:
   - From OPTIMIZATION_GUIDES: doc_id, 'optimization_guide' as doc_type, content, category as metadata_category, priority as metadata_priority, NULL as doc_date
   - From INCIDENT_REPORTS: doc_id, 'incident_report' as doc_type, content, category as metadata_category, priority as metadata_priority, date as doc_date
   
   Include columns: doc_id, doc_type, content, metadata_category, metadata_priority, doc_date

2. Then create a Cortex Search Service:
   CREATE OR REPLACE CORTEX SEARCH SERVICE REVOPS_SEARCH
     ON content
     ATTRIBUTES metadata_category, metadata_priority, doc_type
     WAREHOUSE = ADTECH_WH
     TARGET_LAG = '1 hour'
     EMBEDDING_MODEL = 'snowflake-arctic-embed-l-v2.0'
     AS (
       SELECT doc_id, doc_type, content, metadata_category, metadata_priority, doc_date
       FROM REVOPS_KNOWLEDGE_BASE
     );

Execute all SQL. Then verify with SHOW CORTEX SEARCH SERVICES."""

render_prompt("Prompt 3.1", "Create Cortex Search Service", PROMPT_3_1)

render_explanation("What this prompt does", """
Builds a unified knowledge base from unstructured text sources and creates a hybrid search service.

The search service automatically embeds, indexes, and serves results with auto-refresh when source data changes.
""")


PROMPT_3_2 = """In ADTECH_AI.REVOPS, query our REVOPS_SEARCH service using SEARCH_PREVIEW:

1. Search for "how to improve viewability rates" (should find optimization guides)
2. Search for "budget overspend incident" with filter metadata_priority = 'critical' (should find incident reports)
3. Search for "CTV campaign best practices" (should find both guides and incident context)
4. Search for "client retention churn warning signals" (should find account health content)


Execute all searches and show results."""

render_prompt("Prompt 3.2", "Query the Search Service", PROMPT_3_2)

render_explanation("What this prompt does", """
Tests different search capabilities across the document corpus:

These searches test different retrieval capabilities:
1. **Semantic search** — finds conceptually relevant docs even without exact keyword match
2. **Filtered search** — combines text relevance with metadata filtering (priority level)
3. **Cross-document-type** — retrieves from both guides and incidents for a complete picture
4. **Business concept matching** — maps "churn" to retention-related content
""")


PROMPT_3_3 = """In ADTECH_AI.REVOPS, implement a RAG pattern:

1. Question: "What are the most common platform incidents that affect campaign delivery, what are their root causes, and what preventive measures have been implemented?"

2. Retrieve top 5 documents from REVOPS_SEARCH, then pass to SNOWFLAKE.CORTEX.COMPLETE() with instructions to answer ONLY from the provided documents, cite doc_ids, and structure the answer with: 1) Common incident types, 2) Root causes, 3) Effective measures, 4) Recommendations.

Use claude-sonnet-4-6 as the model. Execute and show the RAG response."""

render_prompt("Prompt 3.3", "RAG Pattern: Search + Generate", PROMPT_3_3)

render_explanation("What this prompt does", """
Implements the full **RAG** pattern: retrieve relevant documents, then generate a grounded answer with citations.
""")


render_key_concepts([
    {"term": "Cortex Search Service", "definition": "A managed hybrid search engine created with SQL. Handles embedding, indexing, reranking, and auto-refresh automatically."},
    {"term": "RAG", "definition": "Retrieval Augmented Generation: retrieve documents, include as context in LLM prompt, generate grounded answer."},
    {"term": "Hybrid Search", "definition": "Combining vector search (semantic similarity) with keyword search (exact matching). Better than either alone."},
])

render_what_you_built([
    "REVOPS_KNOWLEDGE_BASE — unified document table",
    "REVOPS_SEARCH — Cortex Search service with hybrid search",
    "Search queries across multiple document types",
    "Full RAG pipeline for grounded Q&A",
])
