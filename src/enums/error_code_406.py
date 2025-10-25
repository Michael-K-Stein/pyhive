from enum import Enum


class ErrorCode406Enum(str, Enum):
    NOT_ACCEPTABLE = "not_acceptable"

    def __str__(self) -> str:
        return str(self.value)
