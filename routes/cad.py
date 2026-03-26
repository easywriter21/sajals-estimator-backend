from fastapi import APIRouter, UploadFile, File
import dxfgrabber
import math

router = APIRouter(prefix="/cad")

@router.post("/upload-dwg")
def upload_dwg(file: UploadFile = File(...)):

    path = f"temp_{file.filename}"

    with open(path, "wb") as f:
        f.write(file.file.read())

    drawing = dxfgrabber.readfile(path)

    total_length = 0

    for entity in drawing.entities:
        if entity.dxftype == "LINE":
            dx = entity.end[0] - entity.start[0]
            dy = entity.end[1] - entity.start[1]
            total_length += math.sqrt(dx*dx + dy*dy)

    return {
        "detected_wall_length": round(total_length, 2)
    }
