class EnterpriseBaseException(Exception):
    def __init__(self, message: str, code: str = "INTERNAL_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)

class DatabaseConnectionException(EnterpriseBaseException):
    def __init__(self, message: str = "Database connection timed out"):
        super().__init__(message, code="DB_TIMEOUT_504")

class ServiceUnavailableException(EnterpriseBaseException):
    def __init__(self, service_name: str):
        super().__init__(f"Downstream service '{service_name}' unreachable", code="DOWNSTREAM_503")

class EntityNotFoundException(EnterpriseBaseException):
    def __init__(self, entity_name: str, entity_id: str):
        super().__init__(f"{entity_name} with ID {entity_id} not found", code="NOT_FOUND_404")
