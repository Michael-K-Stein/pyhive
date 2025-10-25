from enum import Enum


class CourseExercisesCreatePatbasDownloadErrorComponentAttr(str, Enum):
    PATBAS_DOWNLOAD = "patbas_download"

    def __str__(self) -> str:
        return str(self.value)
