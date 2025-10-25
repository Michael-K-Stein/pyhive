from enum import Enum


class CourseExercisesCreateExpectedDurationErrorComponentCode(str, Enum):
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
