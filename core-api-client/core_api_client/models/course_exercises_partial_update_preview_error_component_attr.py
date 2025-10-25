from enum import Enum


class CourseExercisesPartialUpdatePreviewErrorComponentAttr(str, Enum):
    PREVIEW = "preview"

    def __str__(self) -> str:
        return str(self.value)
