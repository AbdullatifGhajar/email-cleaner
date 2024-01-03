from email_service.Email import Email

from .UnimportantEmail import UnimportanceEmail


class ConfirmationEmail(UnimportanceEmail):
    @property
    def reason(self):
        return "Confirmation Email"

    @classmethod
    def check(self, email: Email) -> float:
        score = 0.0

        # Indicator: includes the some confirmation words
        confirmation_keywords = [
            "confirmation",
            "confirm",
            "verify",
            "verification",
            "validate",
            "validation",
            "activate",
            "activation",
        ]
        for keyword in confirmation_keywords:
            if keyword in email.body:
                score += 0.1
            if keyword in email.subject:
                score += 0.3

        # Indicator: includes a link or button
        link_keywords = ["click", "link", "button", "http://", "https://", "href"]
        for keyword in link_keywords:
            if keyword in email.body:
                score += 0.1

        # Indicator: sent from a "no-reply" or "noreply" address
        if "no-reply" in email.sender or "noreply" in email.sender:
            score += 0.2

        return score
