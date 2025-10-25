from enum import Enum


class AssignmentStatusEnum(str, Enum):
    AUTOCHECKED = "AutoChecked"
    DONE = "Done"
    NEW = "New"
    REDO = "Redo"
    SUBMITTED = "Submitted"
    WORK_IN_PROGRESS = "Work In Progress"

    def __str__(self) -> str:
        return str(self.value)
