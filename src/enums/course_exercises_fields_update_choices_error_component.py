from enum import Enum


class CourseExercisesFieldsUpdateChoicesErrorComponentCode(str, Enum):
    NOT_A_LIST = "not_a_list"

    def __str__(self) -> str:
        return str(self.value)
