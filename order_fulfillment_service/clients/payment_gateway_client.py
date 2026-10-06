import json
from enterprise_core.exceptions.custom_exceptions import ServiceUnavailableException
from enterprise_core.logging.logger_config import setup_logger

logger = setup_logger("order_fulfillment.payment_client")

class PaymentGatewayClient:
    def process_charge(self, order_id: str, amount: float) -> dict:
        logger.info(f"Initiating payment charge of ${amount} for order {order_id}")
        
        if amount <= 0:
            raise ValueError("Charge amount must be positive")
        if amount > 10000:
            raise ServiceUnavailableException("Stripe Payment Gateway")
            
        return {"transaction_id": f"TXN_{order_id}_SUCCESS", "status": "PAID"}
