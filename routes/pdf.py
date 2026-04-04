from fastapi import APIRouter, UploadFile, File
import pdfplumber

from utils.master_estimator import master_estimate

router = APIRouter()

@router.post("/pdf/upload")
async def upload_pdf(file: UploadFile = File(...)):

    path = f"temp_{file.filename}"

    with open(path, "wb") as f:
        f.write(file.file.read())

    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    result = master_estimate(text)

    return result
