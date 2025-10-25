from enum import Enum


class CourseExercisesUpdateDownloadErrorComponentAttr(str, Enum):
    DOWNLOAD = "download"

    def __str__(self) -> str:
        return str(self.value)
