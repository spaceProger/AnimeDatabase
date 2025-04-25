from pydantic_settings import BaseSettings


class EmailConfig(BaseSettings):
    EMAIL_BOX: str
    EMAIL_BOX_PASSWORD: str

    @property
    def EMAIL_DOMEN(self) -> str:
        return "smtp." + self.EMAIL_BOX.split('@')[1]
