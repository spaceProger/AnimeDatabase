from pydantic_settings import BaseSettings


class RedisConfig(BaseSettings):
    REDIS_USER: str
    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB_NAME: str

    @property
    def REDIS_URL(self) -> str:
        return (f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@"
                f"{self.REDIS_HOST}:{self.REDIS_PORT}/"
                f"{self.REDIS_DB_NAME}")
