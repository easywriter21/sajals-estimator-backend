from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import estimate, excel, cad

app = FastAPI(
    title="Sajal's Estimator",
    description="AI Civil Engineering Estimator Backend",
    version="1.0"
)

# Allow frontend connection
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

@app.get("/")
def home():
    return {
        "project": "Sajal's Estimator",
        "assistant": "Estimator",
        "status": "Backend Running"
    }
