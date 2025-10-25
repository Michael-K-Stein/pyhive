from enum import Enum


class CourseExercisesFieldsUpdateChoicesErrorComponentAttr(str, Enum):
    CHOICES = "choices"

    def __str__(self) -> str:
        return str(self.value)
