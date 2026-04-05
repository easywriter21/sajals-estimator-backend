from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from utils.master_estimator import master_estimate

router = APIRouter()

@router.post("/estimate/", response_class=HTMLResponse)
async def estimate(text: str = Form(...)):
    try:
        result = master_estimate(text)

        return f"""
        <html>
        <body>
            <h2>Estimation Result</h2>
            <pre>{result}</pre>
            <br>
            <a href="/">Back</a>
        </body>
        </html>
        """

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
