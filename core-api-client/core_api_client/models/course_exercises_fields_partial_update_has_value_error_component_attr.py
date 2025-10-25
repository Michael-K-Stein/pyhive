from enum import Enum


class CourseExercisesFieldsPartialUpdateHasValueErrorComponentAttr(str, Enum):
    HAS_VALUE = "has_value"

    def __str__(self) -> str:
        return str(self.value)
