from fastapi import APIRouter, UploadFile, File
import dxfgrabber, math

from utils.master_estimator import master_estimate

router = APIRouter()

@router.post("/cad/upload")
async def upload_cad(file: UploadFile = File(...)):

    path = f"temp_{file.filename}"

    with open(path, "wb") as f:
        f.write(file.file.read())

    drawing = dxfgrabber.readfile(path)

    length = 0

    for e in drawing.entities:
        if e.dxftype == "LINE":
            dx = e.end[0] - e.start[0]
            dy = e.end[1] - e.start[1]
            length += math.sqrt(dx*dx + dy*dy)

    area = int(length * 3)

    return master_estimate(f"{area} sq ft building")
