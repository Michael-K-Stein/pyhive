from enum import Enum


class CourseExercisesFieldsUpdateOrderErrorComponentAttr(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
