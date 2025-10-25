from enum import Enum


class AssignmentsResponsesPartialUpdateFileErrorComponentAttr(str, Enum):
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
