from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/excel")

@router.post("/")
def export_excel(data: dict):

    boq = data.get("boq", [])

    df = pd.DataFrame(boq)

    file_name = "Sajals_Estimator_BOQ.xlsx"

    df.to_excel(file_name, index=False)

    return {
        "assistant": "Estimator",
        "message": "Excel generated",
        "file": file_name
    }
