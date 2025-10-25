from enum import Enum


class CourseExercisesFieldsCreateMetadataErrorComponentAttr(str, Enum):
    METADATA = "metadata"

    def __str__(self) -> str:
        return str(self.value)
