from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class SubscribeRequest(BaseModel):
    email: EmailStr
    source: str = "newsletter"
    website: str = ""  # honeypot field — must be empty


class SubscribeResponse(BaseModel):
    message: str


class SubscriberRow(BaseModel):
    email: str
    status: str
    source: str
    created_at: Optional[datetime]
    verified_at: Optional[datetime]
