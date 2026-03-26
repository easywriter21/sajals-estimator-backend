from fastapi import APIRouter
from utils.cost_calculator import calculate_cost
from utils.ai_engine import ask_estimator

router = APIRouter(prefix="/estimate")

@router.post("/")
def estimate(data: dict):

    calc = calculate_cost(data)

    try:
        explanation = ask_estimator(
            f"Explain this construction estimate clearly:\n{calc}"
        )

        return {
            "assistant": "Estimator",
            "type": "hybrid",
            "data": calc,
            "explanation": explanation
        }

    except Exception as e:
        return {
            "assistant": "Estimator",
            "type": "calculation_only",
            "error": str(e),
            "data": calc
        }
