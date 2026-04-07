from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from routes.estimate import router as estimate_router

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Static + Templates
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Routes
app.include_router(estimate_router)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
