from enum import Enum


class ManagementSeatingCreateXErrorComponentAttr(str, Enum):
    X = "x"

    def __str__(self) -> str:
        return str(self.value)
