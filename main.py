from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from routes import estimate, excel, cad, pdf

app = FastAPI()

# 🔹 Get base directory (important for Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔹 Static files (CSS, JS)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# 🔹 Templates (HTML)
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

# 🔹 Include all routes
app.include_router(estimate.router)
app.include_router(excel.router)
app.include_router(cad.router)
app.include_router(pdf.router)

# 🔹 Home route (UI)
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request}
    )
