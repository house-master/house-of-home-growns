from fastapi import APIRouter
from user.delivery.api_v1.routers import auth
from user.model.setting import settings


api_router = APIRouter(prefix=settings.API_V1_STR)

api_router.include_router(auth.router)
