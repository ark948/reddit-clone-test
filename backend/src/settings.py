from pydantic_settings import BaseSettings, SettingsConfigDict

# i am aware that this is basically duplicate of config.py

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra="ignore"
    )



settings = Settings()