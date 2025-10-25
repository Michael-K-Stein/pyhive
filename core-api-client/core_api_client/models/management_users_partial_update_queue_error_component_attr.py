from enum import Enum


class ManagementUsersPartialUpdateQueueErrorComponentAttr(str, Enum):
    QUEUE = "queue"

    def __str__(self) -> str:
        return str(self.value)
