from enum import Enum


class CourseExercisesPartialUpdateDownloadErrorComponentAttr(str, Enum):
    DOWNLOAD = "download"

    def __str__(self) -> str:
        return str(self.value)
