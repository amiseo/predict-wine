from fastapi import FastAPI


app = FastAPI(
    title="Predict wine",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/",
    redoc_url="/redoc"
)



