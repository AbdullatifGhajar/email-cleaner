from UnimportantEmail import UnimportanceEmail

from email_service.Email import Email


class NewsletterEmail(UnimportanceEmail):
    @property
    def reason(self):
        return "Newsletter Email"

    @classmethod
    def check(self, email: Email) -> float:
        score = 0.0

        # Indicator: includes newsletter words
        newsletter_keywords = [
            "newsletter",
            "news",
            "update",
            "updates",
            "subscribe",
            "subscription",
            "unsubscribe",
            "unsubscription",
            "opt-out",
            "opt out",
            "optout",
            "opt-in",
            "opt in",
            "optin",
        ]

        for keyword in newsletter_keywords:
            if keyword in email.body.lower():
                score += 0.1
            if keyword in email.subject.lower():
                score += 0.3

        return score
