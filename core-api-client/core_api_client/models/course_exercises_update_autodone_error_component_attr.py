from enum import Enum


class CourseExercisesUpdateAutodoneErrorComponentAttr(str, Enum):
    AUTODONE = "autodone"

    def __str__(self) -> str:
        return str(self.value)
