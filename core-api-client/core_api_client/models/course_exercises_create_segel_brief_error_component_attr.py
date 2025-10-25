from enum import Enum


class CourseExercisesCreateSegelBriefErrorComponentAttr(str, Enum):
    SEGEL_BRIEF = "segel_brief"

    def __str__(self) -> str:
        return str(self.value)
