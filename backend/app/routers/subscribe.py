from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Subscriber, SubscriberStatus, SubscriberSource
from app.schemas import SubscribeRequest, SubscribeResponse
from app.email_service import send_verification_email

router = APIRouter()

# Simple in-memory rate limiting: {ip: [timestamps]}
import time
from collections import defaultdict

_rate_store: dict[str, list[float]] = defaultdict(list)
RATE_WINDOW = 60  # seconds
RATE_LIMIT = 5  # max requests per window


def _check_rate_limit(ip: str) -> None:
    now = time.time()
    timestamps = [t for t in _rate_store[ip] if now - t < RATE_WINDOW]
    _rate_store[ip] = timestamps
    if len(timestamps) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Muitas tentativas. Aguarde um momento.")
    _rate_store[ip].append(now)


@router.post("/subscribe", response_model=SubscribeResponse)
async def subscribe(request: Request, body: SubscribeRequest, db: Session = Depends(get_db)):
    # Rate limit
    client_ip = request.client.host if request.client else "unknown"
    _check_rate_limit(client_ip)

    # Honeypot
    if body.website:
        # Return fake success to fool bots
        return SubscribeResponse(message="Cadastro realizado! Verifique seu e-mail.")

    # Validate source
    try:
        source = SubscriberSource(body.source)
    except ValueError:
        source = SubscriberSource.newsletter

    existing = db.query(Subscriber).filter(Subscriber.email == body.email).first()

    if existing:
        if existing.status == SubscriberStatus.ACTIVE:
            # Idempotent — already confirmed
            return SubscribeResponse(message="E-mail já cadastrado e confirmado.")
        elif existing.status == SubscriberStatus.UNSUBSCRIBED:
            raise HTTPException(status_code=409, detail="Este e-mail está descadastrado. Entre em contato se quiser reativar.")
        else:
            # PENDING — resend verification
            send_verification_email(existing.email, existing.verify_token)
            return SubscribeResponse(message="Cadastro realizado! Verifique seu e-mail.")

    # New subscriber
    subscriber = Subscriber(email=body.email, source=source)
    db.add(subscriber)
    db.commit()
    db.refresh(subscriber)

    send_verification_email(subscriber.email, subscriber.verify_token)

    return SubscribeResponse(message="Cadastro realizado! Verifique seu e-mail.")
