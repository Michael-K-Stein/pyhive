from enum import Enum


class CourseExercisesUpdateOnCreationDataErrorComponentAttr(str, Enum):
    ON_CREATION_DATA = "on_creation_data"

    def __str__(self) -> str:
        return str(self.value)
