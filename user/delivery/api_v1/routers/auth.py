from common_schema.user import UserRoleType
from dto.user import UserDTO
from user.crud.auth import AuthenticationCrud
from user.delivery.api_v1.routers import auth
from fastapi import APIRouter, BackgroundTasks, Depends, Request

from user.delivery.deps import get_auth_crud


router = APIRouter(prefix="/auth", tags=["User Authentication"])


@router.get("/validate")
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


@router.post("/register")
def get_accounts(
    *,
    user: UserDTO,
    background_tasks: BackgroundTasks,
    crud: AuthenticationCrud = Depends(get_auth_crud),
):
    refresh_token = crud.register(user, background_tasks)
    return refresh_token


@router.get("/email-verify")
def get_accounts(
    *,
    token: str,
    crud: AuthenticationCrud = Depends(get_auth_crud),
):
    err = crud.verify_email_token(token)
    if err != None:
        err.raise_http_exception()

    return {"status": "email verified"}
