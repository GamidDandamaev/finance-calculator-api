from fastapi.testclient import TestClient

from app_final import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_future_value():
    response = client.get(
        "/future-value",
        params={
            "principal": 100000,
            "annual_rate": 10,
            "years": 3,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["principal"] == 100000
    assert data["annual_rate"] == 10
    assert data["years"] == 3
    assert data["future_value"] == 133100.0


def test_loan_payment():
    response = client.get(
        "/loan-payment",
        params={
            "principal": 1000000,
            "annual_rate": 12,
            "years": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["monthly_payment"] == 22244.45


def test_future_value_missing_parameter():
    response = client.get(
        "/future-value",
        params={
            "principal": 100000,
            "annual_rate": 10,
        },
    )

    assert response.status_code == 422