from enum import Enum


class AssignmentResponseTypeEnum(str, Enum):
    AUTOCHECK = "AutoCheck"
    COMMENT = "Comment"
    DONE = "Done"
    REDO = "Redo"
    SUBMISSION = "Submission"
    WORK_IN_PROGRESS = "Work In Progress"

    def __str__(self) -> str:
        return str(self.value)
