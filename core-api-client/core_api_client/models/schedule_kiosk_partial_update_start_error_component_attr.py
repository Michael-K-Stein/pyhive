from enum import Enum


class ScheduleKioskPartialUpdateStartErrorComponentAttr(str, Enum):
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
