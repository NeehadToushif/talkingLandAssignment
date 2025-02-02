from pydantic import BaseModel
from typing import List

class PointCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    description : str

class PolygonCreate(BaseModel):
    name: str
    coordinates: List[List[float]]  # List of lat/lon pairs
    info : dict