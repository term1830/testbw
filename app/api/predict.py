import logging
import random
import joblib
from joblib import load
# .strip()
pipeline = load(r'assets\pipeline.joblib')

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()



class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    x1: float = Field(..., example=3.14)
    x2: int = Field(..., example=-42)
    x3: str = Field(..., example='banjo')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that x1 is a positive number."""
        assert value > 0, f'x1 == {value}, must be > 0'
        return value


def get_prediction(input):
    return prediction

@router.post('/predict')
async def predict(item: str):
    """
    ## How to use:
    * Click "try it out."
    * Enter various items in the kickstart campaign needed
    * Monetary goal, time live, etc
    * This will give a response of whether or not the campaign is likely to succeed
    ## Needed Info:
    - `item`: item1
    - `item`: item2
    - `item`: item3
    - `item`: item4
    ## Response:
    - Whether or not the kickstarter is likely to be a success or not.
    """

    success_failure = get_prediction(item)
    return {
        success_failure
    }
