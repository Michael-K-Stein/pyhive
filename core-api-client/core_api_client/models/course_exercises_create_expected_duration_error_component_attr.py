from enum import Enum


class CourseExercisesCreateExpectedDurationErrorComponentAttr(str, Enum):
    EXPECTED_DURATION = "expected_duration"

    def __str__(self) -> str:
        return str(self.value)
