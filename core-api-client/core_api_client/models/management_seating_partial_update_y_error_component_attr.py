from enum import Enum


class ManagementSeatingPartialUpdateYErrorComponentAttr(str, Enum):
    Y = "y"

    def __str__(self) -> str:
        return str(self.value)
