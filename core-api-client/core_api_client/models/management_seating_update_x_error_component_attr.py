from enum import Enum


class ManagementSeatingUpdateXErrorComponentAttr(str, Enum):
    X = "x"

    def __str__(self) -> str:
        return str(self.value)
