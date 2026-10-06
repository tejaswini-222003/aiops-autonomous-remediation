from fastapi import FastAPI, HTTPException
from user_management_service.services.user_service import UserService
from enterprise_core.exceptions.custom_exceptions import EnterpriseBaseException

app = FastAPI(title="User Management API")
user_service = UserService()

@app.get("/api/v1/users/{user_id}")
def read_user(user_id: int):
    try:
        return user_service.get_profile(user_id)
    except EnterpriseBaseException as e:
        raise HTTPException(status_code=500, detail={"code": e.code, "message": e.message})
