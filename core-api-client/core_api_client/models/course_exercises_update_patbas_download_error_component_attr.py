from enum import Enum


class CourseExercisesUpdatePatbasDownloadErrorComponentAttr(str, Enum):
    PATBAS_DOWNLOAD = "patbas_download"

    def __str__(self) -> str:
        return str(self.value)
