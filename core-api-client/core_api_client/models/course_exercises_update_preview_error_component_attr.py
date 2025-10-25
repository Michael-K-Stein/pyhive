from enum import Enum


class CourseExercisesUpdatePreviewErrorComponentAttr(str, Enum):
    PREVIEW = "preview"

    def __str__(self) -> str:
        return str(self.value)
