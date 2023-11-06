from pydantic import BaseModel, Field
from datetime import datetime as dt
from pytz import timezone as tz


class ItemSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)  # additional validation for the inputs
    description: str = Field(..., min_length=3, max_length=50)
    completed: str = "False"
    created_date: str = dt.now(tz("Africa/Nairobi")).strftime("%Y-%m-%d %H:%M")


class ItemRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)  # additional validation for the inputs
    description: str = Field(..., min_length=3, max_length=50)
    completed: str = "False"


class ItemDB(ItemSchema):
    id: int
