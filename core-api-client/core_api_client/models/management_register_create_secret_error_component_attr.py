from enum import Enum


class ManagementRegisterCreateSecretErrorComponentAttr(str, Enum):
    SECRET = "secret"

    def __str__(self) -> str:
        return str(self.value)
