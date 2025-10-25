from enum import Enum


class ManagementSeatingPartialUpdateXErrorComponentAttr(str, Enum):
    X = "x"

    def __str__(self) -> str:
        return str(self.value)
