from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from utils.master_estimator import master_estimate

router = APIRouter()


@router.post("/estimate/", response_class=HTMLResponse)
async def estimate(
    text: str = Form(...),
    cement: float = Form(...),
    steel: float = Form(...),
    sand: float = Form(...),
    aggregate: float = Form(...),
    labour: float = Form(...)
):
    try:
        prices = {
            "cement": cement,
            "steel": steel,
            "sand": sand,
            "aggregate": aggregate,
            "labour": labour
        }

        result = master_estimate(text, prices)

        return f"""
        <html>
        <body style="font-family: Arial; text-align:center;">
            <h2>Estimation Result</h2>
            <pre>{result}</pre>
            <br>
            <a href="/">⬅ Back</a>
        </body>
        </html>
        """

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
