from enum import Enum


class AssignmentsPartialUpdateSubmissionCountErrorComponentAttr(str, Enum):
    SUBMISSION_COUNT = "submission_count"

    def __str__(self) -> str:
        return str(self.value)
