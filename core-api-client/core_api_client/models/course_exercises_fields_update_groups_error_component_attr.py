from enum import Enum


class CourseExercisesFieldsUpdateGroupsErrorComponentAttr(str, Enum):
    GROUPS = "groups"

    def __str__(self) -> str:
        return str(self.value)
