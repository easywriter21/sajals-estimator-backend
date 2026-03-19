from fastapi import APIRouter
from utils.ai_engine import ask_estimator
from utils.cost_calculator import calculate_cost

router = APIRouter(prefix="/estimate")

@router.post("/")
def estimate(data: dict):

    user_text = data.get("text", "")

    try:
        # AI estimation
        ai_response = ask_estimator(user_text)

        return {
            "assistant": "Estimator",
            "type": "AI",
            "response": ai_response
        }

    except Exception as e:
        # fallback calculation if AI fails
        fallback = calculate_cost(data)

        return {
            "assistant": "Estimator",
            "type": "fallback",
            "error": str(e),
            "result": fallback
        }
