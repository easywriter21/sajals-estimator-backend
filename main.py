from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.estimate import router as estimate_router

app = FastAPI()

app.include_router(estimate_router)


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <title>Sajal Estimator</title>
    </head>
    <body style="font-family: Arial; text-align:center; margin-top:50px;">
        <h1>Sajal Estimator</h1>

        <form action="/estimate/" method="post">
            <textarea name="text" placeholder="Enter project details" required></textarea><br><br>

            <input type="number" name="cement" placeholder="Cement price" required><br><br>
            <input type="number" name="steel" placeholder="Steel price" required><br><br>
            <input type="number" name="sand" placeholder="Sand price" required><br><br>
            <input type="number" name="aggregate" placeholder="Aggregate price" required><br><br>
            <input type="number" name="labour" placeholder="Labour cost" required><br><br>

            <button type="submit">Estimate</button>
        </form>
    </body>
    </html>
    """
