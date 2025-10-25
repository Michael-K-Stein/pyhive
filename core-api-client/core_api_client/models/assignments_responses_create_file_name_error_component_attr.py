from enum import Enum


class AssignmentsResponsesCreateFileNameErrorComponentAttr(str, Enum):
    FILE_NAME = "file_name"

    def __str__(self) -> str:
        return str(self.value)
