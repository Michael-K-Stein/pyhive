from enum import Enum


class CourseExercisesFieldsUpdateLowerLimitErrorComponentAttr(str, Enum):
    LOWER_LIMIT = "lower_limit"

    def __str__(self) -> str:
        return str(self.value)
