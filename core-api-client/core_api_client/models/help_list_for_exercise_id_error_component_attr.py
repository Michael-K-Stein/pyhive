from enum import Enum


class HelpListForExerciseIdErrorComponentAttr(str, Enum):
    FOR_EXERCISE_ID = "for_exercise__id"

    def __str__(self) -> str:
        return str(self.value)
