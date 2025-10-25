from enum import Enum


class ManagementUsersCreateStatusErrorComponentAttr(str, Enum):
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
