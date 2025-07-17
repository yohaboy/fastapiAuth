from pydantic_settings import BaseSettings ,SettingsConfigDict

class Settings(BaseSettings):
    USERNAME : str
    PASSWORD : str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()