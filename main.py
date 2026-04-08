from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from routes.estimate import router as estimate_router
from routes.excel import router as excel_router

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Static files
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# Templates
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

# Routers
app.include_router(estimate_router)
app.include_router(excel_router)

# Home route
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
