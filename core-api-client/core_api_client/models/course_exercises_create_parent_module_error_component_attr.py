from enum import Enum


class CourseExercisesCreateParentModuleErrorComponentAttr(str, Enum):
    PARENT_MODULE = "parent_module"

    def __str__(self) -> str:
        return str(self.value)
