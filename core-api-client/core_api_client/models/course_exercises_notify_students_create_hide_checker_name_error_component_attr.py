from enum import Enum


class CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponentAttr(str, Enum):
    HIDE_CHECKER_NAME = "hide_checker_name"

    def __str__(self) -> str:
        return str(self.value)
