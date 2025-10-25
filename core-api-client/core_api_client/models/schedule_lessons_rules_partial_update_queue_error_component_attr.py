from enum import Enum


class ScheduleLessonsRulesPartialUpdateQueueErrorComponentAttr(str, Enum):
    QUEUE = "queue"

    def __str__(self) -> str:
        return str(self.value)
