from enum import Enum


class ErrorCode401Enum(str, Enum):
    AUTHENTICATION_FAILED = "authentication_failed"
    NOT_AUTHENTICATED = "not_authenticated"

    def __str__(self) -> str:
        return str(self.value)
