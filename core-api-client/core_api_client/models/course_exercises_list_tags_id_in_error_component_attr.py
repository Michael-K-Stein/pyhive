from enum import Enum


class CourseExercisesListTagsIdInErrorComponentAttr(str, Enum):
    TAGS_ID_IN = "tags__id__in"

    def __str__(self) -> str:
        return str(self.value)
