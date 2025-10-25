from enum import Enum


class CourseExercisesCreateAutocheckTagErrorComponentAttr(str, Enum):
    AUTOCHECK_TAG = "autocheck_tag"

    def __str__(self) -> str:
        return str(self.value)
