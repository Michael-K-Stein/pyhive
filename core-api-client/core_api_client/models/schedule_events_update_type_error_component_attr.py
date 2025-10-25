from enum import Enum


class ScheduleEventsUpdateTypeErrorComponentAttr(str, Enum):
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
