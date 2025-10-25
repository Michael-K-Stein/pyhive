from enum import Enum


class CourseExercisesFieldsCreateHasValueErrorComponentAttr(str, Enum):
    HAS_VALUE = "has_value"

    def __str__(self) -> str:
        return str(self.value)
