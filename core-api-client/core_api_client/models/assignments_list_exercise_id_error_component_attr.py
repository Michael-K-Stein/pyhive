from enum import Enum


class AssignmentsListExerciseIdErrorComponentAttr(str, Enum):
    EXERCISE_ID = "exercise__id"

    def __str__(self) -> str:
        return str(self.value)
