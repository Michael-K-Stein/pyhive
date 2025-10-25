from enum import Enum


class CourseExercisesCreateStyleErrorComponentAttr(str, Enum):
    STYLE = "style"

    def __str__(self) -> str:
        return str(self.value)
