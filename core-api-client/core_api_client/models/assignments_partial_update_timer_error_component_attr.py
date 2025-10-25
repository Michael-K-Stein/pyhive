from enum import Enum


class AssignmentsPartialUpdateTimerErrorComponentAttr(str, Enum):
    TIMER = "timer"

    def __str__(self) -> str:
        return str(self.value)
