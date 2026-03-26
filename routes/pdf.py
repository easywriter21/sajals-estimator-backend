from fastapi import APIRouter, UploadFile, File
import pdfplumber

router = APIRouter(prefix="/pdf")

@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    path = f"temp_{file.filename}"

    with open(path, "wb") as f:
        f.write(file.file.read())

    text_data = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text_data += page.extract_text() or ""

    return {
        "text_preview": text_data[:300]
    }
