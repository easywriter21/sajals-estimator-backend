from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/cad/upload")
async def upload_cad(file: UploadFile = File(...)):
    return {"message": "CAD file received", "filename": file.filename}
