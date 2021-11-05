from starlette import responses
from app.models import Wine
from app.models import Response

from joblib import load


CLASSIFER = load("model.pkl")


class Classifier:


    @staticmethod
    def predict(wine: Wine):
        result = CLASSIFER.predict([list(wine.dict().values())])
        response = Response(wine_cultivation=result[0])
        return response
