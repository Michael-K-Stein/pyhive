from enum import Enum


class ErrorCode404Enum(str, Enum):
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)
