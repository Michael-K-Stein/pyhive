from enum import Enum


class QueuesItemsPartialUpdateSetExerciseIdErrorComponentAttr(str, Enum):
    SET_EXERCISE_ID = "set_exercise_id"

    def __str__(self) -> str:
        return str(self.value)
