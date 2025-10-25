from enum import Enum


class HelpListHelpStatusInErrorComponentCode(str, Enum):
    NULL_CHARACTERS_NOT_ALLOWED = "null_characters_not_allowed"

    def __str__(self) -> str:
        return str(self.value)
