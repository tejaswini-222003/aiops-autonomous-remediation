# Synthetic E-Commerce Microservices

A synthetic, multi-service backend environment designed for testing observability, incident response, and distributed debugging. 

This repository contains four interconnected Python microservices with **intentionally injected bugs**. It is accompanied by synthetic telemetry data (Splunk logs and ServiceNow incident exports) to simulate real-world production outages, cascading failures, and trace-level debugging scenarios.

## 🏗️ Repository Structure

```text
.
├── enterprise_core/                      # Shared internal libraries
│   └── database/
│       └── connection_pool.py            # DB connection manager (Bugs: Leaks, Config, Signature)
├── user_management_service/              # User profile & authentication API
│   └── repositories/
│       └── user_repository.py            # Database access layer (Bugs: Unhandled Index)
├── order_fulfillment_service/            # Checkout & order processing API
│   ├── services/
│   │   └── order_service.py              # Business logic (Bugs: Division by Zero)
│   └── clients/
│       └── payment_gateway_client.py     # 3rd-party integrations (Bugs: Unhandled Timeouts)
├── notification_service/                 # Asynchronous event consumer
│   └── consumers/
│       └── event_consumer.py             # Kafka/RabbitMQ consumer (Bugs: Null Pointer/AttributeError)
├── data/                                 # Synthetic observability & ticketing data
│   ├── servicenow_incidents.xlsx         # Incident tickets mapped to trace IDs
│   └── splunk_logs.json                  # Correlated application logs
├── requirements.txt                      # Global dependencies
└── README.md