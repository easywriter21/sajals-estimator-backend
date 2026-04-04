from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from utils.master_estimator import master_estimate

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/estimate/")
async def estimate(
    request: Request,
    text: str = Form(""),
    budget: float = Form(None),
    duration: int = Form(None)
):
    result = master_estimate(text, budget, duration)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "result": result
    })
