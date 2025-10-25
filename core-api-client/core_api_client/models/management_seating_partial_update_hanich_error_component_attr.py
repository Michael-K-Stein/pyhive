from enum import Enum


class ManagementSeatingPartialUpdateHanichErrorComponentAttr(str, Enum):
    HANICH = "hanich"

    def __str__(self) -> str:
        return str(self.value)
