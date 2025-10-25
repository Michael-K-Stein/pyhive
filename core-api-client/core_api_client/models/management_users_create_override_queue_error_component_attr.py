from enum import Enum


class ManagementUsersCreateOverrideQueueErrorComponentAttr(str, Enum):
    OVERRIDE_QUEUE = "override_queue"

    def __str__(self) -> str:
        return str(self.value)
