from enum import Enum


class CourseExercisesUpdateIsLectureErrorComponentAttr(str, Enum):
    IS_LECTURE = "is_lecture"

    def __str__(self) -> str:
        return str(self.value)
