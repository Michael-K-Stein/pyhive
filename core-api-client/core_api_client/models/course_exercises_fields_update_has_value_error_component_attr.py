from enum import Enum


class CourseExercisesFieldsUpdateHasValueErrorComponentAttr(str, Enum):
    HAS_VALUE = "has_value"

    def __str__(self) -> str:
        return str(self.value)
