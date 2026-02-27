import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.config import settings

logger = logging.getLogger(__name__)


def _build_verification_email(to_email: str, verify_url: str) -> MIMEMultipart:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Confirme seu e-mail — Você não conhece Deus"
    msg["From"] = settings.from_email
    msg["To"] = to_email

    text = f"""\
Olá,

Você pediu para receber os conteúdos de "Você não conhece Deus".
Uma pergunta por semana. Uma prática. Um silêncio.

Confirme seu e-mail clicando no link abaixo:

{verify_url}

Se não foi você, ignore esta mensagem.

—
Sem spam. 1 e-mail por semana. Cancelamento em 1 clique.
"""
    msg.attach(MIMEText(text, "plain"))
    return msg


def _build_welcome_email(to_email: str, unsubscribe_url: str) -> MIMEMultipart:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Bem-vindo — Você não conhece Deus"
    msg["From"] = settings.from_email
    msg["To"] = to_email

    text = f"""\
E-mail confirmado.

A partir de agora, você receberá um conteúdo por semana:
— Um texto curto.
— Uma prática (10–20 min).
— Uma pergunta que fica.

Comece onde está.
Observe o que aparece.

Para cancelar a qualquer momento:
{unsubscribe_url}

—
Você não conhece Deus
"""
    msg.attach(MIMEText(text, "plain"))
    return msg


def send_verification_email(to_email: str, token: str) -> None:
    verify_url = f"{settings.public_base_url}/api/verify?token={token}"
    msg = _build_verification_email(to_email, verify_url)

    if not settings.smtp_configured:
        logger.info("=" * 60)
        logger.info("[DEV MODE] Verification link for %s:", to_email)
        logger.info("  %s", verify_url)
        logger.info("=" * 60)
        return

    _send(msg, to_email)


def send_welcome_email(to_email: str, unsubscribe_token: str) -> None:
    unsubscribe_url = f"{settings.public_base_url}/api/unsubscribe?token={unsubscribe_token}"
    msg = _build_welcome_email(to_email, unsubscribe_url)

    if not settings.smtp_configured:
        logger.info("[DEV MODE] Welcome email sent to %s (no SMTP configured)", to_email)
        return

    _send(msg, to_email)


def _send(msg: MIMEMultipart, to_email: str) -> None:
    try:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as server:
            server.starttls()
            server.login(settings.smtp_user, settings.smtp_pass)
            server.sendmail(settings.from_email, to_email, msg.as_string())
    except Exception as e:
        logger.error("Failed to send email to %s: %s", to_email, e)
        raise
