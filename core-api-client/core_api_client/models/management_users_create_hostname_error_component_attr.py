from enum import Enum


class ManagementUsersCreateHostnameErrorComponentAttr(str, Enum):
    HOSTNAME = "hostname"

    def __str__(self) -> str:
        return str(self.value)
