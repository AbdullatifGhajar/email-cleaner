import re
from dataclasses import dataclass


@dataclass
class Sender:
    name: str
    email: str

    @classmethod
    def from_string(cls, string: str):
        # example string: "John Doe <john.doe@example>"
        match = re.match(r"(.*) <(.*)>", string)
        if match:
            name = match.group(1)
            email = match.group(2)
            return cls(name, email)
        else:
            return cls(string, string)
