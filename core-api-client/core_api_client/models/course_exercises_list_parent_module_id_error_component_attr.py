from enum import Enum


class CourseExercisesListParentModuleIdErrorComponentAttr(str, Enum):
    PARENT_MODULE_ID = "parent_module__id"

    def __str__(self) -> str:
        return str(self.value)
