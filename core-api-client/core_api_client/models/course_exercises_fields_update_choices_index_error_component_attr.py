from enum import Enum


class CourseExercisesFieldsUpdateChoicesINDEXErrorComponentAttr(str, Enum):
    CHOICES_INDEX = "choices.INDEX"

    def __str__(self) -> str:
        return str(self.value)
