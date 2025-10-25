from enum import Enum


class ManagementUsersPartialUpdateUserQueueErrorComponentAttr(str, Enum):
    USER_QUEUE = "user_queue"

    def __str__(self) -> str:
        return str(self.value)
