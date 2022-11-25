from pydantic import BaseModel, Field
from typing import List

class Media(BaseModel):
    items: List[str] = Field(min_items = 0, max_items = 5)