from enum import Enum


class CourseExercisesPartialUpdateParentModuleErrorComponentAttr(str, Enum):
    PARENT_MODULE = "parent_module"

    def __str__(self) -> str:
        return str(self.value)
