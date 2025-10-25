from enum import Enum


class CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponentAttr(str, Enum):
    CONTENTS_INDEX_FIELD = "contents.INDEX.field"

    def __str__(self) -> str:
        return str(self.value)
