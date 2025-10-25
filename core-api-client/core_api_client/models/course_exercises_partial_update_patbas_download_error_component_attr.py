from enum import Enum


class CourseExercisesPartialUpdatePatbasDownloadErrorComponentAttr(str, Enum):
    PATBAS_DOWNLOAD = "patbas_download"

    def __str__(self) -> str:
        return str(self.value)
