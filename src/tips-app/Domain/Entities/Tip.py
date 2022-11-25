from pydantic import BaseModel, Field
from Domain.Entities.Media import Media

class Tip(BaseModel):
    tipster_id: str = Field(min_length=1)
    match_id: str = Field(min_length=1)
    analysis: str = Field(min_length=1)
    bookie_id: str = Field(min_length=1)
    rate: float = Field(gt=0.0)
    stake: float = Field(ge=1.0, le=10.0)
    pick_id: str = Field(min_length=1)
    media: Media