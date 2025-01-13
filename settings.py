from pydantic_settings import BaseSettings



class Config(BaseSettings):

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: str
    MAX_POOL_CONNECTIONS: str


settings = Config()
