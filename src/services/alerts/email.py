from email.mime.text import MIMEText
import smtplib


class EmailClient(smtplib.SMTP):
    def __init__(
            self,
            domen: str,
            email_box: str,
            email_box_password: str,
            ):
        self.__domen = domen
        self.__email_box = email_box
        self.__email_box_password = email_box_password
        super().__init__(self.__domen)

    def message(
            self,
            to_email_box: str,
            text: str,
            subject: str | None = None,
            ):
        self.starttls()
        self.login(self.__email_box, self.__email_box_password)
        mail = MIMEText(text, "html")
        mail["Subject"] = subject
        self.sendmail(self.__email_box, to_email_box, mail.as_string())
        self.quit()
