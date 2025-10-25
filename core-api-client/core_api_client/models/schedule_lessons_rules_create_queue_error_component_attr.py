from enum import Enum


class ScheduleLessonsRulesCreateQueueErrorComponentAttr(str, Enum):
    QUEUE = "queue"

    def __str__(self) -> str:
        return str(self.value)
