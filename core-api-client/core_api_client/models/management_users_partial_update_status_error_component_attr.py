from enum import Enum


class ManagementUsersPartialUpdateStatusErrorComponentAttr(str, Enum):
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
