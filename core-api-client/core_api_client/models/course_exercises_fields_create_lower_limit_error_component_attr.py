from enum import Enum


class CourseExercisesFieldsCreateLowerLimitErrorComponentAttr(str, Enum):
    LOWER_LIMIT = "lower_limit"

    def __str__(self) -> str:
        return str(self.value)
