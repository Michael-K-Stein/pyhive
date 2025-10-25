from enum import Enum


class ManagementUsersPartialUpdatePasswordErrorComponentAttr(str, Enum):
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
