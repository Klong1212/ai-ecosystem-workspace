from pydantic import BaseModel,engine
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: redis://user:password@localhost/dbname