from enum import Enum


class ManagementClassesQueueCreateQueueErrorComponentAttr(str, Enum):
    QUEUE = "queue"

    def __str__(self) -> str:
        return str(self.value)
