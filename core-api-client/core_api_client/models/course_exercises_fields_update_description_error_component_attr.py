from enum import Enum


class CourseExercisesFieldsUpdateDescriptionErrorComponentAttr(str, Enum):
    DESCRIPTION = "description"

    def __str__(self) -> str:
        return str(self.value)
