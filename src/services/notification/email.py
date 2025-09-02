import smtplib
from contextlib import contextmanager
from email.mime.text import MIMEText
from typing import Callable, Generator

from services.notification.abc import AbstractNotificationService


class EmailNotificationService(AbstractNotificationService):
    def __init__(
            self,
            domen: str,
            email: str,
            email_password: str,
            ):
        self.smtp_client = smtplib.SMTP(self._domen)
        self._domen = domen
        self._email = email
        self._email_password = email_password

    def login(self) -> None:
        self.smtp_client.starttls()
        self.smtp_client.login(
                user=self._email,
                password=self._email_password)

    def quit(self) -> None:
        self.smtp_client.quit()

    @contextmanager
    def new_session(self) -> Generator:
        self.login()
        yield self
        self.quit()

    def session(
            self,
            func: Callable,
            ) -> Callable:
        def wrapped(*args, **kwargs):
            with self.new_session():
                result = func(*args, **kwargs)
            return result
        return wrapped

    def send_message(
            self,
            recipient: str,
            text: str,
            message_subject: str = "",
            **mail_params,
            ) -> None:
        with self.new_session() as session:
            mail = MIMEText(text, "html")
            mail.set_param(param="Subject", value=message_subject)
            for param_name, param_value in mail_params.items():
                mail.set_param(param=param_name.title(), value=param_value)

            session.smtp_client.sendmail(
                    from_addr=session._email,
                    to_addrs=recipient,
                    msg=mail.as_string())
