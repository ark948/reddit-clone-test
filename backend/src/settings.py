from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    db_connection_string: str
    api_key: str