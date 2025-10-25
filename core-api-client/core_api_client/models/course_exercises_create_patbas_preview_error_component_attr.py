from enum import Enum


class CourseExercisesCreatePatbasPreviewErrorComponentAttr(str, Enum):
    PATBAS_PREVIEW = "patbas_preview"

    def __str__(self) -> str:
        return str(self.value)
