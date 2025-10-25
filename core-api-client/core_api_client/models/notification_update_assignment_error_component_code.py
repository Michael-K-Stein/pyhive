from enum import Enum


class NotificationUpdateAssignmentErrorComponentCode(str, Enum):
    DOES_NOT_EXIST = "does_not_exist"
    INCORRECT_TYPE = "incorrect_type"

    def __str__(self) -> str:
        return str(self.value)
