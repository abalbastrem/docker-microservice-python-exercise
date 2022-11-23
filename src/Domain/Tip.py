from pydantic import BaseModel, Field
from Domain.Media import Media

class Tip(BaseModel):
    tipster_id: str
    match_id: str
    analysis: str
    bookie_id: str
    rate: float
    stake: float = Field(ge=1.0, le=10.0)
    pick_id: str
    media: Media