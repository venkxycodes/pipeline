from pydantic import BaseModel
from typing import Optional, Dict

class Event(BaseModel):
    event_name: str
    user_id: str
    timestamp: Optional[str]
    properties: Optional[Dict[str, str]] = {}
