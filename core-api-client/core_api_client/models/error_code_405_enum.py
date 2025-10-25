from enum import Enum


class ErrorCode405Enum(str, Enum):
    METHOD_NOT_ALLOWED = "method_not_allowed"

    def __str__(self) -> str:
        return str(self.value)
