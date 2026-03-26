from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import estimate, excel, cad, pdf

app = FastAPI(title="Sajal's Estimator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(estimate.router)
app.include_router(excel.router)
app.include_router(cad.router)
app.include_router(pdf.router)

@app.get("/")
def home():
    return {
        "project": "Sajal's Estimator",
        "assistant": "Estimator",
        "status": "Running"
    }
