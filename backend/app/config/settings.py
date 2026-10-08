import os
from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # App
    APP_NAME: str = "Muin AI - Fikih & Tafsir Engine"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_PORT: int = 8001
    APP_HOST: str = "0.0.0.0"
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ]

    # 9Router AI Gateway
    NINE_ROUTER_BASE_URL: str = "http://localhost:20129/v1"
    NINE_ROUTER_API_KEY: str = Field(default="your-9router-api-key", description="API key untuk 9Router gateway")
    NINE_ROUTER_DEFAULT_MODEL: str = "openai/gpt-4o-mini"
    NINE_ROUTER_FALLBACK_MODEL: str = "deepseek/deepseek-chat"

    # Direct Providers (Opsional jika tanpa 9Router)
    OPENAI_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    DEEPSEEK_API_KEY: str = ""

    # Vector DB (Qdrant)
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_API_KEY: str = ""
    QDRANT_COLLECTION: str = "muin_turats_chunks"

    # Embeddings
    EMBEDDING_PROVIDER: str = "openai"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    EMBEDDING_DIMENSION: int = 1536

    # Storage
    PDF_STORAGE_DIR: str = "storage/pdfs"
    EXTRACTED_STORAGE_DIR: str = "storage/extracted"

settings = Settings()
