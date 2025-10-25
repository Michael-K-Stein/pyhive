from enum import Enum


class CourseExercisesUpdateParentModuleErrorComponentAttr(str, Enum):
    PARENT_MODULE = "parent_module"

    def __str__(self) -> str:
        return str(self.value)
