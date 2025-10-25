from enum import Enum


class ManagementUsersUpdateUserQueueErrorComponentAttr(str, Enum):
    USER_QUEUE = "user_queue"

    def __str__(self) -> str:
        return str(self.value)
