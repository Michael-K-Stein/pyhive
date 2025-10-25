from enum import Enum


class CourseExercisesUpdateExpectedDurationErrorComponentAttr(str, Enum):
    EXPECTED_DURATION = "expected_duration"

    def __str__(self) -> str:
        return str(self.value)
