from pydantic import BaseModel

class Tip(BaseModel):
    tipster_id: str
    match_id: str
    analysis: str
    bookie_id: str
    rate: float
    stake: float
    pick_id: str
    media: str | None