from enum import Enum


class HelpUpdateVisibilityErrorComponentCode(str, Enum):
    INVALID_CHOICE = "invalid_choice"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
