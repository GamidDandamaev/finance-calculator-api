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

@app.get("/loan-payment")
def loan_payment(
    principal: float,
    annual_rate: float,
    years: int,
):
    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    if monthly_rate == 0:
        payment = principal / months
    else:
        payment = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "monthly_payment": round(payment, 2),
    }


@app.get("/future-value")
def future_value(
    principal: float,
    annual_rate: float,
    years: int,
):
    value = principal * (1 + annual_rate / 100) ** years

    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "future_value": round(value, 2),
    }


@app.get("/present-value")
def present_value(
    future_value: float,
    annual_rate: float,
    years: int,
):
    value = future_value / (1 + annual_rate / 100) ** years

    return {
        "future_value": future_value,
        "annual_rate": annual_rate,
        "years": years,
        "present_value": round(value, 2),
    }