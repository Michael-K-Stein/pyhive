from enum import Enum


class ScheduleKioskListStartGteErrorComponentCode(str, Enum):
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
