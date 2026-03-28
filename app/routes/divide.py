from fastapi import APIRouter

router = APIRouter()

@router.get("/divide")
def divide(num1: float, num2: float):

    if num2 == 0:
        return {
            "operation": "divide",
            "error": "No se puede dividir entre 0"
        }

    return {
        "operation": "divide",
        "result": num1 / num2
    }