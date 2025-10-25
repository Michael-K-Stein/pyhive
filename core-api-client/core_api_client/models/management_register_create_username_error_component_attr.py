from enum import Enum


class ManagementRegisterCreateUsernameErrorComponentAttr(str, Enum):
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
