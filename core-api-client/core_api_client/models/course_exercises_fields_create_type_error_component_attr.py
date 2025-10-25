from enum import Enum


class CourseExercisesFieldsCreateTypeErrorComponentAttr(str, Enum):
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
