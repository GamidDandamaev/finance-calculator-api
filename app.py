import os

from fastapi import FastAPI


APP_NAME = os.getenv("APP_NAME", "Finance Calculator API")
APP_AUTHOR = os.getenv("APP_AUTHOR", "Gamid")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

app = FastAPI(title=APP_NAME)


@app.get("/")
def root():
    return {
        "message": f"{APP_NAME} is running",
        "author": APP_AUTHOR,
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": APP_VERSION}