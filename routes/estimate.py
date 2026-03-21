from fastapi import APIRouter
from utils.ai_engine import ask_estimator
from utils.cost_calculator import calculate_cost

router = APIRouter(prefix="/estimate")

@router.post("/")
def estimate(data: dict):

    # 🔹 Step 1: Accurate calculation (MAIN LOGIC)
    calculation = calculate_cost(data)

    # 🔹 Step 2: AI explanation (secondary)
    try:
        explanation = ask_estimator(
            f"""
Explain this construction estimate clearly for a civil engineering student:

{calculation}
"""
        )

        return {
            "assistant": "Estimator",
            "type": "hybrid",
            "data": calculation,
            "ai_explanation": explanation
        }

    except Exception as e:
        # If AI fails, still return correct calculation
        return {
            "assistant": "Estimator",
            "type": "calculation_only",
            "error": str(e),
            "data": calculation
        }
