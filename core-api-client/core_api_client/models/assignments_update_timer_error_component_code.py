from enum import Enum


class AssignmentsUpdateTimerErrorComponentCode(str, Enum):
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
