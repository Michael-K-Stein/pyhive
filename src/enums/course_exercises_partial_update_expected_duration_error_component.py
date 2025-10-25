from enum import Enum


class CourseExercisesPartialUpdateExpectedDurationErrorComponentCode(str, Enum):
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
