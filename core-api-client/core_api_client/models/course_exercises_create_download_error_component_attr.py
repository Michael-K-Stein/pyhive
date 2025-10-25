from enum import Enum


class CourseExercisesCreateDownloadErrorComponentAttr(str, Enum):
    DOWNLOAD = "download"

    def __str__(self) -> str:
        return str(self.value)
