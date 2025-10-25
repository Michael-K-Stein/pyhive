from enum import Enum


class AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
