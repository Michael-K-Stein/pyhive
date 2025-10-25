from enum import Enum


class ScheduleKioskListEndLteErrorComponentCode(str, Enum):
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
