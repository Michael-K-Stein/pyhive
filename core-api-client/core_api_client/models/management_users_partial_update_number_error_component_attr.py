from enum import Enum


class ManagementUsersPartialUpdateNumberErrorComponentAttr(str, Enum):
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
