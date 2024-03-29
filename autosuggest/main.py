from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware


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


# ------------------ Default Path ------------------- #
@app.get("/")
async def root():
    return {"message": "autosuggest_api"}
