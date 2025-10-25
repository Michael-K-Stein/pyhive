from enum import Enum


class AssignmentsListExerciseTagsIdInErrorComponentAttr(str, Enum):
    EXERCISE_TAGS_ID_IN = "exercise__tags__id__in"

    def __str__(self) -> str:
        return str(self.value)
