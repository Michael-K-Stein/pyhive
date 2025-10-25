from enum import Enum


class ScheduleKioskCreateStartErrorComponentAttr(str, Enum):
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
