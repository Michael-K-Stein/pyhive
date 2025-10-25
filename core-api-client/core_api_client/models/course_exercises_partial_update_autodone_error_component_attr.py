from enum import Enum


class CourseExercisesPartialUpdateAutodoneErrorComponentAttr(str, Enum):
    AUTODONE = "autodone"

    def __str__(self) -> str:
        return str(self.value)
