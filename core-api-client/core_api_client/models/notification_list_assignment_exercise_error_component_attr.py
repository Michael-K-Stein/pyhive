from enum import Enum


class NotificationListAssignmentExerciseErrorComponentAttr(str, Enum):
    ASSIGNMENT_EXERCISE = "assignment__exercise"

    def __str__(self) -> str:
        return str(self.value)
