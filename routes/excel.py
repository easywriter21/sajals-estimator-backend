from fastapi import APIRouter
from fastapi.responses import FileResponse
from services.cost_calculator import generate_excel

router = APIRouter()


@router.post("/excel/")
def excel():
    file_path = generate_excel()
    return FileResponse(file_path, filename="Estimate.xlsx")
