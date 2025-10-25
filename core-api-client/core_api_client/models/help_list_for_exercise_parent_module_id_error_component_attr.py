from enum import Enum


class HelpListForExerciseParentModuleIdErrorComponentAttr(str, Enum):
    FOR_EXERCISE_PARENT_MODULE_ID = "for_exercise__parent_module__id"

    def __str__(self) -> str:
        return str(self.value)
