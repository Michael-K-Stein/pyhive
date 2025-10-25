from enum import Enum


class HelpPartialUpdateExerciseIdErrorComponentAttr(str, Enum):
    EXERCISE_ID = "exercise_id"

    def __str__(self) -> str:
        return str(self.value)
