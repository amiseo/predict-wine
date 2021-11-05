#Pydantic
from pydantic import BaseModel
from pydantic import Field

#Models
class Wine(BaseModel):
    alcohol: float = Field(
        ...,
        gt=0,
        lt=50,
        example=14.34
    )
    malic_acid: float = Field(
        ...,
        gt=0,
        lt=20,
        example=1.68
    )
    ash: float = Field(
        ...,
        gt=0,
        lt=10,
        example=2.7
    )
    alcalinity_of_ash: float = Field(
        ...,
        gt=0,
        lt=100,
        example=25.0
    )
    magnesium: float = Field(
        ...,
        gt=0,
        lt=500,
        example=98.0
    )
    total_phenols: float = Field(
        ...,
        gt=0,
        lt=15,
        example=2.8
    )
    flavanoids: float = Field(
        ...,
        gt=0,
        lt=20,
        example=1.31
    )
    nonflavanoidPhenols: float = Field(
        ...,
        gt=0,
        lt=5,
        example=0.53
    )
    proanthocyanins: float = Field(
        ...,
        gt=0,
        lt=15,
        example=2.7
    )
    color_intensity: float = Field(
        ...,
        gt=0,
        lt=50,
        example=13.0
    )
    hue: float = Field(
        ...,
        gt=0,
        lt=5,
        example=0.57
    )
    diluted_wines: float = Field(
        ...,
        gt=0,
        lt=20,
        example=1.96

    )
    proline: float = Field(
        ...,
        gt=0,
        lt=5000,
        example=660.0
    )
