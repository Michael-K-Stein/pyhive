from enum import Enum


class CourseExercisesFieldsCreateRequiredErrorComponentAttr(str, Enum):
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
