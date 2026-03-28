from fastapi import APIRouter

router = APIRouter()

@router.get("/subtract")
def subtract(num1: float, num2: float):
    return {"operation": "subtract", "result": num1 - num2}