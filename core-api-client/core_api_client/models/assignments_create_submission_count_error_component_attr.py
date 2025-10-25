from enum import Enum


class AssignmentsCreateSubmissionCountErrorComponentAttr(str, Enum):
    SUBMISSION_COUNT = "submission_count"

    def __str__(self) -> str:
        return str(self.value)
