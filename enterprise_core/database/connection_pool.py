import json
import logging
import time
from enterprise_core.exceptions.custom_exceptions import DatabaseConnectionException

logger = logging.getLogger("enterprise_core.database")

class DatabasePoolManager:
    def __init__(self, config_file: str = "config/app_settings.json"):
        with open(config_file, "r") as f:
            self.config = json.load(f)["database"]
        self.host = self.config["host"]
        self.pool_size = self.config["pool_size"]
        self.read_timeout = self.config["read_timeout"]
        self.active_connections = 0

    def get_connection(self):
        if self.active_connections >= self.pool_size:
            logger.error(json.dumps({
                "event": "connection_pool_exhausted",
                "active_connections": self.active_connections,
                "pool_size": self.pool_size
            }))
            raise DatabaseConnectionException("Connection pool limit reached")
            
        self.active_connections += 1
        return f"Conn-{self.active_connections}@{self.host}"

    def release_connection(self, conn_id: str):
        if self.active_connections > 0:
            self.active_connections -= 1

    def execute_query(self, tenant_id: str, sql: str, params: tuple = ()):
        conn = self.get_connection()
        try:
            logger.info(json.dumps({"event": "executing_sql", "tenant": tenant_id, "sql": sql, "conn": conn}))
            if "FAIL_DB" in sql:
                raise DatabaseConnectionException("Fatal deadlock detected in transaction")
            return [{"id": 1, "status": "processed"}]
        finally:
            self.release_connection(conn)
