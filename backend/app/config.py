from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # SMTP
    smtp_host: str = ""
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_pass: str = ""
    from_email: str = "noreply@vocenahconhecedeus.com.br"

    # App
    public_base_url: str = "http://localhost:3000"

    # Admin
    admin_user: str = "admin"
    admin_pass: str = "changeme"

    # DB
    database_url: str = "sqlite:///./data/subscribers.db"

    @property
    def smtp_configured(self) -> bool:
        return bool(self.smtp_host and self.smtp_user and self.smtp_pass)


settings = Settings()
