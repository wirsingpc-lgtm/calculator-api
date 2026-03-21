from fastapi.testclient import TestClient
from app.main import app

# Creamos el cliente de pruebas vinculado a tu aplicación FastAPI
client = TestClient(app)

def test_read_main():
    """Prueba que el endpoint raíz responda correctamente"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Calculadora"}

def test_sum():
    """Prueba la funcionalidad de suma con parámetros válidos"""
    response = client.get("/sum?num1=10&num2=5")
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "sum"
    assert data["num1"] == 10
    assert data["num2"] == 5
    assert data["result"] == 15

def test_subtract():
    """Prueba la funcionalidad de resta con parámetros válidos"""
    response = client.get("/subtract?num1=10&num2=5")
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "subtract"
    assert data["result"] == 5

def test_invalid_parameters():
    """Prueba que la API devuelva un error 422 si los datos no son números"""
    response = client.get("/sum?num1=abc&num2=5")
    assert response.status_code == 422
