from enum import Enum


class CourseExercisesFieldsCreateOrderErrorComponentAttr(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
