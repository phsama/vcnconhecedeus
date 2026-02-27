import csv
import io
import secrets
import base64
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Subscriber
from app.config import settings

router = APIRouter()


def _authenticate(request: Request) -> None:
    authorization = request.headers.get("Authorization", "")
    if not authorization.startswith("Basic "):
        raise HTTPException(
            status_code=401,
            detail="Autenticação necessária.",
            headers={"WWW-Authenticate": "Basic"},
        )
    try:
        decoded = base64.b64decode(authorization[6:]).decode("utf-8")
        user, pw = decoded.split(":", 1)
    except Exception:
        raise HTTPException(status_code=401, detail="Credenciais inválidas.",
                            headers={"WWW-Authenticate": "Basic"})

    if not (
        secrets.compare_digest(user, settings.admin_user)
        and secrets.compare_digest(pw, settings.admin_pass)
    ):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos.",
            headers={"WWW-Authenticate": "Basic"},
        )


@router.get("/admin/subscribers")
async def export_subscribers(
    request: Request,
    format: str = "csv",
    db: Session = Depends(get_db),
):
    _authenticate(request)

    subscribers = db.query(Subscriber).order_by(Subscriber.created_at.desc()).all()

    if format == "csv":
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["email", "status", "source", "created_at", "verified_at"])
        for s in subscribers:
            writer.writerow([
                s.email,
                s.status.value,
                s.source.value,
                s.created_at.isoformat() if s.created_at else "",
                s.verified_at.isoformat() if s.verified_at else "",
            ])
        output.seek(0)
        return StreamingResponse(
            iter([output.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=subscribers.csv"},
        )

    # JSON fallback
    return [
        {
            "email": s.email,
            "status": s.status.value,
            "source": s.source.value,
            "created_at": s.created_at.isoformat() if s.created_at else None,
            "verified_at": s.verified_at.isoformat() if s.verified_at else None,
        }
        for s in subscribers
    ]
