# aiops-autonomous-remediation
AI powered Autonomous Remediation



ITSM_updated_workflow_V2/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── README.md
│
├── app/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   │
│   ├── graph/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── nodes.py
│   │   ├── nodes.py.bak
│   │   ├── nodes.py.bak2
│   │   ├── state.py
│   │   ├── state.py.bak
│   │   ├── state.py.bak2
│   │   └── workflow.py
│   │
│   ├── ingestion/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── incident_ingestion.py
│   │   ├── python_parser.py
│   │   ├── repository_ingestion.py
│   │   └── startup_ingestion.py
│   │
│   └── services/
│       ├── __pycache__/
│       ├── __init__.py
│       ├── ai_service.py
│       ├── code_service.py
│       ├── cyber_validation_service.py
│       ├── graph_schema_registry.py
│       ├── incident_service.py
│       ├── incident_service.py.bak
│       ├── incident_service.py.bak2
│       ├── neo4j_service.py
│       ├── postgres_service.py
│       ├── qdrant_service.py
│       └── ranker_service.py
│
├── config/
│   └── application_repository_map.json
│
├── data/
│   └── incidents/
│       ├── incidents_2026-10-01.xlsx
│       └── splunk_logs.json
│
├── frontend/
│   ├── __pycache__/
│   ├── __init__.py
│   └── Streamlit_app.py
│
├── qdrant_db/
│   ├── collection/
│   ├── .lock
│   └── meta.json
│
├── repository_workspace/
│   ├── enterprise_core/
│   ├── notification_service/
│   ├── order_fulfillment_service/
│   ├── user_management_service/
│   └── README.md
│
├── shared_workspace/
│   └── config/
│       └── app_settings.json
│
├── sql/
│   └── schema.sql
│
├── src/
│   └── aiops/
│       └── __init__.py
│
├── add_graph_followup_context_v2.py
├── add_graph_followup_context.py
├── add_graph_query_diagnostics.py
├── audit_all_repository_calls.py
├── checkpoint.py
├── setup_postgres.py
└── test1234/

