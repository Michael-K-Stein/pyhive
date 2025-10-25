from enum import Enum


class ScheduleKioskUpdateLocationErrorComponentAttr(str, Enum):
    LOCATION = "location"

    def __str__(self) -> str:
        return str(self.value)
