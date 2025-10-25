from enum import Enum


class QueuesUpdateNonFieldErrorsErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NULL = "null"
    UNIQUE = "unique"

    def __str__(self) -> str:
        return str(self.value)
