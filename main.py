from icecream import ic

from email_analyse.ConfirmationEmail import ConfirmationEmail
from email_analyse.PasswordEmail import PasswordEmail
from email_service.EmailManager import EmailManager

if __name__ == "__main__":
    with EmailManager() as email_importer:
        for email in email_importer.emails():
            ic(ConfirmationEmail.check(email))
            ic(PasswordEmail.check(email))
