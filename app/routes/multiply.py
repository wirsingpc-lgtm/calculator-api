from fastapi import APIRouter

router = APIRouter()

@router.get("/multiply")
def multiply(num1: float, num2: float):
    return {"operation": "multiply", "result": num1 * num2}