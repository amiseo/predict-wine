from fastapi import FastAPI
from fastapi import Body
from fastapi import status

from app.models import Wine
from app.models import Response
from app.usecase import Classifier


app = FastAPI(
    title="Predict wine",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/",
    redoc_url="/redoc"
)


@app.post(
    path="/predict",
    status_code=status.HTTP_200_OK,
    summary="Predict wine cultivation",
    response_model=Response
    )
def predict_wine(wine: Wine = Body(...)):
    return Classifier.predict(wine)
