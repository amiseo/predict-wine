from fastapi import FastAPI
from fastapi import Body

from app.models import Wine

app = FastAPI(
    title="Predict wine",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/",
    redoc_url="/redoc"
)

@app.post("/predict")
def predict_wine(wine: Wine = Body(...)):
    return wine