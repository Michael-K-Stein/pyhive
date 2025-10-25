from enum import Enum


class ScheduleEventsPartialUpdateEndErrorComponentAttr(str, Enum):
    END = "end"

    def __str__(self) -> str:
        return str(self.value)
