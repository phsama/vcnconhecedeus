from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Subscriber, SubscriberStatus
from app.email_service import send_welcome_email
from app.config import settings

router = APIRouter()


@router.get("/verify")
async def verify(token: str, db: Session = Depends(get_db)):
    subscriber = db.query(Subscriber).filter(Subscriber.verify_token == token).first()

    if not subscriber:
        raise HTTPException(status_code=404, detail="Token inválido ou expirado.")

    if subscriber.status != SubscriberStatus.ACTIVE:
        subscriber.status = SubscriberStatus.ACTIVE
        subscriber.verified_at = datetime.now(timezone.utc)
        db.commit()
        # Send welcome email
        send_welcome_email(subscriber.email, subscriber.unsubscribe_token)

    return RedirectResponse(url=f"{settings.public_base_url}/verified", status_code=302)
