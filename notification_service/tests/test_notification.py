import pytest
from notification_service.services.email_service import EmailService

def test_send_email_success():
    service = EmailService()
    assert service.send_transaction_email("user@domain.com", "Test", "Hello") is True

def test_send_email_invalid_address():
    service = EmailService()
    with pytest.raises(ValueError):
        service.send_transaction_email("invalid_email_string", "Test", "Hello")
