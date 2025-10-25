from enum import Enum


class ScheduleEventsCreateEndErrorComponentAttr(str, Enum):
    END = "end"

    def __str__(self) -> str:
        return str(self.value)
