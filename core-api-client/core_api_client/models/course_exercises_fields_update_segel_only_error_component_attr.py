from enum import Enum


class CourseExercisesFieldsUpdateSegelOnlyErrorComponentAttr(str, Enum):
    SEGEL_ONLY = "segel_only"

    def __str__(self) -> str:
        return str(self.value)
