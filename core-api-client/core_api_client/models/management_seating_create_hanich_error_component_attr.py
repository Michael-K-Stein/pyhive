from enum import Enum


class ManagementSeatingCreateHanichErrorComponentAttr(str, Enum):
    HANICH = "hanich"

    def __str__(self) -> str:
        return str(self.value)
