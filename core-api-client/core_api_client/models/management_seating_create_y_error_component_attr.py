from enum import Enum


class ManagementSeatingCreateYErrorComponentAttr(str, Enum):
    Y = "y"

    def __str__(self) -> str:
        return str(self.value)
