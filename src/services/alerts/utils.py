from config import main_config
from services.alerts.email import EmailClient


def client() -> EmailClient:
    return EmailClient(
        domen=main_config.EMAIL_DOMEN,
        email_box=main_config.EMAIL_BOX,
        email_box_password=main_config.EMAIL_BOX_PASSWORD,
    )
