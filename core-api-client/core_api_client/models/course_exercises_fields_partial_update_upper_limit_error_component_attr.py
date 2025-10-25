from enum import Enum


class CourseExercisesFieldsPartialUpdateUpperLimitErrorComponentAttr(str, Enum):
    UPPER_LIMIT = "upper_limit"

    def __str__(self) -> str:
        return str(self.value)
