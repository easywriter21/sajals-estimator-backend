from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from utils.master_estimator import master_estimate
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@router.post("/estimate/")
async def estimate(
    request: Request,
    area: float = Form(...),
    floors: int = Form(...),

    cement: float = Form(None),
    steel: float = Form(None),
    sand: float = Form(None),
    aggregate: float = Form(None),
    labour: float = Form(None),

    budget: float = Form(None),
    time_limit: int = Form(None)
):

    # Default Indian rates
    default_rates = {
        "cement": 350,
        "steel": 65,
        "sand": 900,
        "aggregate": 700,
        "labour": 400
    }

    # Use user input or default
    rates = {
        "cement": cement if cement else default_rates["cement"],
        "steel": steel if steel else default_rates["steel"],
        "sand": sand if sand else default_rates["sand"],
        "aggregate": aggregate if aggregate else default_rates["aggregate"],
        "labour": labour if labour else default_rates["labour"]
    }

    result = master_estimate(area, floors, rates, budget, time_limit)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,   # ✅ FIXED
            "result": result      # ✅ FIXED
        }
    )
