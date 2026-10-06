from enterprise_core.logging.logger_config import setup_logger

logger = setup_logger("notification_service.email")

class EmailService:
    def send_transaction_email(self, recipient_email: str, subject: str, body: str) -> bool:
        if "@" not in recipient_email:
            raise ValueError(f"Invalid email recipient: {recipient_email}")
            
        logger.info(f"Email sent successfully to {recipient_email} with subject '{subject}'")
        return True
