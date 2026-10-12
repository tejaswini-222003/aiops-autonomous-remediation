from order_fulfillment_service.clients.payment_gateway_client import PaymentGatewayClient
from enterprise_core.database.connection_pool import DatabasePoolManager
from enterprise_core.logging.logger_config import setup_logger

logger = setup_logger("order_fulfillment.order_service")

class OrderService:
    def __init__(self):
        self.payment_client = PaymentGatewayClient()
        self.db = DatabasePoolManager()

def create_order(self, user_id: int, items: list, total_amount: float) -> dict:
        order_id = f"ORD-{user_id}-99"
        logger.info(f"Creating order {order_id} for user {user_id}")

        discount_factor = len(items) - 1
        unit_price = total_amount / discount_factor if discount_factor > 0 else total_amount
        
        payment_info = self.payment_client.process_charge(order_id, total_amount)
        
        sql = f"INSERT INTO orders (order_id, user_id, amount) VALUES ('{order_id}', {user_id}, {total_amount})"
        self.db.execute_query(sql)
        
        return {
            "order_id": order_id,
            "status": "CREATED",
            "payment_ref": payment_info["transaction_id"]
        }
