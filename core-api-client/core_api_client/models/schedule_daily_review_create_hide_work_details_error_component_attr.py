from enum import Enum


class ScheduleDailyReviewCreateHideWorkDetailsErrorComponentAttr(str, Enum):
    HIDE_WORK_DETAILS = "hide_work_details"

    def __str__(self) -> str:
        return str(self.value)
