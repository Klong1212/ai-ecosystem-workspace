from pydantic_settings import BaseSettings,SettingsConfigDict



class Settings(BaseSettings):
    """Application settings."""
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    database_url: str
    minio_endpoint: str = "localhost:9000"
    minio_root_user: str = "minioadmin"
    minio_root_password: str = "minioadmin"
    minio_secure: bool = False