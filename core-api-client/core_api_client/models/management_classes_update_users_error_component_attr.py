from enum import Enum


class ManagementClassesUpdateUsersErrorComponentAttr(str, Enum):
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
