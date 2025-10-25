from enum import Enum


class ManagementUsersUpdateStatusErrorComponentAttr(str, Enum):
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
