from enum import Enum


class HelpResponsesCreateDearStudentErrorComponentAttr(str, Enum):
    DEAR_STUDENT = "dear_student"

    def __str__(self) -> str:
        return str(self.value)
