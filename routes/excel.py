from fastapi import APIRouter
from fastapi.responses import FileResponse
from utils.cost_calculator import generate_excel

router = APIRouter()

@router.post("/excel/")
def excel():
    path = generate_excel()
    return FileResponse(path, filename="Sajals_Estimator_BOQ.xlsx")
