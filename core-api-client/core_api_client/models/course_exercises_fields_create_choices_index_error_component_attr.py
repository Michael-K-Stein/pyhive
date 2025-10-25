from enum import Enum


class CourseExercisesFieldsCreateChoicesINDEXErrorComponentAttr(str, Enum):
    CHOICES_INDEX = "choices.INDEX"

    def __str__(self) -> str:
        return str(self.value)
