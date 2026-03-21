from fastapi import APIRouter
from fastapi.responses import FileResponse
import pandas as pd
from utils.cost_calculator import calculate_cost

router = APIRouter(prefix="/excel")

@router.post("/")
def export_excel(data: dict):

    result = calculate_cost(data)
    boq = result["boq"]

    df = pd.DataFrame(boq)

    file_name = "Sajals_Estimator_BOQ.xlsx"

    df.to_excel(file_name, index=False)

    # 🔥 IMPORTANT: RETURN FILE ONLY
    return FileResponse(
        path=file_name,
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename=file_name
    )
