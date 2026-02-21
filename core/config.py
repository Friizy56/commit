from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application configuration settings"""
    
    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/commit_ai"
    
    # App settings
    APP_NAME: str = "Commit AI"
    DEBUG: bool = True
    
    # Security settings
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # LLM settings
    LLM_MODEL: str = "llama3.1:8b"
    LLM_API_URL: str = "http://localhost:11434"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    """Get cached settings instance"""
    return Settings()
