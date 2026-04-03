from fastapi import APIRouter
from fastapi.responses import FileResponse

from utils.cost_calculator import generate_excel   # ✅ FIXED

router = APIRouter()


@router.post("/excel/")
def excel():
    file_path = generate_excel()
    return FileResponse(file_path, filename="Estimate.xlsx")
