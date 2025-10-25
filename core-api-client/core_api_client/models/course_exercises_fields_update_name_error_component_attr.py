from enum import Enum


class CourseExercisesFieldsUpdateNameErrorComponentAttr(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
