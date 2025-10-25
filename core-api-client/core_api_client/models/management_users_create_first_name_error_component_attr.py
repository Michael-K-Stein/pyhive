from enum import Enum


class ManagementUsersCreateFirstNameErrorComponentAttr(str, Enum):
    FIRST_NAME = "first_name"

    def __str__(self) -> str:
        return str(self.value)
