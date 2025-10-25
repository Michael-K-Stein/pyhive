from enum import Enum


class NotificationUpdateWasReadErrorComponentAttr(str, Enum):
    WAS_READ = "was_read"

    def __str__(self) -> str:
        return str(self.value)
