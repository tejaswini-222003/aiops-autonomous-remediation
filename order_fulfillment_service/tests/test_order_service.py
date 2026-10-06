import pytest
from order_fulfillment_service.services.order_service import OrderService
from enterprise_core.exceptions.custom_exceptions import ServiceUnavailableException

def test_create_order_success():
    service = OrderService()
    res = service.create_order(user_id=10, items=["item_a"], total_amount=150.0)
    assert res["status"] == "CREATED"

def test_create_order_gateway_failure():
    service = OrderService()
    with pytest.raises(ServiceUnavailableException):
        service.create_order(user_id=10, items=["item_a"], total_amount=15000.0)
