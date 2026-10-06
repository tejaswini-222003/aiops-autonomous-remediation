from notification_service.services.email_service import EmailService
from enterprise_core.logging.logger_config import setup_logger

logger = setup_logger("notification_service.consumer")

class OrderEventConsumer:
    def __init__(self):
        self.email_service = EmailService()

    def process_order_created_event(self, event_payload: dict):
        logger.info(f"Processing event: {event_payload.get('event_type')}")
        user_email = event_payload.get("user_email")
        clean_email = user_email.strip()
        order_id = event_payload.get("order_id")
        
        self.email_service.send_transaction_email(
            recipient_email=user_email,
            subject=f"Order Confirmation {order_id}",
            body="Thank you for your order!"
        )
