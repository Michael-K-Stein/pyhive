from enum import Enum


class ScheduleDailyReviewCreateHideWorkDetailsErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
