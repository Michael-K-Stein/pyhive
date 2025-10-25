from enum import Enum


class CourseExercisesFieldsPartialUpdateTypeErrorComponentAttr(str, Enum):
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
