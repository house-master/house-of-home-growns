from common_schema.user import UserRoleType
from user.crud.auth import AuthenticationCrud
from user.delivery.api_v1.routers import auth
from fastapi import APIRouter, Depends, Request

from user.delivery.deps import get_auth_crud


router = APIRouter(prefix="/auth", tags=["accounts"])


@router.get("/verify")
def get_accounts(
    *,
    request: Request,
    crud: AuthenticationCrud = Depends(get_auth_crud),
):
    user = crud.validate_access_token(request)
    return user


@router.post("/login")
def get_accounts(
    *,
    email: str,
    password: str,
    role: UserRoleType,
    crud: AuthenticationCrud = Depends(get_auth_crud),
):
    refresh_token = crud.login(email, password, role)
    return refresh_token


@router.get("/logout")
def get_accounts(
    *,
    request: Request,
    crud: AuthenticationCrud = Depends(get_auth_crud),
):
    status = crud.logout(request)
    return {"status": status}


@router.get("/refresh")
def get_accounts(
    *,
    request: Request,
    crud: AuthenticationCrud = Depends(get_auth_crud),
):
    access_token = crud.generate_access_token(request)
    return access_token
