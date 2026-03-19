from fastapi import APIRouter
from utils.cost_calculator import calculate_cost

router = APIRouter(prefix="/estimate")

@router.post("/")
def estimate(data: dict):

    result = calculate_cost(data)

    return {
        "assistant": "Estimator",
        "project": "Sajal's Estimator",
        "estimation": result
    }
