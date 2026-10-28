# """
# Shared UI configuration — single source of truth for all components.
# """
# import os


# def _normalize_url(url: str) -> str:
#     return url.rstrip("/")


# API_BASE: str = _normalize_url(
#     os.environ.get("NEURAL_SEARCH_API_URL", "http://localhost:8000")
# )



from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    embedding_model: str = "all-MiniLM-L6-v2"
    documents_dir: str = "data/documents"
    qdrant_path: str = "data/qdrant"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()