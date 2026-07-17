from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    redis_url: str = "redis://localhost:6379"
    postgres_url: str = "postgresql://postgres:postgres@localhost:5432/postgres"
    label_studio_url: str = "http://localhost:8080"