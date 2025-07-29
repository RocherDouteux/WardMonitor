from pydantic import BaseModel
from typing import List

class Plot(BaseModel):
    price: int
    size: str  # "S", "M", or "L"

class Ward(BaseModel):
    ward_id: int
    plots: List[Plot]

class Region(BaseModel):
    region_name: str
    wards: List[Ward]
