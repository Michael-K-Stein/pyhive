from enum import Enum


class ManagementUsersUpdateStatusErrorComponentCode(str, Enum):
    INVALID_CHOICE = "invalid_choice"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
