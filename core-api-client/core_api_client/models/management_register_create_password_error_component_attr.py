from enum import Enum


class ManagementRegisterCreatePasswordErrorComponentAttr(str, Enum):
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
