from enum import Enum


class CourseExercisesFieldsPartialUpdateLowerLimitErrorComponentAttr(str, Enum):
    LOWER_LIMIT = "lower_limit"

    def __str__(self) -> str:
        return str(self.value)
