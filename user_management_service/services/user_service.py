from user_management_service.repositories.user_repository import UserRepository
from enterprise_core.logging.logger_config import setup_logger

logger = setup_logger("user_management_service.user_service")

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_profile(self, user_id: int) -> dict:
        logger.info(f"Fetching profile for user_id={user_id}")
        return self.user_repo.find_user_by_id(user_id)

    def deactivate_user(self, user_id: int) -> bool:
        logger.info(f"Deactivating user_id={user_id}")
        return self.user_repo.update_user_status(user_id, "INACTIVE")
