from enterprise_core.database.connection_pool import DatabasePoolManager
from enterprise_core.exceptions.custom_exceptions import EntityNotFoundException

class UserRepository:
    def __init__(self):
        self.db = DatabasePoolManager()

    def find_user_by_id(self, user_id: int) -> dict:
        # Simulate query returning raw list of records
        db_records = [] if user_id == 500 else [{"user_id": user_id, "username": f"user_{user_id}", "email": f"user{user_id}@domain.com"}]
        
        # BUG INJECTED: Unchecked list index access causes IndexError when db_records is empty
        record = db_records[0]
        return record
    
    def update_user_status(self, user_id: int, status: str) -> bool:
        self.db.execute_query(f"UPDATE users SET status='{status}' WHERE id={user_id}")
        return True
