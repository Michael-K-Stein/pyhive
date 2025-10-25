from enum import Enum


class CourseExercisesPartialUpdatePatbasErrorComponentAttr(str, Enum):
    PATBAS = "patbas"

    def __str__(self) -> str:
        return str(self.value)
