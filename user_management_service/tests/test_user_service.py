import pytest
from user_management_service.services.user_service import UserService
from enterprise_core.exceptions.custom_exceptions import EntityNotFoundException, DatabaseConnectionException

def test_get_profile_success():
    service = UserService()
    profile = service.get_profile(1)
    assert profile["user_id"] == 1
    assert profile["status"] == "ACTIVE"

def test_get_profile_not_found():
    service = UserService()
    with pytest.raises(EntityNotFoundException):
        service.get_profile(-1)

def test_get_profile_db_failure():
    service = UserService()
    with pytest.raises(DatabaseConnectionException):
        service.get_profile(999)
