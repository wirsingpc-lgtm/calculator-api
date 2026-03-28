from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Calculadora"}

def test_sum():
    response = client.get("/sum?num1=2&num2=3")
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_subtract():
    response = client.get("/subtract?num1=10&num2=4")
    assert response.status_code == 200
    assert response.json()["result"] == 6

def test_multiply():
    response = client.get("/multiply?num1=3&num2=5")
    assert response.status_code == 200
    assert response.json()["result"] == 15

def test_divide():
    response = client.get("/divide?num1=10&num2=2")
    assert response.status_code == 200
    assert response.json()["result"] == 5