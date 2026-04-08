from fastapi import APIRouter
from fastapi.responses import FileResponse
from openpyxl import Workbook

router = APIRouter()

@router.post("/download-excel/")
def download_excel():

    wb = Workbook()
    ws = wb.active
    ws.title = "BOQ"

    ws.append(["Item", "Value"])
    ws.append(["Generated", "Estimator Result"])

    file_path = "estimate.xlsx"
    wb.save(file_path)

    return FileResponse(file_path, filename="estimate.xlsx")
