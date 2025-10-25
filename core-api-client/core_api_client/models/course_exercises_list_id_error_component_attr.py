from enum import Enum


class CourseExercisesListIdErrorComponentAttr(str, Enum):
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
