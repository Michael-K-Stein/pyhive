from enum import Enum


class ScheduleKioskPartialUpdateLocationErrorComponentAttr(str, Enum):
    LOCATION = "location"

    def __str__(self) -> str:
        return str(self.value)
