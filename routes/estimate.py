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
    text: str = Form(...),
    cement: float = Form(...),
    steel: float = Form(...),
    sand: float = Form(...),
    aggregate: float = Form(...),
    labour: float = Form(...)
):
    prices = {
        "cement": cement,
        "steel": steel,
        "sand": sand,
        "aggregate": aggregate,
        "labour": labour
    }

    result = master_estimate(text, prices)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "result": result
    })
