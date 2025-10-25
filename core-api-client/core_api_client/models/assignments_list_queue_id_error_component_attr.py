from enum import Enum


class AssignmentsListQueueIdErrorComponentAttr(str, Enum):
    QUEUE_ID = "queue__id"

    def __str__(self) -> str:
        return str(self.value)
