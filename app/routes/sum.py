from fastapi import APIRouter

router = APIRouter()

@router.get("/sum")
def sum(num1: float, num2: float):
    return {"operation": "sum", "result": num1 + num2}