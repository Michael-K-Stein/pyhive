from enum import Enum


class CourseExercisesFieldsPartialUpdateMetadataErrorComponentAttr(str, Enum):
    METADATA = "metadata"

    def __str__(self) -> str:
        return str(self.value)
