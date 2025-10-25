from enum import Enum


class AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
