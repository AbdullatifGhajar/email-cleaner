from dataclasses import dataclass

from email_service import Sender


@dataclass
class Email:
    id: bytes
    subject: str
    sender: Sender
    date: str
    body: str
