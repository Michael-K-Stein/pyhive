from enum import Enum


class CourseProgramsPartialUpdateHanichWorkNameErrorComponentAttr(str, Enum):
    HANICH_WORK_NAME = "hanich_work_name"

    def __str__(self) -> str:
        return str(self.value)
