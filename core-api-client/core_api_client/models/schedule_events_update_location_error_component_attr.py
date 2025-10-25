from enum import Enum


class ScheduleEventsUpdateLocationErrorComponentAttr(str, Enum):
    LOCATION = "location"

    def __str__(self) -> str:
        return str(self.value)
