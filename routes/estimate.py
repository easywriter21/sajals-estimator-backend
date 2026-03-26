from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from utils.cost_calculator import calculate_cost
from utils.ai_engine import ask_estimator

router = APIRouter(prefix="/estimate")

# Templates for frontend UI
templates = Jinja2Templates(directory="templates")


# 🔹 1. API ROUTE (JSON response)
@router.post("/")
def estimate_api(data: dict):

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


# 🔹 2. UI ROUTE (HTML page response)
@router.post("/estimate-ui/")
def estimate_ui(
    request: Request,
    text: str = Form(""),
    builtUpArea: float = Form(1200),
    floors: int = Form(2),
    budget: float = Form(None),
    duration: float = Form(None)
):

    data = {
        "text": text,
        "builtUpArea": builtUpArea,
        "floors": floors,
        "budget": budget,
        "duration": duration
    }

    calc = calculate_cost(data)

    try:
        explanation = ask_estimator(
            f"Explain this construction estimate clearly:\n{calc}"
        )
    except Exception:
        explanation = "AI explanation not available"

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "data": calc,
            "explanation": explanation
        }
        )
