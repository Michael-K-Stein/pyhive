from enum import Enum


class ScheduleLessonsRulesUpdateQueueErrorComponentAttr(str, Enum):
    QUEUE = "queue"

    def __str__(self) -> str:
        return str(self.value)
