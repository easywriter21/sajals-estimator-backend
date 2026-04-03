from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/pdf/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return {"message": "PDF received", "filename": file.filename}
