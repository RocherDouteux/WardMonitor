from pydantic import BaseModel
from typing import List

class Plot(BaseModel):
    plot_number: int
    price: int
    size: str  # "S", "M", or "L"
    available: bool = True

class Ward(BaseModel):
    ward_id: int
    plots: List[Plot]

class Region(BaseModel):
    region_name: str
    wards: List[Ward]
