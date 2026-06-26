from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "jdbc:postgresql://ep-calm-recipe-atj5t1rx-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="")

settings = Settings()