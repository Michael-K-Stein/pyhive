from enum import Enum


class CourseExercisesFieldsCreateUpperLimitErrorComponentAttr(str, Enum):
    UPPER_LIMIT = "upper_limit"

    def __str__(self) -> str:
        return str(self.value)
