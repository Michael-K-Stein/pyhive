from enum import Enum


class HelpCreateTitleErrorComponentAttr(str, Enum):
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
