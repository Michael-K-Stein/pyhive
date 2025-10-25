from enum import Enum


class ScheduleEventsListStartGteErrorComponentAttr(str, Enum):
    START_GTE = "start__gte"

    def __str__(self) -> str:
        return str(self.value)
