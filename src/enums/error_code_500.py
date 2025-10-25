from enum import Enum


class ErrorCode500Enum(str, Enum):
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
