from enum import Enum


class ManagementUsersUpdateHostnameErrorComponentAttr(str, Enum):
    HOSTNAME = "hostname"

    def __str__(self) -> str:
        return str(self.value)
