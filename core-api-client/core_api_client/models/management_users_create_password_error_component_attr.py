from enum import Enum


class ManagementUsersCreatePasswordErrorComponentAttr(str, Enum):
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
