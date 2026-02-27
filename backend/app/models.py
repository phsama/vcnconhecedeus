import enum
import secrets
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class SubscriberStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    UNSUBSCRIBED = "UNSUBSCRIBED"


class SubscriberSource(str, enum.Enum):
    newsletter = "newsletter"
    waitlist = "waitlist"


class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    status = Column(Enum(SubscriberStatus), default=SubscriberStatus.PENDING, nullable=False)
    source = Column(Enum(SubscriberSource), default=SubscriberSource.newsletter, nullable=False)
    verify_token = Column(String, unique=True, nullable=False, default=lambda: secrets.token_urlsafe(32))
    unsubscribe_token = Column(String, unique=True, nullable=False, default=lambda: secrets.token_urlsafe(32))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    verified_at = Column(DateTime(timezone=True), nullable=True)
