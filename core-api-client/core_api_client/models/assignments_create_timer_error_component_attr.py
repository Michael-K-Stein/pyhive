from enum import Enum


class AssignmentsCreateTimerErrorComponentAttr(str, Enum):
    TIMER = "timer"

    def __str__(self) -> str:
        return str(self.value)
