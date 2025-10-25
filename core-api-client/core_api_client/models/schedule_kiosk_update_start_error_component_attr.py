from enum import Enum


class ScheduleKioskUpdateStartErrorComponentAttr(str, Enum):
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
