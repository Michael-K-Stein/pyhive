from enum import Enum


class CourseExercisesFieldsDuplicateCreateNameErrorComponentAttr(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
