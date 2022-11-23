from pydantic import BaseModel

class Range(BaseModel):
    min: float
    max: float

class GetTipsByRequest(BaseModel):
    tipster_id: str | None = None
    match_id: str | None = None
    bookie_id: str | None = None
    rate_range: Range | None = None
    stake_range: Range | None = None
    pick_id: str | None = None
    media: str | None = None