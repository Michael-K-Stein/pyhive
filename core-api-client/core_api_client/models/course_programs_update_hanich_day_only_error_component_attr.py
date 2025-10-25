from enum import Enum


class CourseProgramsUpdateHanichDayOnlyErrorComponentAttr(str, Enum):
    HANICH_DAY_ONLY = "hanich_day_only"

    def __str__(self) -> str:
        return str(self.value)
