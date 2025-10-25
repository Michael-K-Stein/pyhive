from enum import Enum


class ManagementSeatingUpdateYErrorComponentAttr(str, Enum):
    Y = "y"

    def __str__(self) -> str:
        return str(self.value)
