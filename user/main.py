from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from user.delivery.api_v1.api import api_router as api_v1_router


app = FastAPI()


# ------------------ CORS ------------------- #
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------ Router ------------------- #
app.include_router(api_v1_router)


# ------------------ Default Path ------------------- #
@app.get("/")
async def root():
    return {"message": "user_api"}
