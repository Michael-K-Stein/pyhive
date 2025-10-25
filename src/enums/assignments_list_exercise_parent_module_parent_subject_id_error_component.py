from enum import Enum


class AssignmentsListExerciseParentModuleParentSubjectIdErrorComponentCode(str, Enum):
    INVALID = "invalid"
    MAX_VALUE = "max_value"

    def __str__(self) -> str:
        return str(self.value)
