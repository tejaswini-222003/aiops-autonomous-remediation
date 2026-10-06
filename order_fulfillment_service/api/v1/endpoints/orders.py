from fastapi import FastAPI, HTTPException
from order_fulfillment_service.services.order_service import OrderService
from enterprise_core.exceptions.custom_exceptions import EnterpriseBaseException

app = FastAPI(title="Order Fulfillment API")
order_service = OrderService()

@app.post("/api/v1/orders")
def submit_order(user_id: int, amount: float):
    try:
        return order_service.create_order(user_id=user_id, items=["item1"], total_amount=amount)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
