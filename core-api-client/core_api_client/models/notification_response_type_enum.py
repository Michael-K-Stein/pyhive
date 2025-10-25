from enum import Enum


class NotificationResponseTypeEnum(str, Enum):
    AUTOCHECK = "AutoCheck"
    COMMENT = "Comment"
    DONE = "Done"
    OPEN = "Open"
    REDO = "Redo"
    RESOLVE = "Resolve"
    SUBMISSION = "Submission"
    WORK_IN_PROGRESS = "Work In Progress"

    def __str__(self) -> str:
        return str(self.value)
