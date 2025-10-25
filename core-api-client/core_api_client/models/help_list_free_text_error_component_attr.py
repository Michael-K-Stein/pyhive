from enum import Enum


class HelpListFreeTextErrorComponentAttr(str, Enum):
    FREE_TEXT = "free_text"

    def __str__(self) -> str:
        return str(self.value)
