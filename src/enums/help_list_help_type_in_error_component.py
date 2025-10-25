from enum import Enum


class HelpListHelpTypeInErrorComponentCode(str, Enum):
    NULL_CHARACTERS_NOT_ALLOWED = "null_characters_not_allowed"

    def __str__(self) -> str:
        return str(self.value)
