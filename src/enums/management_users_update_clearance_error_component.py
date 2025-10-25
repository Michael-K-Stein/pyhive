from enum import Enum


class ManagementUsersUpdateClearanceErrorComponentCode(str, Enum):
    INVALID_CHOICE = "invalid_choice"
    MAX_VALUE = "max_value"
    MIN_VALUE = "min_value"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
