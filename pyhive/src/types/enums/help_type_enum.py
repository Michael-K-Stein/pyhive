from enum import Enum


class HelpTypeEnum(str, Enum):
    CHAT = "Chat"
    ERROR = "Error"
    EXERCISE = "Exercise"
    MEDICAL = "Medical"
    MUSIC = "Music"
    OTHER = "Other"
    REQUEST = "Request"

    def __str__(self) -> str:
        return str(self.value)
