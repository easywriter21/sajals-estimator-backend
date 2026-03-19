from fastapi import APIRouter
import dxfgrabber
import math

router = APIRouter(prefix="/cad")

@router.post("/")
def read_cad(file_path: str):

    drawing = dxfgrabber.readfile(file_path)

    lines = []

    for entity in drawing.entities:

        if entity.dxftype == "LINE":

            dx = entity.end[0] - entity.start[0]
            dy = entity.end[1] - entity.start[1]

            length = math.sqrt(dx*dx + dy*dy)

            lines.append(length)

    return {
        "assistant": "Estimator",
        "detected_wall_lengths": lines
    }
