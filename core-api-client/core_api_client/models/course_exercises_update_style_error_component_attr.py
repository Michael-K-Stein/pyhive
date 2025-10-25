from enum import Enum


class CourseExercisesUpdateStyleErrorComponentAttr(str, Enum):
    STYLE = "style"

    def __str__(self) -> str:
        return str(self.value)
