from enum import Enum


class CourseExercisesPartialUpdateAutocheckTagErrorComponentAttr(str, Enum):
    AUTOCHECK_TAG = "autocheck_tag"

    def __str__(self) -> str:
        return str(self.value)
