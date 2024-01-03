from dataclasses import dataclass


@dataclass
class Email:
    id: bytes
    subject: str
    sender: str
    date: str
    body: str
