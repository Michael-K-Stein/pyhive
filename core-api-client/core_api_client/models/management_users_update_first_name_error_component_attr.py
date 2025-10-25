from enum import Enum


class ManagementUsersUpdateFirstNameErrorComponentAttr(str, Enum):
    FIRST_NAME = "first_name"

    def __str__(self) -> str:
        return str(self.value)
