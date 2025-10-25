from enum import Enum


class ManagementUsersUpdateNumberErrorComponentAttr(str, Enum):
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
