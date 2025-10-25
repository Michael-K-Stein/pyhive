from enum import Enum


class ManagementUsersMePartialUpdateCurrentPasswordErrorComponentAttr(str, Enum):
    CURRENT_PASSWORD = "current_password"

    def __str__(self) -> str:
        return str(self.value)
