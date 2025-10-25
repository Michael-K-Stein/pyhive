from enum import Enum


class CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponentAttr(str, Enum):
    CHOICES_INDEX = "choices.INDEX"

    def __str__(self) -> str:
        return str(self.value)
