from enum import Enum


class ScheduleEventsPartialUpdateStartErrorComponentAttr(str, Enum):
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
