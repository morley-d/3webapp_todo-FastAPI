import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()


class Settings(BaseSettings):
    app_name: str = os.getenv('NAME_APP')
    db_url: str = os.getenv('SQLALCHEMY_DATABASE_URI')

    class Config:
        env_file: str = '../.env'


settings = Settings()
