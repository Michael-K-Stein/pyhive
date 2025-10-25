from enum import Enum


class CourseProgramsUpdateAutoScheduleErrorComponentAttr(str, Enum):
    AUTO_SCHEDULE = "auto_schedule"

    def __str__(self) -> str:
        return str(self.value)
