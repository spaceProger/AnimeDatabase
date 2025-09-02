from services.abc import AbstractObserver
from services.auth.types import SignUpEvent
from services.notification.abc import AbstractNotificationService
from services.notification import messages as notify_messages


class SignUpNotificationObserver(AbstractObserver):
    def __init__(
            self,
            notification_service: AbstractNotificationService,
            ) -> None:
        self.notification_service = notification_service

    def accept(self, event: SignUpEvent) -> None:
        text = notify_messages.SIGNUP_EMAIL_MESSAGE
        text = text.format(code=event.auth_code)
        subject = notify_messages.SIGNUP_EMAIL_SUBJECT

        self.notification_service.send_message(
            recipient=event.user_email,
            text=text,
            message_subject=subject)
