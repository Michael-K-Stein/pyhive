from enum import Enum


class HelpPartialUpdateTitleErrorComponentAttr(str, Enum):
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
