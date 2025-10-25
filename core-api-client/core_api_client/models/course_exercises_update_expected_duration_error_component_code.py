from enum import Enum


class CourseExercisesUpdateExpectedDurationErrorComponentCode(str, Enum):
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
