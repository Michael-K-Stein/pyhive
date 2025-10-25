from enum import Enum


class ManagementUsersUpdateUsernameErrorComponentAttr(str, Enum):
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
