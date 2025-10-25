from enum import Enum


class HelpCreateVisibilityErrorComponentAttr(str, Enum):
    VISIBILITY = "visibility"

    def __str__(self) -> str:
        return str(self.value)
