from enum import Enum


class AssignmentsListExerciseParentModuleIdErrorComponentAttr(str, Enum):
    EXERCISE_PARENT_MODULE_ID = "exercise__parent_module__id"

    def __str__(self) -> str:
        return str(self.value)
