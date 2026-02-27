from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Subscriber, SubscriberStatus
from app.config import settings

router = APIRouter()


@router.get("/unsubscribe")
async def unsubscribe(token: str, db: Session = Depends(get_db)):
    subscriber = db.query(Subscriber).filter(Subscriber.unsubscribe_token == token).first()

    if not subscriber:
        raise HTTPException(status_code=404, detail="Token inválido.")

    if subscriber.status != SubscriberStatus.UNSUBSCRIBED:
        subscriber.status = SubscriberStatus.UNSUBSCRIBED
        db.commit()

    return RedirectResponse(url=f"{settings.public_base_url}/unsubscribed", status_code=302)
