from enum import Enum


class NotificationCreateWasReadErrorComponentAttr(str, Enum):
    WAS_READ = "was_read"

    def __str__(self) -> str:
        return str(self.value)
