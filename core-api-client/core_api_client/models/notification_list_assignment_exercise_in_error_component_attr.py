from enum import Enum


class NotificationListAssignmentExerciseInErrorComponentAttr(str, Enum):
    ASSIGNMENT_EXERCISE_IN = "assignment__exercise__in"

    def __str__(self) -> str:
        return str(self.value)
