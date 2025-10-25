from enum import Enum


class AssignmentsUpdateManualCheckCountErrorComponentCode(str, Enum):
    INVALID = "invalid"
    MAX_STRING_LENGTH = "max_string_length"
    MAX_VALUE = "max_value"
    MIN_VALUE = "min_value"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
