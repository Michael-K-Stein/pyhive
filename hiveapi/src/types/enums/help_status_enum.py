from enum import Enum


class HelpStatusEnum(str, Enum):
    OPEN = "Open"
    RESOLVED = "Resolved"

    def __str__(self) -> str:
        return str(self.value)
