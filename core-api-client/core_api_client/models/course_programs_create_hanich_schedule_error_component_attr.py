from enum import Enum


class CourseProgramsCreateHanichScheduleErrorComponentAttr(str, Enum):
    HANICH_SCHEDULE = "hanich_schedule"

    def __str__(self) -> str:
        return str(self.value)
