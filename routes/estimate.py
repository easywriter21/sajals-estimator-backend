from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from services.ai_engine import generate_estimate

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/estimate/")
async def estimate(request: Request, text: str = Form(...)):
    result = generate_estimate(text)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "result": result
    })
