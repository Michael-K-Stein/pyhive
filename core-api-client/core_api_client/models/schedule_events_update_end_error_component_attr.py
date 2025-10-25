from enum import Enum


class ScheduleEventsUpdateEndErrorComponentAttr(str, Enum):
    END = "end"

    def __str__(self) -> str:
        return str(self.value)
