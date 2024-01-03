from abc import ABC, abstractclassmethod, abstractproperty
from dataclasses import dataclass

from email_service.Email import Email


@dataclass
class UnimportanceEmail(ABC):
    @abstractproperty
    def reason(self):
        pass

    @abstractclassmethod
    def check(cls, email: Email) -> float:
        pass
