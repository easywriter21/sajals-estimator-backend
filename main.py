from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes import estimate, excel, cad, pdf

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(estimate.router)
app.include_router(excel.router)
app.include_router(cad.router)
app.include_router(pdf.router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",              
        context={"request": request}    
    )
