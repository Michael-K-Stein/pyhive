from enum import Enum


class ManagementUsersCreateDisableUserQueueErrorComponentAttr(str, Enum):
    DISABLE_USER_QUEUE = "disable_user_queue"

    def __str__(self) -> str:
        return str(self.value)
