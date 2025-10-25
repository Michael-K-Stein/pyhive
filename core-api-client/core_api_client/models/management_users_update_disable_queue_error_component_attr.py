from enum import Enum


class ManagementUsersUpdateDisableQueueErrorComponentAttr(str, Enum):
    DISABLE_QUEUE = "disable_queue"

    def __str__(self) -> str:
        return str(self.value)
