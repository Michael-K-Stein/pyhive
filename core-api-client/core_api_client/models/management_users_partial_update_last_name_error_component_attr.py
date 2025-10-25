from enum import Enum


class ManagementUsersPartialUpdateLastNameErrorComponentAttr(str, Enum):
    LAST_NAME = "last_name"

    def __str__(self) -> str:
        return str(self.value)
