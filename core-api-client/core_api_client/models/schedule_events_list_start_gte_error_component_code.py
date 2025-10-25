from enum import Enum


class ScheduleEventsListStartGteErrorComponentCode(str, Enum):
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
