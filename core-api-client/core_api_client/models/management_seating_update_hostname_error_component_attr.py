from enum import Enum


class ManagementSeatingUpdateHostnameErrorComponentAttr(str, Enum):
    HOSTNAME = "hostname"

    def __str__(self) -> str:
        return str(self.value)
