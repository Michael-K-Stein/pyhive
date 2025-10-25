from enum import Enum


class AssignmentsPartialUpdateDescriptionErrorComponentAttr(str, Enum):
    DESCRIPTION = "description"

    def __str__(self) -> str:
        return str(self.value)
