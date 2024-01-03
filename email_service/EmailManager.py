import email
import imaplib
import os
from email.header import decode_header

from .Email import Email

# Email account credentials
IMAP_SERVER = os.environ.get("IMAP_SERVER")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


class EmailManager:
    def __init__(self, imap_server=IMAP_SERVER, address=EMAIL_ADDRESS, password=EMAIL_PASSWORD, mailbox="inbox"):
        self.imap_server = imap_server
        self.email_address = address
        self.email_password = password
        self.mailbox = mailbox

    def __enter__(self):
        self.mail = imaplib.IMAP4_SSL(self.imap_server)
        self.mail.login(self.email_address, self.email_password)
        self.mail.select(self.mailbox)

        status, messages = self.mail.search(None, "ALL")
        self.message_ids: list[str] = [msg.decode() for msg in messages[0].split()]

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.mail.logout()

    def get_email(self, message_id):
        status, msg_data = self.mail.fetch(message_id, "(RFC822)")
        raw_email = msg_data[0][1]

        msg = email.message_from_bytes(raw_email)

        # Extract email information
        subject, encoding = decode_header(msg["Subject"])[0]
        sender, encoding = decode_header(msg["From"])[0]
        date, encoding = decode_header(msg["Date"])[0]
        body = msg.get_payload()[0].as_string()

        return Email(
            id=message_id,
            subject=subject,
            sender=sender,
            date=date,
            body=body,
        )

    # TODO
    def delete_email(self, message_id):
        pass

    def emails(self):
        for message_id in self.message_ids:
            yield self.get_email(message_id)
