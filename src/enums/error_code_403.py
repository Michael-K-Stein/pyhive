from enum import Enum


class ErrorCode403Enum(str, Enum):
    PERMISSION_DENIED = "permission_denied"

    def __str__(self) -> str:
        return str(self.value)
