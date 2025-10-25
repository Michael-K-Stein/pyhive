from enum import Enum


class ScheduleKioskListStartGteErrorComponentAttr(str, Enum):
    START_GTE = "start__gte"

    def __str__(self) -> str:
        return str(self.value)
