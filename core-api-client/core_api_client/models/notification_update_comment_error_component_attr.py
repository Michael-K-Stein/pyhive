from enum import Enum


class NotificationUpdateCommentErrorComponentAttr(str, Enum):
    COMMENT = "comment"

    def __str__(self) -> str:
        return str(self.value)
