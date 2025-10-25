from enum import Enum


class QueuesItemsMoveCreateNewOrderErrorComponentCode(str, Enum):
    INVALID = "invalid"
    MAX_STRING_LENGTH = "max_string_length"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
