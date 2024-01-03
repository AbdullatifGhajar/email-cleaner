from email_analyse.UnimportantEmail import UnimportanceEmail
from email_service.Email import Email


class PasswordEmail(UnimportanceEmail):
    @property
    def reason(self):
        return "One Time Password"

    @classmethod
    def check(self, email: Email) -> float:
        score = 0.0

        # Indicator: includes password words
        password_keywords = [
            "password",
            "reset",
            "forget",
            "forgot",
            "otp",
            "code",
            "login",
            "log in",
            "log-in",
            "sign in",
            "sign-in",
            "signin",
        ]

        for keyword in password_keywords:
            if keyword in email.body.lower():
                score += 0.1
            if keyword in email.subject.lower():
                score += 0.3

        return score
