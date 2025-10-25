from enum import Enum


class HelpUpdateTitleErrorComponentAttr(str, Enum):
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
