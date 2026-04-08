from fastapi import APIRouter, Form, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from utils.master_estimator import master_estimate
from utils.pdf_parser import extract_data_from_pdf
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@router.post("/estimate/")
async def estimate(
    request: Request,
    area: float = Form(None),
    floors: int = Form(None),
    budget: float = Form(None),
    time_limit: int = Form(None),
    pdf: UploadFile = File(None)
):

    if pdf:
        content = await pdf.read()
        extracted_area, extracted_floors = extract_data_from_pdf(content)

        if extracted_area:
            area = extracted_area
        if extracted_floors:
            floors = extracted_floors

    if not area or not floors:
        return templates.TemplateResponse("result.html", {
            "request": request,
            "result": {"Error": "Area or Floors not found"}
        })

    result = master_estimate(area, floors, budget, time_limit)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "result": result
    })
